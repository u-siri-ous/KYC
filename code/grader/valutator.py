import cv2 as cv
from grader.refine import detect_edges

def grading(path):
    image, _, _ = detect_edges(path)
    height, width = image.shape
    left, right, up, down = borders(image, height, width)

    cen = centering(left, right, up, down)
    cor = corners(image, height, width, left, right, up, down)
    edg = edges(image, height, width, left, right, up, down)
    sur = (cen + cor + edg)//3
    return cen, cor, edg, sur

def borders(image, height, width):
    middle_x = width // 2
    middle_y = height // 2

    # Initialize counters and flags
    left = 0
    right = 0
    up = 0
    down = 0

    # Calculate width on the left
    end = False
    for w in range(width):
        c = image[middle_y, w]
        if c == 0 and not end:
            pass
        if c == 255:
            left += 1
            end = True
        if c == 0 and end:
            break

    # Calculate width on the right
    end = False
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

def centering(left, right, up, down):
    horizontal_ratio = int((left / right) * 10) if left < right else int((right / left) * 10)
    vertical_ratio = int((up / down) * 10) if up < down else int((down / up) * 10)

    return (vertical_ratio + horizontal_ratio) // 2

def white_pixeles(corner):
    percentage_white_pixels = (cv.countNonZero(corner) / corner.size) * 10
    return int(percentage_white_pixels + 1)

def corners(image, height, width, left, right, up, down):

    # Calculate the percentage of white pixels for each corner
    top_left_corner = white_pixeles(image[0:up, 0:left])
    top_right_corner = white_pixeles(image[0:up, width - right:width])
    bottom_left_corner = white_pixeles(image[height - down:height, 0:left])
    bottom_right_corner = white_pixeles(image[height - down:height, width - right:width])

    # Calculate the average percentage of white pixels for all corners
    average_corner_percentage = (top_left_corner + top_right_corner + bottom_left_corner + bottom_right_corner) // 4

    return average_corner_percentage

def edges(image, height, width, left, right, up, down):

    # Calculate the percentage of white pixels for each edge
    top_edge = white_pixeles(image[0:up, 0:width])
    right_edge = white_pixeles(image[0:height, width - right:width])
    bottom_edge = white_pixeles(image[height - down:height, 0:width])
    left_edge = white_pixeles(image[0:height, 0:left])

    # Calculate the average percentage of white pixels for all edges
    average_edge_percentage = (top_edge + right_edge + bottom_edge + left_edge) // 4

    print()
    return average_edge_percentage

if __name__ == "__main__":
    pass