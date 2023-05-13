from datetime import datetime


class LogUtilities:

	@staticmethod
	def log_msg(msg: str, file_name='./Logs/Logfile_'+str(datetime.now())[:10]+'.txt', writing_mode='a', level: str='info') -> None:
		"""
		:param level:
		:param msg:
		:param file_name:
		:param writing_mode:
		:return:
		"""

		try:
			with open(file_name, writing_mode) as f:
				text_to_written_in_log_file = str(datetime.now())[:22] + '   ' + level + '   ' + msg
				f.write('\n'+text_to_written_in_log_file)
				f.close()
		except:
			pass
