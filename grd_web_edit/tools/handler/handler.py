#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web as web
import tornado
import os
import tornado.template
from tornado.escape import json_encode
import conf
import add_handler
import history_handler
import modify_handler
import manual_handler
class IndexHandler(web.RequestHandler):
	"""主页"""
	def get(self):
		self.render("index.html")
	def post(self):
		pass


class Add(web.RequestHandler):
	def get(self):
		self.render("add.html")
	def post(self):
		message_string =  self.get_argument("message")
		translation_desc =  self.get_argument("translation")
		comment = self.get_argument("comment")

		add_h = add_handler.AddHandler()
		flag = add_h.add(message_string,comment,  translation_desc)

		ret_message = "%s" % ("add success!" if flag  else add_h.get_error_info())
		self.write(ret_message)
		
class Modify(web.RequestHandler):
	def get(self, ids):
		self.render("modify.html", message_name = ids)
	def post(self, arg):
		if arg == "search":
			message_name = self.get_argument("message_name")
			self.write(json_encode(modify_handler.search(message_name)))
		elif arg == "update":
			message_name = self.get_argument("message_name")
			translation_desc = self.get_argument("translation_desc")

			self.write(json_encode(modify_handler.update(message_name, translation_desc)))
		elif arg == "delete":
			message_name = self.get_argument("message_name")
			self.write(json_encode(modify_handler.delete(message_name)))

class History(web.RequestHandler):
	def get(self, *args, **kwargs):
		histories =  history_handler.get_historys()
		self.render("history.html", histories = histories)


class Tool(web.RequestHandler):
	def get(self):
		self.render("tool.html")
	def post(self):
		message_text = self.get_argument("message_text",None)
		translation_text = self.get_argument("translation_text",None)
		if message_text:
			id_ = manual_handler.get_message_id(message_text)
			self.write(id_)
		if translation_text:
			message_names =  manual_handler.get_message_names(translation_text)
			self.write("\n".join(message_names))

class Help(web.RequestHandler):
	def get(self, *args, **kwargs):
		self.render("help.html")