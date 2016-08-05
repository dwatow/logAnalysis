import os, sys
from log_analysis import analysis_msg

#

path = "C:\\Users\\kgs_chris\\Desktop\\工作\\issue Kita lag\\MSG\\"
log_dirs = os.listdir( path + '\\')

target_dirs = []
for dirname in log_dirs:
	if dirname.find('2016') == 0:
		target_dirs.append(dirname)

# target_dirs.append('20160614')

for date in target_dirs:
	min_log_filename = 'msg' + date
	reprot_dirname = 'report' + min_log_filename


	#analysis_msg(path, min_log_filename)

	# print (path + date)
	dirs = os.listdir( path + date + '\\')
	file_list = []
	for index in range(1, len(dirs)+1):
		file_list.append('FablinkMsgLog_' + date + '_' + str(index))

	analysis_msg(path, date, file_list)