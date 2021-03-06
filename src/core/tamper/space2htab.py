#!/usr/bin/env python
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.
 
For more see the file 'readme/COPYING' for copying permission.
"""

from src.utils import settings

"""
About: Replaces space character ('%20') with horizontal tab ('%09')
Notes: This tamper script works against all targets.
"""

__tamper__ = "space2htab"

settings.TAMPER_SCRIPTS[__tamper__] = True
if settings.WHITESPACE[0] == "%20":
  settings.WHITESPACE[0] = "%09"
else:
  settings.WHITESPACE.append("%09") 

# eof 