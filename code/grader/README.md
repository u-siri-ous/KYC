# The Grader

The grader was implemented using the BGS grading scale and OpenCV.
The usage of an automated tool was deemed necessary, as it is often hard to evaluate a card based solely on the naked eye of a newcomer. The condition value is crucial, as it indicates the card's state and influences its market price.

## Beckett Grading Services (BGS)

Beckett Grading Services ensures a fair and comprehensive card evaluation based on four factors:

- **Centering**
- **Corners**
- **Edges**
- **Surface**

and a score from 1 to 10 in each of them accordingly, with half-points for in-between characteristics.
The card will then be assigned a category according to the score in each factor.
<div align="center">
    <img width="600" alt="Screenshot 2024-03-02 alle 20 04 06" src="https://github.com/LeoRamill/KYC/assets/161584956/ed547e26-d27f-4a8e-8bb0-d774e6385c55">
</div>




## Implementing a Grader using OpenCV

The grader uses image transformation techniques for each of the categories mentioned above.

In particular, the surface evaluation was obtained by averaging the three other values, as it strongly depends on the card's condition in general. Specifically, surface condition depends on flaws that are most likely not visible in a picture.

The classifier is of use in cases where some info cannot be retained because of evident damages, such as an entire part of the card cut away, in which the grade would be low, but all info can still be displayed either way. For the scope of this project, the focus was on the front centering rather than the back centering. 

The HSV colorspace was used to identify yellow through saturation and color values using thresholds, after which, the result was binarized to get a mask. This also helped in locating the card in the picture and cutting it out.

```python
lower_yellow = np.array([20, 100, 100], dtype=np.uint8)
upper_yellow = np.array([30, 255, 255], dtype=np.uint8)

# Create a binary mask where pixels falling within the yellow color range become white (255) and others black (0)
mask = cv.inRange(hsv_image, lower_yellow, upper_yellow)
```
