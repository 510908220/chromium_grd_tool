#!/usr/bin/env python
# -*- coding: utf-8 -*-

import conf
import shelve

class InnerDb(object):
	def __init__(self):
		super(InnerDb, self).__init__()

	def __enter__(self):
		self.sh = shelve.open(conf.DB_NAME, 'c')#获取一个shelve对象
		return self

	def __exit__(self, exc_type, exc_value, exc_tb):
		if self.sh:
			self.sh.close()

	def write(self, key, value):
		"""若key已存在，则覆盖"""
		self.sh[key] = value

	def delete(self, key):
		if self.sh:
			if key in self.read_all():
				del self.sh[key]

	def read(self, key):
		if self.sh:
			all_data = self.read_all()
			if key in all_data:
				return all_data[key]

	def read_all(self):
		all_data = {}
		if self.sh:
			for item in self.sh.items():
				all_data[item[0]] = item[1]
		return all_data

if __name__ == "__main__":
	with InnerDb() as db:
		db.write("username", "hzz1")
		db.write("password", "123456")

		print db.read("username1")
		print db.read_all()