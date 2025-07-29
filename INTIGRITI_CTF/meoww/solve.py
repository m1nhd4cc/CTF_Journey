from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh
img = Image.open('flag.png')
img_array = np.array(img)

# Tách và hiển thị từng kênh màu
plt.figure(figsize=(15, 5))

plt.subplot(141)
plt.imshow(img_array)
plt.title('Original')

plt.subplot(142)
plt.imshow(img_array[:,:,0], cmap='gray')  # Red channel
plt.title('Red Channel')

plt.subplot(143)
plt.imshow(img_array[:,:,1], cmap='gray')  # Green channel
plt.title('Green Channel')

plt.subplot(144)
plt.imshow(img_array[:,:,2], cmap='gray')  # Blue channel
plt.title('Blue Channel')

plt.show()

# Thử nghịch đảo màu
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.imshow(img_array)
plt.title('Original')

plt.subplot(122)
plt.imshow(255 - img_array)  # Invert colors
plt.title('Inverted')

plt.show()
