from PIL import Image
import numpy as np

img_path = 'room.jpg'
I = Image.open(img_path)
im = np.array(I)
print(im.dtype, im.shape)

im1 = 255 - im
im2 = (100 / 255) * 255 + 150
im3 = 255 * (im / 255) ** 2
pil_im = Image.fromarray(np.uint8(im3))
pil_im.show()
pil_im.save(img_path.split('.')[0] + '_convert.' + img_path.split('.')[1])
