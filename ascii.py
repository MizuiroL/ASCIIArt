import sys
from PIL import Image

ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

img1 = Image.open("FILE_NAME")
print 'Image size:', img1.size

pixelMatrix = list(img1.getdata())
width, height = img1.size
pixelMatrix = [pixelMatrix[i * width:(i + 1) * width] for i in xrange(height)]

for x in xrange(height):
    for y in xrange(width):
        pixel = pixelMatrix[x][y]
        pixelMatrix[x][y] = (pixel[0] + pixel[1] + pixel[2]) / 3
        pixelMatrix[x][y] = ASCII_CHARS[pixelMatrix[x][y] / 4]
        sys.stdout.write(pixelMatrix[x][y])
    print ''
