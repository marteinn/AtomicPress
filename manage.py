#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wordflask import app
from wordflask.app import manager

# Theme
from themes.minimal import minimal

# Start wordflask
app.start()

# Part of theme
app.activate_theme(minimal)


if __name__ == "__main__":
    manager.run()