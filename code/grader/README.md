# The Grader

The grader was implemented using the BGS grading scale and OpenCV.
The usage of an automated tool was deemed necessary, as it is often hard to evaluate a card based solely on the naked eye of a newcomer. The condition value is crucial, as it indicates the card's state and influences its market price.

## Beckett Grading Services (BGS)

Beckett Grading Services ensures a fair and comprehensive card evaluation based on four factors:

- Centering
- Corners
- Edges
- Surface

and a score from 1 to 10 in each of them accordingly, with half-points for in-between characteristics.
The card will then be assigned a category according to the score in each factor.

$$
\begin{table}[ht]
    \centering
    \resizebox{\linewidth}{!}{
    \begin{tabular}{c|c|c|c}
    \hline
    \textbf{Category} & \textbf{Grade} & \textbf{Front Centering} & \textbf{Back Centering}  \\
    \hline
        Pristine & 10 & $\geq$ 50/50 both ways & $\geq$ 60/40  \\
        Gem Mint & 9.5 & $\geq$	50/50 one way, $\geq$ 55/45 other & $\geq$ 60/40  \\
        Mint & 9 to 8 & $\geq$ 55/45 both ways & $\geq$ 70/30 \\
        Near Mint & 8 to 7 & both ways between 60/40 and 65/35 & between 80/20 and 90/10 \\
        Excellent Mint & 6 & $\geq$	70/30 both ways & $\geq$ 95/5 \\
        Excellent & 5 to 4 & $\geq$ 75/25 both ways & $\geq$ 95/5  \\
        Very Good & 4 to 3 & both ways between 80/20 and 85/15 & $\geq$ 100/0 \\
        Good & 2 & $\geq$ 90/10 both ways & 100/0 or offcut \\
        Poor & 1 & 100/0 or offcut & 100/0 or offcut \\
    \hline
    \end{tabular}}
    %
    \newline
    \vspace{0.2em}
    \newline
    %
    \resizebox{\linewidth}{!}{
    \begin{tabular}{c|c|c}
    \hline
    \textbf{Corners} & \textbf{Edges} & \textbf{Surface} \\
    \hline
        Perfect & Perfect & Flawless color and gloss \\
        Mint & Mint & Extremely minor flaws, scratchless\\
        Mint & Mint & Minor spots and scratches \\
        Sharp with minor imperfections & Relatively smooth & Minor speckling with occasional print spots \\
        Fuzzy but not frayed & Moderate chipping & Minor discoloration and noticeable spots \\
        Fuzzy with minor ding & Rough with no layering & Minor imperfections and discoloration \\
        Notched with minor layering & Chipped with layering & Heavy print spots and moderate imperfections \\
        Moderately layered & Severely chipped & Severe print spots and imperfections \\
        Noticeably layered & Destructively chipped & Severe imperfections and creases \\
    \hline
    \end{tabular}}
    \label{tab:my_label1}
\end{table}
$$

## Implementing a Grader using OpenCV

The grader uses image transformation techniques for each of the categories mentioned above.

In particular, the surface evaluation was obtained by averaging the three other values, as it strongly depends on the card's condition in general. Specifically, surface condition depends on flaws that are most likely not visible in a picture.

The classifier is of use in cases where some info cannot be retained because of evident damages, such as an entire part of the card cut away, in which the grade would be low, but all info can still be displayed either way. For the scope of this project, the focus was on the front centering rather than the back centering. 

The HSV colorspace was used to identify yellow through saturation and color values using thresholds, after which, the result was binarized to get a mask.

This also helped in locating the card in the picture and cutting it out.

```python
lower_yellow = np.array([20, 100, 100], dtype=np.uint8)
upper_yellow = np.array([30, 255, 255], dtype=np.uint8)

# Create a binary mask where pixels falling within the yellow color range become white (255) and others black (0)
mask = cv.inRange(hsv_image, lower_yellow, upper_yellow)
```