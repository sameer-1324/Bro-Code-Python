import numpy as np

array = np.array([[['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L']],
                  [['M', 'N', 'O', 'P'], ['Q', 'R', 'S', 'T'], ['U', 'V', 'W', 'X']],
                  [['Y', 'Z', '1', '2'], ['3', '4', '5', '6'], ['7', '8', '9', '10']]])

word = array[0, 0, 0] + array[1, 0, 3] + array[1, 0, 3] + array[0, 2, 3] + array[0, 1, 0]

print(word)