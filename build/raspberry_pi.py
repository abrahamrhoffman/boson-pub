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
        btstrp = bootstrap.BootStrap(self.container)
        btstrp.run()

    def build_uboot(self):
        print("#######################")
        print("# Boson : Build uBoot #")
        print("#######################")
        sys.stdout.write("Building uboot [{}bit]... ".format(self.arch))
        sys.stdout.flush()
        cmd = ("docker exec -ti boson-pub " + \
               "bash /x/scripts/soc/raspberry_pi/build/uboot/" + \
               "build_{}bit.sh /x/u-boot-2018.09".format(self.arch))
        if self.verbose:
            subprocess.call(cmd, shell=True)
        else:
            subprocess.call(cmd, stdout=self.devnull, shell=True)
        print("Done")

    def get_binaries(self):
        cmd = ("bash `pwd`/../docker/scripts/soc/raspberry_pi/emmc/" + \
               "get_binaries.sh")
        if self.verbose:
            subprocess.call(cmd, stdout=self.devnull, shell=True)
        else:
            subprocess.call(cmd, shell=True)

    def format(self):
        cmd = ("bash `pwd`/../docker/scripts/soc/raspberry_pi/emmc/format.sh ")
        cmd += ("{}".format(self.drive))
        subprocess.call(cmd, shell=True)

    def run(self):
        self.start_bootstrap()
        self.build_uboot()
        self.get_binaries()
        #self.format()


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
        raspberrypi = RaspberryPi(args.drive, args.arch,
                                  args.image, args.verbose)
        raspberrypi.run()
    else:
        raspberrypi = RaspberryPi(args.drive, args.arch, args.image)
        raspberrypi.run()

if __name__ == ("__main__"):
    main()