# coding: utf-8


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


def is_even(number):
    return number % 2 == 0
