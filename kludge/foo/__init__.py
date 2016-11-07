#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a module that uses the __init__.py file to define the entire click
group and add the subcommands to it.
"""

import click
import flan
import fuzz


@click.group()
def foo():
    """This docstring defines the foo subcommand of the Kluge CLI."""
    pass

"""Add the imported subcommands here."""
foo.add_command(flan.flan)
foo.add_command(fuzz.fuzz)
