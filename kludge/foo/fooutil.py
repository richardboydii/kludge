#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This submodule of foo contains common methods used by other foo modules.
This pattern is designed to keep your code nice and DRY. Also names like 'util'
or 'common' are too overloaded, so the convention I tend to use is something
along the lines of modulenameutil or modulenamecommon. It's not as elegant as
it common or util, but it will keep things clear when looking at the code.
"""


def make_it_an_int(stringy_number):
    """Taks a string and returns and integer. Yes, this is rather nonsensical
    but its a teaching moment to show you how to centralize common logic
    across submodules in a module.
    """
    if stringy_number.isdigit():
        return int(stringy_number)
    else:
        raise SystemError("%s is not a number. C'mon dude." % stringy_number)
