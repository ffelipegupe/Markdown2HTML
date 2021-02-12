#!/usr/bin/python3
""" Markdown to HTML """

import sys
import os.path


if __name__ == "__main__":
    """ Function that takes an argument 2 strings """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)
    elif os.path.isfile(sys.argv[1]) is False:
                print("Missing {}\n".format(sys.argv[1]), file=sys.stderr)
                exit(1)
    else:
        exit(0)
