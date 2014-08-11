#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2
import csv
import re

def get_names(letter):
    page = urllib2.urlopen('http://ism.uz/letters/' + letter)
    soup = BeautifulSoup(page.read())
    men_names = soup.find_all('ol', class_='men-names')
    names = []
    for men_name in men_names:
        names.append(men_name.text.strip().split())

    return names


def main():
    for a in get_names('B')[0]:
        print a



if __name__ == '__main__':
    main()
