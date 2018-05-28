#!/usr/bin/env python

# -*- coding: utf-8 -*-

import random


def main(args):
    liczba = random.randint(1, 10)
    print("wylosowano:", liczba)
    odp = input("podaj liczbę od 1 do 10:")
    print("podałeś:", odp)

    if liczba == int(odp):
        print("zgadłeś")
    else:
        print("spróbuj ponownie")
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
