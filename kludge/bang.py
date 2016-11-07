#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a flat submodule for the CLI with one command. You'll notice that
it is registered directly with the top-level CLI using the @click.command()
notation."""

import click


@click.command()
@click.argument("number", required=1)
@click.option("--ending", "-e", required=0, 
              help=("Print an optional end string."))
def bang(number, ending):
    """Given a NUMBER, prints 'Bang! Bang!'"""
    if not ending:
        ending = ""
    if number.isdigit():
        for x in range(int(number)):
            print "Bang Bang! %s!" % ending
    else:
        raise SystemError("%s is not a number. That is sad." % number)
