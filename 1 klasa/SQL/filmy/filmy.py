#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []
    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter='\t')
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]
            dane.append(rekord)
    return dane


def main(args):
    dane_z_pliku('filmy.txt')
    exit()

    con = sqlite3.connect('filmy.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    # utworzenie tabeli w bazie
    with open('filmy.sql', 'r') as plik:
        cur.executescript(plik.read())


    filmy = dane_z_pliku('flimy.txt')
    filmy.pop(0)
    cur.executemany('INSERT INTO flimy VALUES(?, ?, ?, ?, ?)', filmy)

    con.commit()
    con.close()
    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
