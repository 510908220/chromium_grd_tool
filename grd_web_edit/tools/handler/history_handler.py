__author__ = 'Administrator'
import innerdb
def get_historys():
	records = None
	with innerdb.InnerDb() as db:
		records = db.read_all()
	return records
def delete_history(message_name):
	if message_name:
		with innerdb.InnerDb() as db:
			db.delete(str(message_name).strip())
