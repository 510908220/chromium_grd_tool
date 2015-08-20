#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
import os
import util
class GrdMessage(object):
	"""grd message结构"""
	def __init__(self, name, desc, text, comment):
		self.name = name
		self.desc = desc
		self.text = text
		self.comment = comment
class Grd(object):
	"""generated_resources_yye.grdp文件操作"""
	def __init__(self, path):
		super(Grd, self).__init__()
		self.path = path
		self.error_info = ""
		self.parser = None
		self.tree = None
		self.root = None
		try:
			self._init()
		except Exception,ex:
			self.error_info = ex

	def _init(self):
		self.parser = etree.XMLParser(remove_comments=False, remove_blank_text=True)
		self.tree = etree.parse(self.path, parser=self.parser)
		self.root = self.tree.getroot()

	def _is_equal(self, node_message, data_message):
		if node_message.tag == "message":
			attributes = node_message.attrib

			if attributes["name"]:
				if attributes["name"].strip() == data_message.name.strip():
					self.error_info = "name:%s has exists！\n" % data_message.name
					return True
			if node_message.text:
				if node_message.text.strip() == data_message.text.strip():
					self.error_info = "text:%s has exists！\n" % data_message.text
					return True
		return False

	def _is_message_exist(self, node_messages,data_message):
		for message in node_messages.iter("message"):
			if self._is_equal(message, data_message):
				return True
		return False

	def get_node_messages(self):
		return self.root

	def add_message_into_grd(self, node_messages, data_message):
		"""
			node_messages:grd中message节点
			data_message :待添加message节点内容

		"""

		if not self._is_message_exist(node_messages, data_message):
			node_message = etree.Element("message")
			node_message.set('name', data_message.name)
			node_message.set('desc', data_message.desc)
			node_message.text = data_message.text
			node_message.append(etree.Comment(data_message.comment))
			node_messages.append(node_message)
			return True
		return False

	def add(self, msg):
		node_messages = self.get_node_messages()
		if node_messages is not None:
			flag =  self.add_message_into_grd(node_messages, msg)
			if flag:
				return True
			else:
				self.error_info = "the message node has been exists!"
				return False
		else:
			self.error_info = "root is invalid!! may be %s not exists!" % self.path
			return False

	def get_message_node(self,name):
		node_messages = self.get_node_messages()
		if node_messages is not None:
			for message in node_messages.iter("message"):
				if name.strip() == message.attrib['name'].strip():
					return message


	def get_message_name(self,id_):
		node_messages = self.get_node_messages()
		if node_messages is not None:
			for message in node_messages.iter("message"):
				if message.text  is not None:
					translation_id = util.generate_message_id(message.text)
					if translation_id.strip() == id_.strip():
						return message.attrib['name'].strip()

	def get_message_node_string(self,name):
		message = self.get_message_node(name)
		if message is not None:
			return etree.tostring(message, pretty_print=True, encoding="utf-8"), message.text

	def remove(self, name):
		node_messages = self.get_node_messages()
		if node_messages is not None:
			message_node = self.get_message_node(name)
			if message_node is not None:
				message_node.getparent().remove(message_node)
				return True
			else:
				self.error_info = "message_node:%d not exists!" % name
				return False
		else:
			self.error_info = "root is invalid!! may be %s not exists!" % self.path
			return False

	def update(self, msg):
		node_messages = self.get_node_messages()
		if node_messages is not None:
			message_node = self.get_message_node(msg.name)
			if message_node is not None:#name, desc, text, comment
				message_node.desc = msg.desc
				message_node.comment = msg.comment
				return True
			else:
				self.error_info = "message_node:%d not exists!" % msg.name
				return False
		else:
			self.error_info = "root is invalid!! may be %s not exists!" % self.path
			return False

	def save(self):
		self.tree.write(self.path, pretty_print=True, xml_declaration=True, encoding='utf-8')

class XTB(object):
	"""generated_resources_zh-CN.xtb文件操作"""
	def __init__(self, path):
		super(XTB, self).__init__()
		self.path = path
		self.error_info = ""
		self.parser = None
		self.tree = None
		self.root = None
		try:
			self._init()
		except Exception, ex:
			self.error_info = ex

	def _init(self):
		self.parser = etree.XMLParser(remove_comments=False, remove_blank_text=True)
		self.tree = etree.parse(self.path, parser=self.parser)
		self.root = self.tree.getroot()

	def get_node_translations(self):
		return self.root

	def add(self, id, text):
		node_translation = etree.Element("translation")
		node_translation.set('id', id)
		node_translation.text = text

		node_translations = self.get_node_translations()
		if node_translations is not None:
			node_translations.append(node_translation)
			return True
		else:
			self.error_info = "root is invalid!! may be %s not exists!" % self.path
			return False

	def get_translation_node(self, id_):
		for translation in self.root.iter("translation"):
			if translation.attrib["id"].strip() == id_.strip():
				return translation
	def get_translation_node_ids(self,translation_text):
		ids = []
		print translation_text
		for translation in self.root.iter("translation"):
			if translation is not None:
				if translation.text is not None:
					if translation.text.strip() == translation_text.strip():
						ids.append(translation.attrib["id"])
		return ids

	def delete(self, id_):
		node_translations = self.get_node_translations()
		if node_translations is not None:
			translation_node = self.get_translation_node(id_)
			if translation_node is not None:
				translation_node.getparent().remove(translation_node)
				return True
			else:
				self.error_info = "translation_node %s is not exists" % id_
				return False
		else:
			self.error_info = "root is invalid!! may be %s not exists!" % self.path
			return False

	def get_chongfu(self):
		ids = {}
		repeats = []
		for translation in self.root.iter("translation"):
			if translation.attrib["id"].strip():
				if not ids.has_key(translation.attrib["id"].strip()):
					ids[translation.attrib["id"].strip()] = 0
				ids[translation.attrib["id"].strip()] += 1

		for key in ids:
			if ids[key] > 1:
				repeats.append(key)

		return repeats

	def update(self, id_, text):
		node_translations = self.get_node_translations()
		if node_translations is not None:
			translation_node = self.get_translation_node(id_)
			if translation_node is not None:
				translation_node.text = text
				return True
			else:
				self.error_info = "translation_node %s is not exists" % id_
				return False
		else:
			self.error_info = "root is invalid!! may be %s not exists!" % self.path
			return False

	def save(self):
		self.tree.write(self.path, pretty_print=True, xml_declaration=True, encoding='utf-8')
