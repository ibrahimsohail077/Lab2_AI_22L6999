

import matplotlib.pyplot as plt
import numpy as np
import urllib.request
from PIL import Image


urllib.request.urlretrieve(
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6Ns6SbqQCUFhCZcuqiPydWw4yFdO_oUFbUw&s',
    "johan.png")


img = Image.open("johan.png")


img_array = np.array(img)



plt.figure(figsize=(8, 6))
plt.imshow(img_array)
plt.title("Original Image")
plt.show()


rotated_img = np.rot90(img_array)


plt.figure(figsize=(8, 6))
plt.imshow(rotated_img)
plt.title("Rotated Image")
plt.show()



flipped_img = np.fliplr(img_array)


plt.figure(figsize=(8, 6))
plt.imshow(flipped_img)
plt.title("Flipped Image")
plt.show()



gray_img = np.dot(img_array[..., :3], [0.299, 0.587, 0.114])


plt.figure(figsize=(8, 6))
plt.imshow(gray_img, cmap='gray')  
plt.title("Grayscale Image")
plt.show()
