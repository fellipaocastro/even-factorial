#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import

from even_factorial import factorial, is_even


def main():
    try:
        number = int(raw_input('Entre com um número par inteiro: '))

        if not is_even(number):
            raise ValueError

        print 'factorial({0}) = {1}'.format(number, factorial(number))
    except ValueError:
        print 'Somente números pares inteiros são aceitos!'
        main()

if __name__ == '__main__':
    main()
