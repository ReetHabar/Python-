import matplotlib.pyplot as plt
import numpy as np

# test_image = np.random.rand(100, 100)  # Random grayscale image
# plt.imshow(test_image, cmap='gray')
# plt.title('Test Image')
# plt.axis('off')
# plt.show()
# # import matplotlib
# # print(matplotlib.__version__)  # Should print the version
x=np.array([1,2,3,4,7])
y=np.array([1,4,9,16,25])
plt.figure(figsize=(4,3))
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel("y")
plt.show()