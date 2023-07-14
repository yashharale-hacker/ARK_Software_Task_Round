from utils import Player, WINDOW_WIDTH
import cv2
import numpy as np

player = Player()


# Initializing a Player object with a random start position on a randomly generated Maze

def strategy():
    # This function is to localize the position of the newly created player with respect to the map
    maze = player.getMap()  # main image already in gray scale
    snapShot = player.getSnapShot()  # template
    # Assuming same size of snapShot in map also.

    w, h = snapShot.shape[::-1]

    match = cv2.matchTemplate(maze, snapShot, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8

    (y_points, x_points) = np.where(match >= threshold)

    boxes = list()

    # zip map 2 or more iterables into single iterable
    for (x, y) in zip(x_points, y_points):
        boxes.append((x, y, x + w, y + h))

    for (x1, y1, x2, y2) in boxes:
        cv2.rectangle(maze, (x1, y1), (x2, y2), (0, 0, 0), 2)

    cv2.imshow("maze", maze)
    cv2.imshow("surrounding", snapShot)

    # player.move_horizontal(10)
    # cv2.imshow("surroundingnew", player.getSnapShot())
    # player.move_horizontal(10)
    # cv2.imshow("surroundingnew1", player.getSnapShot())
    # player.move_horizontal(10)
    # cv2.imshow("surroundingnew2", player.getSnapShot())

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    strategy()

