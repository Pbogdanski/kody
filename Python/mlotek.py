#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    liczba = random.randint(1, 10)  # losowanie liczby <1;10>
    # print("Wylosowano:", liczba)
    # pobranie typu użytkownika
    for i in range(3):
        odp = input("Podaj liczbę od 1 do 10: ")
        print("Podałeś:", odp)

        if liczba == int(odp):  # porównanie odpowiedzi z wylosowaną liczbą
            print("Zgadłeś!")
            break  # przerwanie działania pętli 2xspacja # spacja - komentarz
        else:
            print("Spróbuj jeszcze raz!")

    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
