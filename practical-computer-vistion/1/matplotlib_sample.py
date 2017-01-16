import numpy as np
from PIL import Image
from matplotlib import pylab as plt

im = np.array(Image.open('../../images/lena.jpg'))
plt.imshow(im)

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

plt.plot(x, y, 'r*')
plt.plot(x[:2], y[:2])


plt.title('Plotting: "empire.jpg"')

plt.show()
