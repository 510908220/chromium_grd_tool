#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
#---Server---
SERVER = "localhost"
PORT = "9898"

#---DataBase---
DB_NAME = "grd.dat"
test_files_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),os.pardir, os.pardir, os.pardir, "test_files")
xtb_path = os.path.join(test_files_dir, "generated_resources_zh-CN.xtb")

grd_path = os.path.join(test_files_dir, "generated_resources_yye.grdp")

if __name__ == "__main__":
	print (os.path.realpath(xtb_path))
