#!/usr/bin/env python

import argparse
import helloworld

def parse_command_line():
    " parses args for the helloworld.py funtions"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add args
    parser.add_argument(
        "--name",
        help="optional name to say hello to",
        type=str)

    parser.add_argument(
        "--aday",
        help="print a date to plan a hairstyle for you",
        type=int)

    parser.add_argument(
        "--temp",
        help="print the temperature to pick a food for you",
        type=int)

    # parse args
    args = parser.parse_args()
    return args


def main():
    "run helloworld on parsed args"
    args = parse_command_line()
    helloworld.helloworld(
        name=args.name,
        aday=args.aday,
        temp=args.temp)
