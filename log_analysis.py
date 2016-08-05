#coding=utf-8
from datetime import datetime
from MsgLog import MsgLog, RequestLog, ReplyLog

# request_log = RequestLog('2016/06/14 16:58:10.533  [Recv Request] ChannelId = DMChannel1, SourceModule = ISAPI_CLIENT, Service = FR_QueryRawMaterialBySysKeyListRequest, ConnId = D104385C60')
# request_log.set_end_datetime('2016/06/14 16:58:10.583  [Sent Reply] ChannelId = DMChannel1, TargetModule = ISAPI_CLIENT, Service = FR_QueryRawMaterialBySysKeyListReply, ConnId = D104385C60')
# reply_log = ReplyLog('2016/06/14 16:58:10.583  [Sent Reply] ChannelId = DMChannel1, TargetModule = ISAPI_CLIENT, Service = FR_QueryRawMaterialBySysKeyListReply, ConnId = D104385C60')


def analysis_msg(path, date, target_filename_list):
	msg_log_list = []
	find = {}
	for target_filename in target_filename_list:
		#fpathname = 'C:\\Users\\kgs_chris\\Desktop\\工作\\issue Kita lag\\MSG\\msg20160614.log'
		fpathname = path + date + '\\' + target_filename + '.log'
		with open(fpathname, 'r', encoding='UTF-8') as f:
			for line in f.readlines():
				if 'Request' in line:
					curr_request = RequestLog(line)
					find[curr_request.conn_id] = curr_request

				if 'Reply' in line:
					curr_reply = ReplyLog(line)
					if curr_reply.conn_id in find:
						curr_request = find[curr_reply.conn_id]
						curr_request.set_end_datetime(line)

						msg_log_list.append(curr_request)
						del find[curr_reply.conn_id]

	#ofpath = 'C:\\Users\\kgs_chris\\Desktop\\工作\\issue Kita lag\\MSG\\reportmsg20160614\\'
	output_str = ''
	for log in msg_log_list:
		output_str += str(log)

	ofpath = path + 'report' + date + '.log'
	with open(ofpath, 'w', encoding='UTF-8') as f:
		f.write(output_str)
	print ('file output: ' + ofpath)
#analysis_msg('C:\\Users\\kgs_chris\\Desktop\\工作\\issue Kita lag\\MSG\\', 'msg20160614')