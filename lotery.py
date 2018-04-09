# -*- coding: utf-8 -*-
import random

def generator_loto_stevil(dolzina):
    lista_stevil = []
    while True:
        if len(lista_stevil) == dolzina:
            break
        loto_stevilo = random.randint(1, 50)

        if loto_stevilo not in lista_stevil:
            lista_stevil.append(loto_stevilo)

    return lista_stevil

def main():
    print "Dobrodošli v generatorju loto števil."
    vprasanje = int(raw_input('Vnesite koliko naključnih loto števil bi imeli:'))
    print(generator_loto_stevil(vprasanje))

if __name__ == "__main__":
    main()
    print "END"