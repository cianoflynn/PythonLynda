#!/usr/local/bin/python3
# regex.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

import re

def main():

    fh = open('raven.txt')
    for line in fh:
        if re.search('(Len|Neverm)ore', line):
            print(line, end='')
    print()

    # after running loop above, must re-assign fh. Why?
    # Does python automatically close file when iterator reaches the end?
    fh = open('raven.txt')
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(match.group())
    print()

    fh = open('raven.txt')
    for line in fh:
        match = re.search('(Len|Neverm|neverm)ore', line)
        if match:
            print(match.group())
    print()

    fh = open('raven.txt')
    for line in fh:
        # print every line
        # substitute, i.e. search and replace
        print(re.sub('(Len|Neverm|neverm)ore', 'Al Gore', line), end='')
    print()

if __name__ == "__main__": main()
