import subprocess
import argparse
import glob
import sys
import os


class BootStrap(object):

    def __init__(self, image, verbose=False):
        self.devnull = open(os.devnull, "w")
        self.verbose = verbose
        self.image = ("abehoffman/boson-pub:{}".format(image))
        self.image_name = (self.image.split("/")[-1].split(":")[0])
        self.init_feedback()

    def init_feedback(self):
        print("###########################")
        print("# Boson : Build Container #")
        print("###########################")

    def stop(self):
        sys.stdout.write("Stopping Container... ")
        sys.stdout.flush()
        cmd = ("docker stop {}".format(self.image_name))
        if self.verbose:
            subprocess.call(cmd, shell=True)
        else:
            subprocess.call(cmd, stdout=self.devnull, stderr=self.devnull,
                            shell=True)
        sys.stdout.write("Done")
        sys.stdout.flush()
        print("")

    def remove(self):
        sys.stdout.write("Removing Container... ")
        sys.stdout.flush()
        cmd = ("docker rm {}".format(self.image_name))
        if self.verbose:
            subprocess.call(cmd, shell=True)
        else:
            subprocess.call(cmd, stdout=self.devnull, stderr=self.devnull,
                            shell=True)
        sys.stdout.write("Done")
        sys.stdout.flush()
        print("")

    def build(self):
        sys.stdout.write("Building Container... ")
        sys.stdout.flush()
        cmd = ("docker build -t {} ../docker/.".format(self.image))
        if self.verbose:
            subprocess.call(cmd, shell=True)
        else:
            subprocess.call(cmd, stdout=self.devnull, stderr=self.devnull,
                            shell=True)
        sys.stdout.write("Done")
        sys.stdout.flush()
        print("")

    def push(self):
        sys.stdout.write("Pushing Container... ")
        sys.stdout.flush()
        cmd = ("docker push {}".format(self.image))
        if self.verbose:
            subprocess.call(cmd, shell=True)
        else:
            subprocess.call(cmd, stdout=self.devnull, stderr=self.devnull,
                            shell=True)
        sys.stdout.write("Done")
        sys.stdout.flush()
        print("")

    def start(self):
        sys.stdout.write("Starting Container... ")
        sys.stdout.flush()
        cmd = ("docker run -d --name {} {}".format(self.image_name,
                                                   self.image))
        if self.verbose:
            subprocess.call(cmd, shell=True)
        else:
            subprocess.call(cmd, stdout=self.devnull, stderr=self.devnull,
                            shell=True)
        sys.stdout.write("Done")
        sys.stdout.flush()
        print("")

    def clean(self):
        files_to_remove = glob.glob("./*.pyc")
        for aFile in files_to_remove:
            os.remove(aFile)

    def run(self):
        self.stop()
        self.remove()
        self.build()
        self.push()
        self.start()
        self.clean()


def main():
    parser = argparse.ArgumentParser()
    required = parser.add_argument_group('Required arguments')
    required.add_argument("-i", "--image", action="store",
                          help="Docker image version", required=True)
    required.add_argument("-v", "--verbose", action="store_true",
                          help="Show output (default False)")
    args = parser.parse_args()
    if args.verbose:
        bootstrap = BootStrap(args.image, args.verbose)
    else:
        bootstrap = BootStrap(args.image)
    bootstrap.run()

if __name__ == ("__main__"):
    main()