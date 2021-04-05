#!/usr/bin/env python3

import click

from fizzbuzz.calculator import value_of


@click.command()
@click.argument("number", type=int)
def fizzbuzz(number: int):
    click.echo(value_of(number))


if __name__ == "__main__":
    fizzbuzz()
