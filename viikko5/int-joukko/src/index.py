import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    joukko.lisaa_joukkoon(1)
    joukko.lisaa_joukkoon(2)
    joukko.lisaa_joukkoon(3)
    joukko.lisaa_joukkoon(2)

    print(joukko.to_int_list())


if __name__ == "__main__":
    main()
