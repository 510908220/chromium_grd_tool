#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'
import util
import conf
import xml_node
def get_message_id(message_text):
	return util.generate_message_id(message_text)

def get_message_names(translation_text):
	xtb = xml_node.XTB(conf.xtb_path)
	ids = xtb.get_translation_node_ids(translation_text)

	grd = xml_node.Grd(conf.grd_path)

	message_names = []
	for id_ in ids:
		message_name = grd.get_message_name(id_)
		if  message_name is not None:
			message_names.append(message_name)
	return message_names
