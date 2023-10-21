import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label


def crop(labeled, label=1):
    image = np.where(labeled == label)
    zeros = np.zeros((max(image[0]) - min(image[0]) + 1, max(image[1]) - min(image[1]) + 1))
    for i in range(len(image[0])):
        zeros[image[0][i] - min(image[0])][image[1][i] - min(image[1])] = 1

    arr = []
    for i in range(zeros.shape[0]):
        arr.append([])
        for l in range(zeros.shape[1]):
            arr[-1].append(zeros[i][l])
    return arr


image = label(np.load("ps.npy.txt"))

arrays = []
count = []
for i in range(1, np.max(image) + 1):
    figure = crop(image, i)
    if figure not in arrays:
        arrays.append(figure)
        count.append(0)
    count[arrays.index(figure)] += 1

for i in range(len(arrays)):
    print(f"Фигура вида {i + 1}: {count[i]}")
    plt.imshow(arrays[i])
    plt.show()

print(f"Всего фигур: {sum(count)}")
