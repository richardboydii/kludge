#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a subcommand of the foo subcommand of the Kluge CLI. It uses a
function from the fooutil module and its own function in order to drive the
logic.
"""

import click
import fooutil


@click.command()
@click.argument("number")
@click.option("--flavor", "-f", required=0, 
              help=("Specify a special flavor for your Flan"))
def flan(number, flavor):
    """Make an order of a NUMBER of Flan."""
    num = fooutil.make_it_an_int(number)
    flan_flavor = check_flan_flavor(flavor)
    order_some_flan(num, flan_flavor)


def check_flan_flavor(flavor):
    """Determine what kind of flavor we want for our Flan."""
    if not flavor:
        flan_flavor = "plain old boring"
    else:
        flan_flavor = flavor
    return (flan_flavor + " flavored flan")


def order_some_flan(num, flan_flavor):
    """Order some Flan."""
    print "I want %s orders of %s NOW!" % (num, flan_flavor)

