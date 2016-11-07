#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a submodule of the bar module."""

import click


@click.group()
def bat():
    """This docstring defines the bat subcommand of the bar subcommand."""
    pass


@bat.command()
def aluminum():
    """The sound of an aluminum bat."""
    print "Plink!"


@bat.command()
def flying():
    """The sound of a flying bat."""
    print "Squee! Squee! Squee!"


@bat.command()
def wood():
    """The sound of a wooden bat."""
    print "Thwack!"
