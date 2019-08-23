#!/usr/bin/env python3
# coding: utf-8
"""
main.py.
08-23-19
jack skrable

command line program used to initiate a new python project
"""

import os
import sys
import string
import argparse
import datetime


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

source_path = '/'.join(os.path.realpath(__file__).split('/')[:-1])
project_path = os.path.abspath('./' + args.name)
date = datetime.datetime.now().strftime('%Y-%m-%d')

author = input('Author: ')
title = input('Title: ')
description = input('Description: ')

# print(source_path)
# print(project_path)
# print(date)
# print(os.path.join(source_path,args.language))

os.system('mkdir ' + project_path)
os.system(' '.join(['cp', os.path.join(source_path,args.language,'.'), project_path, '-r -a']))

with open(os.path.join(project_path, 'main.py'), 'r+') as f:
	contents = f.read()
	contents = contents.replace('[author]', author)
	contents = contents.replace('[title]', title)
	contents = contents.replace('[date]', date)
	contents = contents.replace('[description]', description)
	f.seek(0)
	f.write(contents)
	f.truncate()

