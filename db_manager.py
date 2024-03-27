from colorama import Fore, Style

import sqlite3

cyan = Fore.CYAN
green = Fore.GREEN
red = Fore.RED
reset = Style.RESET_ALL

def get(dbfile, dbtable, attribute, row):
    try:
        print(f"{cyan}SQlite{reset}: Get row({green}{row}{reset}) from {green}{dbtable}{reset}")
        con = sqlite3.connect(dbfile)
        cur = con.cursor()

        cur.execute(f"SELECT * FROM {dbtable} ORDER BY name")
        rows = cur.fetchall()

        for item in rows:
            attribute.append(item[row].strip())

        return attribute

    except sqlite3.Error as error:
        print(f'{red}Error occurred ({dbtable}) - {reset}', error)


def update(dbfile, dbtable, item, attribute, row):
    try:
        print(f"{cyan}SQlite{reset}: update row({green}{row}{reset}), {attribute} = {item} from {green}{dbtable}{reset}")
        con = sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute(f"UPDATE {dbtable} SET name = ? WHERE rowid = ?", (attribute), row)
        #cur.execute(f"UPDATE {dbtable} SET {attribute} = {item} WHERE rowid = {row}")

        con.commit()
        con.close()
    except sqlite3.Error as error:
        print(f'{red}Error occurred ({dbtable}) - {reset}', error)

def delete(dbfile, dbtable, row):
    try:
        con = sqlite3.connect(dbfile)
        cur = con.cursor()

        cur.execute(f"DELETE from {dbtable} WHERE rowid = {row}")
        con.commit()
        con.close()

        print(f"{cyan}SQlite{reset}: Deleted row({green}{row}{reset}) from {green}{dbtable}{reset}")

    except sqlite3.Error as error:
        print(f'{red}Error occurred ({dbtable}) - {reset}', error)

def add_new(dbfile, dbtable, name, link):
    try:
        print(f"{cyan}SQlite{reset}: add new value ({name}, {link}) to {green}{dbtable}{reset}")
        con = sqlite3.connect(dbfile)
        cur = con.cursor()

        cur.execute(f"INSERT INTO {dbtable} VALUES ('{name}', '{link}')")

        con.commit()
        con.close()

    except sqlite3.Error as error:
        print(f'{red}Error occurred ({dbtable}) - {reset}', error)


def list_all(dbfile, dbtable):
    try:
        print(f"{cyan}SQlite{reset}: {green}{dbtable}{reset}")
        con = sqlite3.connect(dbfile)
        cur = con.cursor()

        cur.execute(f"SELECT rowid, * from {dbtable}")
        rows = cur.fetchall()

        for row in rows:
            print(row)

        con.close()
    except sqlite3.Error as error:
        print(f'{red}Error occurred ({dbtable}) - {reset}', error)