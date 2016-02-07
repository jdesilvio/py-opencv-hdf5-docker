import cv2
import h5py
import numpy

image = cv2.imread("testImage.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hu = cv2.HuMoments(cv2.moments(image)).flatten()
nphu = numpy.array(hu)
print(hu)
print(nphu)

h5f = h5py.File('../h5data/opencvTest.h5', 'w')
h5f.create_dataset('dataset_1', data=nphu)
print(h5f)
h5f.close()

h5fget = h5py.File('../h5data/opencvTest.h5','r')
x = h5fget['dataset_1'][:]
h5fget.close()

print(x)
