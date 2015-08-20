#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import webbrowser
import subprocess
import ctypes
ctypes.windll.kernel32.SetConsoleTitleA("Grd Tools")
current_dir = os.path.dirname(__file__)
server = os.path.join(current_dir, "tools", "grd.py")
p1=subprocess.Popen(server, shell=True)
webbrowser.open("http://localhost:9898")
