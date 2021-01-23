

class Blob():
    def __init__(self):
        self.center_blob = [0, 0]  # Blob center coordinate list
        self.pix = []  # coordinates of blob's pixels [(12,23), (23,34)]

    def add(self, x, y):
        """"
        add x and y to the list of pixels
        """
        # update the center
        self.center_blob[0] = (self.center_blob[0] * self.mass() + x) / (self.mass() + 1)
        self.center_blob[1] = (self.center_blob[1] * self.mass() + y) / (self.mass() + 1)
        # add this pixel to 
        self.pix.append((x, y))

    def mass(self):
        """
        return count of pixels in blob
        """
        return len(self.pix)

    def distanceTo(self, c):
        # euclidean distance between two blobs
        dx = (c.center_blob[0] - self.center_blob[0]) ** 2
        dy = (c.center_blob[1] - self.center_blob[1]) ** 2
        return (dx + dy) ** 0.5
    
    def __str__(self):
        """
        return string representation of the Blob object
        """
        return '{} ({}, {})'.format('%2d' %self.mass(), '%7.4f' %self.center_blob[0], '%7.4f' %self.center_blob[1])



if __name__ == "__main__":
    tau = 180  # color threshold
    min_pixels = 25  # minimum of pixels to make a blob
