import sys
from picture import Picture
from blob import Blob
from beadfinder import BeadFinder
from glob import glob


def main():
    min_pixels = float(sys.argv[1])

    tau = float(sys.argv[2])

    delta = float(sys.argv[3])

    # fix error when we have * in args

    pictures = sys.argv[4:] if len(sys.argv) > 5 else glob(sys.argv[4])

    for i in range(len(pictures) - 1):
        # Get the beads and calculate Radial displacement

        beads_One = BeadFinder(Picture(pictures[i]), tau).getBeads(min_pixels)

        beads_Two = BeadFinder(Picture(pictures[i + 1]), tau).getBeads(min_pixels)

        for bead_One in beads_One:

            small_lest = float('inf')

            for bead_Two in beads_Two:

                distance = bead_One.distanceTo(bead_Two)

                if distance < small_lest and distance <= delta:

                    small_lest = distance

            if small_lest <= delta:

                print('%.4f' %small_lest)  # print for us Radial displacement

        print()


if __name__ == "__main__":
    main()