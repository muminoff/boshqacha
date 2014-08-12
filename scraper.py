#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2
import string
import re
import sqlite3

eng_alphabet = string.uppercase
eng_alphabet = re.sub('W', '', eng_alphabet)
eng_alphabet = re.sub('C', '', eng_alphabet)
uzb_alphabet = [letter for letter in eng_alphabet] + ["O\xe2\x80\x98", "G\xe2\x80\x98", "SH", "CH"]
urls = ["http://ism.uz/letters/" + letter for letter in uzb_alphabet]

def _execute(query):
    """Function to execute queries against a local sqlite database"""
    dbPath = 'database.db'
    connection = sqlite3.connect(dbPath)
    cursorobj = connection.cursor()
    try:
            cursorobj.execute(query)
            result = cursorobj.fetchall()
            connection.commit()
    except Exception:
            raise
    connection.close()
    return result


def get_men_names(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    names = soup.find_all('ol', class_='men-names')
    names_array = []
    for names_ in names:
        for name in names_.text.strip().split():
            if ',' in name:
                name = name.replace(',', '')
            print name
            #_execute("INSERT INTO `ismlar` (`firstname`,`sex`) VALUES (\"{0}\", \"{1}\");".format(name.encode('utf-8'), "male"))

    print "Done for %s" % url
    return


def get_women_names(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    names = soup.find_all('ol', class_='women-names')
    names_array = []
    for names_ in names:
        for name in names_.text.strip().split():
            if ',' in name:
                name = name.replace(',', '')
            print name
            #_execute("INSERT INTO `ismlar` (`firstname`,`sex`) VALUES (\"{0}\", \"{1}\");".format(name.encode('utf-8'), "female"))

    print "Done for %s" % url
    return

def main():

    for url in urls:
        get_men_names(url)
        get_women_names(url)



if __name__ == '__main__':
    main()
