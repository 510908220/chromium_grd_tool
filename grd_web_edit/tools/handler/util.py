#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'
__date__   = "2014/7/17 星期四 10:14:32"
import os
try:
	import hashlib
	_new_md5 = hashlib.md5
except ImportError:
	import md5
	_new_md5 = md5.new

def generate_message_id( message, meaning=''):
	"""根据grd中 message节点的text生成id信息"""
	def _UnsignedFingerPrintImpl(str, encoding='utf-8'):
		hex128 = _new_md5(str).hexdigest()
		int64 = long(hex128[:16], 16)
		return int64
	def UnsignedFingerPrint(str, encoding='utf-8'):
		return _UnsignedFingerPrintImpl(str, encoding)
	def FingerPrint(str, encoding='utf-8'):
		fp = UnsignedFingerPrint(str, encoding=encoding)
		  # interpret fingerprint as signed longs
		if fp & 0x8000000000000000L:
			fp = - ((~fp & 0xFFFFFFFFFFFFFFFFL) + 1)
		return fp

	fp = FingerPrint(message.strip())
	if meaning:
		# combine the fingerprints of message and meaning
		fp2 = FingerPrint(meaning)
		if fp < 0:
			fp = fp2 + (fp << 1) + 1
		else:
			fp = fp2 + (fp << 1)
	  	# To avoid negative ids we strip the high-order bit
	return str(fp & 0x7fffffffffffffffL)