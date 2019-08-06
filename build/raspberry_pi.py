import subprocess
import argparse
import glob
import sys
import os


class RaspberryPi(object):

    def __init__(self, local_drive, verbose=False):
        self.devnull = open(os.devnull, "w")
        self.verbose = verbose
        self.drive = local_drive

    def bootstrap(self):
        pass

    def format(self):
        cmd = ("bash `pwd`/../docker/scripts/raspberry_pi/emmc/format.sh ")
        cmd += ("{}".format(self.drive))
        subprocess.call(cmd, shell=True)

    def get_binaries(self):
        cmd = ("bash `pwd`/../docker/scripts/raspberry_pi/emmc/" + \
               "get_binaries.sh")
        subprocess.call(cmd, shell=True)

    def run(self):
        self.format()

def main():
    parser = argparse.ArgumentParser()
    required = parser.add_argument_group('Required arguments')
    required.add_argument("-d", "--drive", action="store",
                          help="Local drive to format and prepare. " + \
                               "Example: /dev/sdn", required=True)
    required.add_argument("-v", "--verbose", action="store_true",
                          help="Display output (default False)")
    args = parser.parse_args()
    if args.verbose:
        raspberrypi = RaspberryPi(args.drive, args.verbose)
        raspberrypi.run()
    else:
        raspberrypi = RaspberryPi(args.drive)
        raspberrypi.run()

if __name__ == ("__main__"):
    main()