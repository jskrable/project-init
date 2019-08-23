#!/usr/bin/env python3
# coding: utf-8
"""
main.py
08-23-19
jack skrable

command line program used to initiate a new python project
"""

import os
import sys
import string
import argparse


def arg_parser():
    # function to parse arguments sent to CLI
    # setup argument parsing with description and -h method
    parser = argparse.ArgumentParser(
        description='Initializes a new project from the command line')
    parser.add_argument('-n', '--name', default='new-project', type=str, nargs='?',
                        help='name of the project to initialize')
    parser.add_argument('-l', '--language', default='python', type=str, nargs='?',
                        help='programming language to use')

    # parse args and return
    args = parser.parse_args()
    return args


# MAIN
#####################################################################
args = arg_parser()

git_ignore = '/home/jskrable/code/project-init/.gitignore'
project_path = os.path.abspath('./' + args.name)
dt = datetime.datetime.now()
date = '-'.join([dt.year,dt.month,dt.day])

os.system('mkdir ' + project_path)
os.system(' '.join('cp',git_ignore,project_path+'/.gitignore'))
