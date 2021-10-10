#!/usr/bin/python

import os

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    "--input", "-i", type=str, help="Input .gif file filepath.", required=True
)
parser.add_argument(
    "--output", "-o", type=str, help="Output .mp4 file filepath.", required=True
)
args = parser.parse_args()

os.system(
    'ffmpeg -i {0} -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" {1}'.format(
        args.input, args.output
    )
)
