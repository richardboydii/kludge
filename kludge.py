#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the root CLI that groups all the submodules together."""
import click

import kludge.bang as bang
import kludge.bar as bar
import kludge.foo as foo
"""The subocmmands are all located in the ./kludge directory. The __init__.py
file tells Python to look in a directory for Python files. 

The kludge.bang module is a single python file that defines the bang subcommand.

the kludge.bar module is a module with a child module that contains the bar
subcommand and its own subcommand, bat that has three subcommands

the kludge.foo module contains the foo subcommand which has two subcommands
broken into different files with a common fooutil module for shared functions.
"""


@click.group()
def cli():
    """This docstring will display help about the base CLI."""
    pass
    """As you can see, the main Click group is simply called CLI. In reality
    it's just a function that we define and add the pass line which will pass
    everything to our subcommands.
    """


cli.add_command(bang.bang)
cli.add_command(bar.bar)
cli.add_command(foo.foo)


if __name__ == "__main__":
    cli()
