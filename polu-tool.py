import os
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument("ip")
args = argparser.parse_args()

url = "{}/wordpress".format(args.ip)

os.system("wpscan --url {}".format(url))
