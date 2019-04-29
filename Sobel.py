from PIL import Image, ImageFilter
import numpy as np
import math

class Sobel:
    def __init__(self, path):
        self.im = Image.open(path).convert('L')
        self.width, self.height = self.im.size
        self.GaussianBlur(self.im)
        mat = self.im.load()
        sobelx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
        sobely = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]

        self.sobelIm = Image.new('L', (self.width, self.height))
        pixels = self.sobelIm.load()

        linScale = .25

        # For each pixel in the image
        for row in range(self.width - len(sobelx)):
            for col in range(self.height - len(sobelx)):
                Gx = 0
                Gy = 0
                for i in range(len(sobelx)):
                    for j in range(len(sobely)):
                        val = mat[row + i, col + j] * linScale
                        Gx += sobelx[i][j] * val
                        Gy += sobely[i][j] * val

                pixels[row + 1, col + 1] = int(math.sqrt(Gx * Gx + Gy * Gy))
        self.ImageSave(self.sobelIm)

    def GaussianBlur(self, image, Radius=2):
        """
        :param image: Image that we want to use blur
        """
        return image.filter(ImageFilter.GaussianBlur())
    def ImageSave(self,image):
        self.sobelIm.save("sobelFiltered.jpg")
