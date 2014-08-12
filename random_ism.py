from random import choice, sample, randrange
import json

def main():
    firstnames_file = open('firstnames.json', 'r')
    firstnames = json.load(firstnames_file)
    lastnames_file = open('lastnames.json', 'r')
    lastnames = json.load(lastnames_file)
    fathersname_file = open('fathersname.json', 'r')
    fathersnames = json.load(fathersname_file)

    for x in range(1, 10):
        fname = choice(firstnames)
        #lname = choice(lastnames)
        #fname2 = choice(fathersnames)
        #print fname['firstname'], lname['lastname'], fname2['fathersname']
        print fname['firstname']


if __name__ == '__main__':
    main()
