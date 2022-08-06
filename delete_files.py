from cProfile import label
import os


images = os.listdir("E:\YOLO_object_detection\Data")

labels = os.listdir("E:\YOLO_object_detection\Data\edited")

images = [im[:-4] for im in images]
labels = [l[:-4] for l in labels]

print(len(images))
print(len(labels))


non = []

[non.append(im) for im in images if im not in labels]

print("this is non")
print(non)

