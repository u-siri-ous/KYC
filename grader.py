import cv2 as cv
from refine import detect_edges

def calculate_dimensions(image, middle_x, middle_y):
    height, width = image.shape

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
    image, _ = detect_edges(image_path)

    # Calculate the middle point
    middle_x = image.shape[1] // 2
    middle_y = image.shape[0] // 2

    left, right, up, down = calculate_dimensions(image, middle_x, middle_y)

    # print('left:', left)
    # print('right:', right)
    # print('up:', up)
    # print('down:', down)

    # Calculate and display ratios
    print(f"{image_path.split('/')[-1].split('.')[0]}:")

    if left < right:
        print('Orizzontal ratio:', int((left / right)*10))
    else:
        print('Orizzontal ratio:', int((right / left)*10))

    if up < down:
        print('Vertical ratio:', int((up / down)*10))
    else:
        print('Vertical ratio:', int((down / up)*10))
    print()

if __name__ == "__main__":
    centering()