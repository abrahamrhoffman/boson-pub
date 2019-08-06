import subprocess
import argparse
import glob
import sys
import os

import bootstrap


class RaspberryPi(object):

    def __init__(self, local_drive, arch, container, verbose=False):
        self.devnull = open(os.devnull, "w")
        self.container = container
        self.drive = local_drive
        self.verbose = verbose
        self.arch = arch

    def start_bootstrap(self):
        name = ("abehoffman/boson-pub:{}".format(self.container))
        btstrp = bootstrap.BootStrap(self.container)
        btstrp.run()

    def format(self):
        cmd = ("bash `pwd`/../docker/scripts/raspberry_pi/emmc/format.sh ")
        cmd += ("{}".format(self.drive))
        subprocess.call(cmd, shell=True)

    def get_binaries(self):
        cmd = ("bash `pwd`/../docker/scripts/raspberry_pi/emmc/" + \
               "get_binaries.sh")
        subprocess.call(cmd, shell=True)

    def run(self):
        self.start_bootstrap()
        #self.format()
        #self.get_binaries()


def main():
    parser = argparse.ArgumentParser()
    required = parser.add_argument_group('Required arguments')
    required.add_argument("-i", "--image", action="store",
                          help="Boson container version.  Ex: 1.0.5",
                          required=True)
    required.add_argument("-d", "--drive", action="store",
                          help="Local drive to format and prepare. " + \
                               "Example: /dev/sdn", required=True)
    required.add_argument("-a", "--arch", action="store",
                          help="CPU architecture: 64 [or] 32",
                          required=True)
    required.add_argument("-v", "--verbose", action="store_true",
                          help="Display output (default False)")
    args = parser.parse_args()
    if args.verbose:
        raspberrypi = RaspberryPi(args.drive, args.arch, args.verbose)
        raspberrypi.run()
    else:
        raspberrypi = RaspberryPi(args.drive, args.arch)
        raspberrypi.run()

if __name__ == ("__main__"):
    main()