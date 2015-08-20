#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
import os


class RepeatXxtb(object):
	"""generated_resources_zh-CN.xtb文件操作"""
	def __init__(self, path):
		super(RepeatXxtb, self).__init__()
		self.path = path
		self.error_info = ""
		self.parser = None
		self.tree = None
		self.root = None
		try:
			self._init()
		except Exception, ex:
			self.error_info = ex
			print ex

	def _init(self):
		self.parser = etree.XMLParser(remove_comments=False, remove_blank_text=True)
		self.tree = etree.parse(self.path, parser=self.parser)
		self.root = self.tree.getroot()

	def get_node_translations(self):
		return self.root


	def get_translation_node(self, id_):
		for translation in self.root.iter("translation"):
			if translation.attrib["id"].strip() == id_.strip():
				return translation

	def delete(self, id_):
		node_translations = self.get_node_translations()
		if node_translations is not None:
			translation_node = self.get_translation_node(id_)
			if translation_node is not None:
				self.root.remove(translation_node)
				return True
			else:
				self.error_info = "translation_node %s is not exists" % id_
				return False
		else:
			self.error_info = "root is invalid!! may be %s not exists!" % self.path
			return False



	def save(self):
		self.tree.write(self.path, pretty_print=True, xml_declaration=True, encoding='utf-8')

path = r"C:\Users\Administrator\Desktop\generated_resources_zh-CN.xtb"

xtb = XTB(path)
chongfus = xtb.get_chongfu()
print len(chongfus)
"""
for i in chongfus:
	xtb.delete(i)
xtb.save()
"""