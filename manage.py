#!/usr/bin/env python
# -*- coding: utf-8 -*-

from atomicpress import app

# Theme
from themes.minimal import minimal

# Activate theme
app.activate_theme(minimal)

if __name__ == "__main__":
    app.run()
