import sqlite3
import json


def main():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # fathersname
    cur.execute('select * from fathersname')
    fathersname_recs = cur.fetchall()
    fathersname_rows = [dict(rec) for rec in fathersname_recs]
    fathersname_rows_json = json.dumps(fathersname_rows, indent=4)
    f = open('fathersname.json', 'w')
    f.write(fathersname_rows_json)
    f.close()
    print 'Done.'
    # firstname
    cur.execute('select * from firstnames')
    firstname_recs = cur.fetchall()
    firstname_rows = [dict(rec) for rec in firstname_recs]
    firstname_rows_json = json.dumps(firstname_rows, indent=4)
    f = open('firstnames.json', 'w')
    f.write(firstname_rows_json)
    f.close()
    print 'Done..'
    # lastname
    cur.execute('select * from lastnames')
    lastname_recs = cur.fetchall()
    lastname_rows = [dict(rec) for rec in lastname_recs]
    lastname_rows_json = json.dumps(lastname_rows, indent=4)
    f = open('lastnames.json', 'w')
    f.write(lastname_rows_json)
    f.close()
    print 'Done...'


if __name__ == '__main__':
    main()
