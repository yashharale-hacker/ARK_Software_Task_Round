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

# maze_gray = cv2.cvtColor(maze, cv2.COLOR_BGR2GRAY)
# snapShot_gray = cv2.cvtColor(snapShot, cv2.COLOR_BGR2GRAY)

# print(len(snapShot), len(map), len(snapShot[1]), len(map[1]))
# print(map, snapShot)
# print(height, width)
# h, w = snapShot.shape[::-1]
# print(h, w)

# Store the coordinates of matched area in a numpy array
    # loc = np.where(match >= threshold)

    # zip map 2 or more iterables into single iterable
    # for pt in zip(*loc[::-1]):
    #     cv2.rectangle(maze, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

'''
def non_max_suppression_fast(boxes, overlapThresh):
	# if there are no boxes, return an empty list
	if len(boxes) == 0:
		return []
	# if the bounding boxes integers, convert them to floats --
	# this is important since we'll be doing a bunch of divisions
	if boxes.dtype.kind == "i":
		boxes = boxes.astype("float")
	# initialize the list of picked indexes	
	pick = []
	# grab the coordinates of the bounding boxes
	x1 = boxes[:,0]
	y1 = boxes[:,1]
	x2 = boxes[:,2]
	y2 = boxes[:,3]
	# compute the area of the bounding boxes and sort the bounding
	# boxes by the bottom-right y-coordinate of the bounding box
	area = (x2 - x1 + 1) * (y2 - y1 + 1)
	idxs = np.argsort(y2)
	# keep looping while some indexes still remain in the indexes
	# list
	while len(idxs) > 0:
		# grab the last index in the indexes list and add the
		# index value to the list of picked indexes
		last = len(idxs) - 1
		i = idxs[last]
		pick.append(i)
		# find the largest (x, y) coordinates for the start of
		# the bounding box and the smallest (x, y) coordinates
		# for the end of the bounding box
		xx1 = np.maximum(x1[i], x1[idxs[:last]])
		yy1 = np.maximum(y1[i], y1[idxs[:last]])
		xx2 = np.minimum(x2[i], x2[idxs[:last]])
		yy2 = np.minimum(y2[i], y2[idxs[:last]])
		# compute the width and height of the bounding box
		w = np.maximum(0, xx2 - xx1 + 1)
		h = np.maximum(0, yy2 - yy1 + 1)
		# compute the ratio of overlap
		overlap = (w * h) / area[idxs[:last]]
		# delete all indexes from the index list that have
		idxs = np.delete(idxs, np.concatenate(([last],
			np.where(overlap > overlapThresh)[0])))
	# return only the bounding boxes that were picked using the
	# integer data type
	return boxes[pick].astype("int")
'''
