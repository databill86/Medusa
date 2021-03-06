#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Common module
"""
import re

seps = r' [](){}+*|=-_~#/\\.,;:'  # list of tags/words separators
seps_no_groups = seps.replace('[](){}', '')
seps_no_fs = seps.replace('/', '').replace('\\', '')

title_seps = r'-+/\|'  # separators for title

dash = (r'-', r'['+re.escape(seps_no_fs)+']')  # abbreviation used by many rebulk objects.
alt_dash = (r'@', r'['+re.escape(seps_no_fs)+']')  # abbreviation used by many rebulk objects.
