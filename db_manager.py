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