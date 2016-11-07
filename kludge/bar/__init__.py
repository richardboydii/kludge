#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is module uses the __init__.py to define the subocommand and its child
subcommands.
"""

import click
import bat


@click.group()
def bar():
    """This docstring defines the bar subcommand of the Kluge CLI."""
    pass

"""Add the imported subcommands here."""
bar.add_command(bat.bat)
