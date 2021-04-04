#!/usr/bin/env python3

from calculator import value_of

import click


@click.command()
@click.argument("number", type=int)
def fizzbuzz(number: int):
    click.echo(value_of(number))


if __name__ == "__main__":
    fizzbuzz()
