from datetime import datetime

class MsgLog:
    def _log_to_datetime(self, txt_str_log):
        date = txt_str_log[:10]
        time = txt_str_log[11:23]
        year, month, day = date.split('/')
        hour, minute, second = time.split(':')
        second, ms = second.split('.')
        return datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), int(ms)*1000)
    def _init_message_id(self, txt_str_log):
        str_message_begin = txt_str_log.find('Service = ') + len('Service = ')
        str_message_end = txt_str_log.find(self.message_type, txt_str_log.find(self.message_type)+1) + len(self.message_type)
        return txt_str_log[str_message_begin:str_message_end]
    def _init_conn_id(self, txt_str_log):
        return txt_str_log[txt_str_log.find('ConnId = ') + len('ConnId = '):len(txt_str_log)-1]


class RequestLog(MsgLog):
    def __init__(self, txt_str_log):
        self.message_type = 'Request'
        self.message_id = self._init_message_id(txt_str_log)
        self.conn_id = self._init_conn_id(txt_str_log)
        self.begin_datetime = self._log_to_datetime(txt_str_log)
        self.delta_sec = 0.0

    def set_end_datetime(self, txt_str_log):
        self.end_datetime = self._log_to_datetime(txt_str_log)
        #print (self.begin_datetime)
        #print (self.end_datetime)

        self.delta_sec = (self.end_datetime - self.begin_datetime).total_seconds()
        #print (self.delta_sec)


    def __str__(self):
    	return str(self.begin_datetime) + "\t" + str(self.conn_id) + "\t" + self.message_id + "\t" + str(self.delta_sec) + "\tsec" + '\n'

class ReplyLog(MsgLog):
    def __init__(self, txt_str_log):
        self.message_type = 'Reply'
        self.message_id = self._init_message_id(txt_str_log)
        self.conn_id = self._init_conn_id(txt_str_log)
        self.end_datetime = self._log_to_datetime(txt_str_log)
        #self.delta_sec = 0.0

    def __str__(self):
    	return self.conn_id + "\t" + self.message_id