
from PIL import Image

ImaR1 = Image.open("VideoMap.png")
ImaR1.show()

I1 = ImaR1.convert('L')
I1.show()

I2 = I1.copy()
I2.thumbnail((320, 320))
I2.show()

I3 = I1.copy()
I3.transpose(Image.ROTATE_180).show()

I4 = ImaR1.copy()
I4.transpose(Image.FLIP_LEFT_RIGHT).show()

I5 = I1.copy()
I5.rotate(45).show()
I6 = I5.rotate(45)

DPI = (300, 300)

I6.save("45.jpg",
        dpi = DPI,
        quality = 100)