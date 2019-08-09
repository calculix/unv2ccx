# -*- coding: utf-8 -*-


"""
    © Ihor Mirzov, August 2019
    Distributed under GNU General Public License v3.0

    Converts UNV file from Salome to CalculiX INP mesh: reads UNV_file,
    creates an internal FEM object, then writes the INP_file.

    Usage:
        python3 unv2ccx.py unv inp [-h]
    Positional arguments:
        unv         .unv file name
        inp         .inp file name
    Optional arguments:
        -h          show help message and exit
    Example:
        python3 unv2ccx.py ./tests-elements/116.unv ./tests-elements/116.inp
"""


import os, argparse, logging, shutil, INPWriter
from UNVParser import *


if __name__ == '__main__':

    # Clean cached files
    if os.path.isdir('__pycache__'):
        shutil.rmtree('__pycache__') # works in Linux as in Windows

    # Command line parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str,
                        help='.unv file name (with extension)',
                        default='')
    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(level = logging.INFO, format = '%(levelname)s: %(message)s')

    # Parse UNV file
    FEM = UNVParser(args.filename).parse()

    # Write INP file
    INPWriter.write(FEM, args.filename)

    logging.info(os.path.basename(args.filename) + ' done!\n')
