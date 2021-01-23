
# -----------------------------------------------------------------------
import sys
import stddraw
from color import Color
from picture import Picture
from blob import Blob
import stdarray
# -----------------------------------------------------------------------


class BeadFinder:
    def __init__(self, picture, tau):
        """
        Constructs a blob finder to find blobs in the picture pic,using of threshold tau
        """
        self.tau = tau
        self.photo = picture
        # create a array with picture size
        check = stdarray.create2D(self.photo.height(), self.photo.width(), False)

        # list of blobs
        self.blobs = []

        #  Modifies RGB photos
        for i in range(self.photo.height()):
            for j in range(self.photo.width()):
                color = self.photo.get(j, i)
                r = color.getRed()
                g = color.getGreen()
                b = color.getBlue()
                if r >= self.tau and g >= self.tau and b >= self.tau:
                    check[i][j] = True

        for i in range(self.photo.height()):
            for j in range(self.photo.width()):
                if check[i][j]:
                    blob = Blob()
                    self.proccess(blob, check, i, j)
                    self.blobs.append(blob)

    def getBeads(self, min_pixels):

        """
        Returns a list of all beads at least with min_pixels pixels.
        """

        beads = []
        for i in self.blobs:
            if i.mass() >= min_pixels:
                beads.append(i)
        return beads


    def proccess(self, blob, array, i=0, j=0):
        if not array[i][j]:
            return

        # mark the pixel if it is white
        blob.add(j, i)
        array[i][j] = False

        # try catch for prvent index out of range

        try:
            self.proccess(blob, array, i + 1, j)  # Check Up
        except:
            pass
        try:
            self.proccess(blob, array, i, j + 1)  # Check Right
        except:
            pass
        try:
            self.proccess(blob, array, i - 1, j)  # Check Down
        except:
            pass
        try:
            self.proccess(blob, array, i, j - 1)  # Check left
        except:
            pass


def main():
    # for test this class
    min_pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    img = Picture(sys.argv[3])

    bf = BeadFinder(img, tau)
    beads = bf.getBeads(min_pixels)

    for i in beads:
        print(str(i))

if __name__ == "__main__":
    main()
