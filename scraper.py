#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2
import string
import re

eng_alphabet = string.uppercase
eng_alphabet = re.sub('W', '', eng_alphabet)
eng_alphabet = re.sub('C', '', eng_alphabet)
uzb_alphabet = [letter for letter in eng_alphabet] + ["O\xe2\x80\x98", "G\xe2\x80\x98", "SH", "CH"]


def get_men_names(letter):
    page = urllib2.urlopen("http://ism.uz/letters/%s" % letter)
    soup = BeautifulSoup(page.read())
    names = soup.find_all('ol', class_='men-names')
    names_array = []
    for name in names:
        names_array.append(name.text.strip().split())

    return names_array[0]


def get_women_names(letter):
    page = urllib2.urlopen("http://ism.uz/letters/%s" % letter)
    soup = BeautifulSoup(page.read())
    names = soup.find_all('ol', class_='women-names')
    names_array = []
    for name in names:
        names_array.append(name.text.strip().split())

    return names_array[0]


def main():
    for letter in ['A']:
        print get_men_names(letter), len(get_men_names(letter))
        print get_women_names(letter), len(get_women_names(letter))



if __name__ == '__main__':
    main()
