#!/usr/bin/env python
# -*- coding: utf-8 -*-

#encoding:utf-8
__author__ = 'Administrator'
import xml_node
import conf
import util
import history_handler
import innerdb
def get_message_info(message_name):
	"""
		return:
			message_string
			message_text
	"""
	grd = xml_node.Grd(conf.grd_path)
	message_info = grd.get_message_node_string(message_name)
	return message_info
def get_translation_text(id_):
	xtb = xml_node.XTB(conf.xtb_path)
	translation_node = xtb.get_translation_node(id_)
	if translation_node is not None:
		return translation_node.text

def search(message_name):
	message_info = get_message_info(message_name)
	if message_info is not None:
		id_ = util.generate_message_id(message_info[1].strip())
		print id_
		translation_text = get_translation_text(id_)
		print "translation_text:", translation_text, type(translation_text)
		message_str = message_info[0]
		if translation_text is not None:
			return {"translation_text":translation_text.encode("utf-8"),"message_str":message_str}
		else:
			return {"message_str":message_str}
	return {}

def delete(message_name):
	message_info = get_message_info(message_name)
	ret_info = {"ret":'false', "info":"no such message node"}
	if message_info is not None:
		id_ = util.generate_message_id(message_info[1])
		grd = xml_node.Grd(conf.grd_path)

		message_flag = grd.remove(message_name)
		xtb = xml_node.XTB(conf.xtb_path)
		xtb_flag = xtb.delete(id_)

		if message_flag and xtb_flag:#删除成功才保存使生效
			grd.save()
			xtb.save()
			ret_info["ret"] = 'true'
			ret_info["info"] = ""
			history_handler.delete_history(message_name)
		else:
			ret_info["ret"] = 'false'
			ret_info["info"] = grd.error_info + "/" + xtb.error_info
	return ret_info

def update(message_name, translation_desc):
	message_info = get_message_info(message_name)
	ret_info = {"ret":'false', "info":"update faile"}
	if message_info is not None:
		id_ = util.generate_message_id(message_info[1])

		xtb = xml_node.XTB(conf.xtb_path)
		xtb_flag = xtb.update(id_, translation_desc)
		if xtb_flag:
			xtb.save()
			ret_info["ret"] = "true"
			ret_info["info"] = ""

			with innerdb.InnerDb() as db:
				db.write(str(message_name),{"id":id_,"translation_desc":translation_desc})
		else:
			ret_info["ret"] = "false"
			ret_info["info"] = xtb.error_info
	return ret_info



