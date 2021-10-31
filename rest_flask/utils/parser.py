"""
Module with argparser for run app
"""
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", help="Port", default=8080, type=int)
parser.add_argument(
    "-ho",
    "--host",
    help="Host",
    default="localhost" if sys.platform == "win32" else "0.0.0.0",
    type=str,
)
