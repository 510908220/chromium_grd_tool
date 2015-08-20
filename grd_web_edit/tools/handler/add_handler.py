__author__ = 'Administrator'
from lxml import etree
import xml_node
import util
import innerdb
import conf
class AddHandler(object):
	def __init__(self):
		self.error_info = ""
	def add(self,message_string, comment, translation_desc):
		try:
			root = etree.fromstring(message_string)
			tag = root.tag
			name = root.attrib['name']
			desc = root.attrib['desc']
			text = root.text
			comment = comment
		except Exception, ex:
			self.error_info = ex
			return False

		msg = xml_node.GrdMessage(name,desc, text, comment)
		grd = xml_node.Grd(conf.grd_path)
		flag = grd.add(msg)
		if flag:
			id_ = util.generate_message_id(text)
			xtb = xml_node.XTB(conf.xtb_path)
			flag = xtb.add(id_,translation_desc)
			if flag:
				grd.save()
				xtb.save()
				with innerdb.InnerDb() as db:
					db.write(name,{"id":id_,"translation_desc":translation_desc})
				return True
			else:
				self.error_info = xtb.error_info
				return False
		else:
			self.error_info = grd.error_info
			return False

	def get_error_info(self):
		return self.error_info

if __name__ == "__main__":
	root = etree.fromstring("<age/>")
	name = root.attrib['name']
	print root
