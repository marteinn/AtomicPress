#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wordflask import app

# Theme
from themes.minimal import minimal

# Part of theme
app.activate_theme(minimal)

if __name__ == "__main__":
    app.run()
