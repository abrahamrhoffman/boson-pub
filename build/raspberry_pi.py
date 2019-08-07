import subprocess
import argparse
import glob
import sys
import os

import bootstrap


class RaspberryPi(object):

    def __init__(self, arch, container, verbose=False):
        self.devnull = open(os.devnull, "w")
        self.uboot_version = ("u-boot-2018.09")
        self.build_folder = ("`pwd`/files")
        self.container = container
        self.verbose = verbose
        self.arch = arch

    def prepare_folder(self):
        cmd = ("rm -rf {} 2> /dev/null".format(self.build_folder))
        subprocess.call(cmd, shell=True)
        cmd = ("mkdir {} 2> /dev/null".format(self.build_folder))
        subprocess.call(cmd, shell=True)

    def start_bootstrap(self):
        btstrp = bootstrap.BootStrap(self.container)
        btstrp.run()
        print("")

    def build_uboot(self):
        print("#######################")
        print("# Boson : Build uBoot #")
        print("#######################")
        sys.stdout.write("Building uboot [{}bit]... ".format(self.arch))
        sys.stdout.flush()
        cmd = ("docker exec -ti boson-pub " + \
               "bash /x/scripts/soc/raspberry_pi/build/uboot/" + \
               "build_{}bit.sh /x/{}".format(self.arch, self.uboot_version))
        if self.verbose:
            subprocess.call(cmd, shell=True)
        else:
            subprocess.call(cmd, stdout=self.devnull, shell=True)
        print("Done")
        print("")

    def get_binaries(self):
        print("########################")
        print("# Boson : Gather Files #")
        print("########################")
        sys.stdout.write("Gathering files... ".format(self.arch))
        sys.stdout.flush()

        cmd = ("bash `pwd`/../docker/scripts/soc/raspberry_pi/emmc/" + \
               "get_binaries.sh {}".format(self.build_folder))
        if self.verbose:
            subprocess.call(cmd, stderr=self.devnull, shell=True)
        else:
            subprocess.call(cmd, shell=True)
        print("Done")
        print("")

    def get_build_files(self):
        binFiles = ["u-boot.bin"]
        for ele in binFiles:
            cmd = ("sudo docker cp boson-pub:/x/{}/{} {}"
                   .format(self.uboot_version, ele, self.build_folder))
            subprocess.call(cmd, shell=True)

    def get_config_files(self):
        configFiles = ["cmdline.txt", "config.txt"]
        for ele in configFiles:
            cmd = ("cp `pwd`/../docker/scripts/soc/raspberry_pi/build" + \
                   "/uboot/files/{} ".format(ele) + \
                   "{}".format(self.build_folder))
            subprocess.call(cmd, shell=True)

    def run(self):
        self.prepare_folder()
        self.start_bootstrap()
        self.build_uboot()
        self.get_binaries()
        self.get_build_files()
        self.get_config_files()


def main():
    parser = argparse.ArgumentParser()
    required = parser.add_argument_group('Required arguments')
    required.add_argument("-i", "--image", action="store",
                          help="Boson container version.  Ex: 1.0.5",
                          required=True)
    required.add_argument("-a", "--arch", action="store",
                          help="CPU architecture: 64 [or] 32",
                          required=True)
    required.add_argument("-v", "--verbose", action="store_true",
                          help="Display output (default False)")
    args = parser.parse_args()
    if args.verbose:
        raspberrypi = RaspberryPi(args.arch, args.image, args.verbose)
        raspberrypi.run()
    else:
        raspberrypi = RaspberryPi(args.arch, args.image)
        raspberrypi.run()

if __name__ == ("__main__"):
    main()