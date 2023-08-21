import cv2 as cv
from grader.refine import detect_edges

def grading(path):
    cen = centering(path)
    cor = corners(path)
    edg = edges(path)
    sur = (cen + cor + edg)//3

    print(f"Centering: {cen}")
    print(f"Corners: {cor}")
    print(f"Edges: {edg}")
    print(f"Surface: {sur}")
    return cen, cor, edg, sur

def borders(image):
    height, width = image.shape
    middle_x = width // 2
    middle_y = height // 2

    # Initialize counters and flags
    left = 0
    right = 0
    up = 0
    down = 0
    end = False

    # Calculate width on the left
    for w in range(width):
        c = image[middle_y, w]
        if c == 0 and not end:
            pass
        if c == 255:
            left += 1
            end = True
        if c == 0 and end:
            break

    # Reset the flag for the right side
    end = False

    # Calculate width on the right
    for w in range(width - 1, -1, -1):
        c = image[middle_y, w]
        if c == 0 and not end:
            pass
        if c == 255:
            right += 1
            end = True
        if c == 0 and end:
            break

    # Calculate height on the top
    end = False
    for h in range(height):
        c = image[h, middle_x]
        if c == 0 and not end:
            pass
        if c == 255:
            up += 1
            end = True
        if c == 0 and end:
            break

    # Reset the flag for the bottom side
    end = False
    for h in range(height - 1, -1, -1):
        c = image[h, middle_x]
        if c == 0 and not end:
            pass
        if c == 255:
            down += 1
            end = True
        if c == 0 and end:
            break

    return left, right, up, down

def centering(image_path):
    # Load the image
    image, _, _, _ = detect_edges(image_path)

    left, right, up, down = borders(image)

    # print('left:', left)
    # print('right:', right)
    # print('up:', up)
    # print('down:', down)

    # Calculate and display ratios
    print(f"{image_path.split('/')[-1].split('.')[0]}:")

    if left < right:
        # print('Orizzontal ratio:', int((left / right)*10))
        orizzontal = int(left / right)*10
    else:
        # print('Orizzontal ratio:', int((right / left)*10))
        orizzontal = int((right / left)*10)

    if up < down:
        # print('Vertical ratio:', int((up / down)*10))
        vertical = int((up / down)*10)
    else:
        # print('Vertical ratio:', int((down / up)*10))
        vertical = int((down / up)*10)
    # print()
    return (vertical + orizzontal) // 2

def white_pixeles(corner):
    white_pixel_count = cv.countNonZero(corner)
    total_pixels = corner.size
    percentage_white_pixels = (white_pixel_count / total_pixels) * 10
    return int(percentage_white_pixels + 1)

def corners(image_path):
    # Load the image
    image, _, _, _ = detect_edges(image_path)
    left, right, up, down = borders(image)
    height, width = image.shape

    # top-left corner
    tl = white_pixeles(image[0:up, 0:left])
    # print(f"Percentage of white pixels in the top-left corner: {tl + 1}")

    # top-right corner
    tr = white_pixeles(image[0:up, width - right:width])
    # print(f"Percentage of white pixels in the top-right corner: {tr + 1}")

    # bottom-left corner
    bl = white_pixeles(image[height - down:height, 0:left])
    # print(f"Percentage of white pixels in the bottom-left corner: {bl + 1}")

    # bottom-right corner
    br = white_pixeles(image[height - down:height, width - right:width])
    # print(f"Percentage of white pixels in the bottom-right corner: {br + 1}")

    # print()
    return (tl + tr + bl + br)//4

def edges(image_path):
    # Load the image
    image, _, _, _ = detect_edges(image_path)
    left, right, up, down = borders(image)
    height, width = image.shape

    # top edge
    t = white_pixeles(image[0:up, 0:width])
    # print(f"Percentage of white pixels in the top edge: {t}")

    # right edge
    r = white_pixeles(image[0:height, width - right:width])
    # print(f"Percentage of white pixels in the right edge: {r}")

    # bottom edge
    b = white_pixeles(image[height - down:height, 0:width])
    # print(f"Percentage of white pixels in the bottom edge: {b}")

    # left edge
    l = white_pixeles(image[0:height, 0:left])
    # print(f"Percentage of white pixels in the left edge: {l}")

    print()
    return (t + r + b + l) // 4

if __name__ == "__main__":
    pass