#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a subcommand of the foo subcommand of the Kluge CLI. It demonstrates
how to create a subcommand in the parent group.
"""

import click
import fooutil


@click.command()
@click.argument("number")
def fuzz(number):
    """Given a NUMBER implements a Fizz Buzz test."""
    num = fooutil.make_it_an_int(number)
    test_for_fizz_buzz(num)


def test_for_fizz_buzz(number):
    """I like to push logic out of the subcommand to funcitons in he file."""
    if (not number % 3) and (not number % 5):
        print "AWW YEAH FIZZ BUZZ!"
    elif not number % 5:
        print "Just plain ol' Fizz."
    elif not number % 3:
        print "That's a Buzz kill."
    else:
        print "No Fizz, no Buzz."

