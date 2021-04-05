#!/usr/bin/env python3

import click

from fizzbuzz.calculator import value_of


@click.command()
@click.argument("number", type=int)
def fizzbuzz(number: int):
    """
    Bienvenido a FizzBuzz!\b
    Dado un número, si es divisible por 3,
    devolverá 'fizz'. Si es divisible por 5,
    devolverá 'buzz'. Si es divisble de 3 y 5,
    devolverá 'fizzbuzz'. En caso de no ser
    divisible de ningúno de los anteriores,
    devolverá el número dado.
    """
    click.echo(value_of(number))


if __name__ == "__main__":
    fizzbuzz()
