"""
包装qt的日志模块(qDebug的messagehandle重定向),供前台使用,主要有以下细节

* 日志输出目录
* 接口 qDebug
* 日志文件名格式
* 日志单条记录格式
* 日志级别
* 有新的日志时输出时触发信号
"""
import socket
from enum import Enum
from datetime import datetime

import os


class LoggingLevel(Enum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    CRITICAL = 3
    FATAL = 4


class YqLogger():
    def __init__(self, dir, appname):
        """

        :param dir: 日志写入目录
        :param appname: 日志文件名的组成,用来确定时哪个app的日志
        """
        self.dir = dir
        self.appname = appname

    def debug(self):
        pass

    def info(self):
        pass

    def warning(self):
        pass

    def critical(self):
        pass

    def fatal(self):
        pass

    def __get_log_filename(self):
        """
        refer: http://strftime.org/
        :return: processname.yyyymmdd-hhmmss.hostname.pid.log
        """

        log_filename = '{processname}.{time}.{hostname}.{pid}.log'.format(
            processname=self.appname,
            time=datetime.today().strftime('%Y%m%d-%H%M%S'),
            hostname=socket.gethostname(),
            pid=os.getpid()
        )

        log_filename = os.path.join(self.dir, log_filename)

        return log_filename

    def __save_to_log_file(self, msg):
        log_filename = self.__get_log_filename()

        # refer: https://stackoverflow.com/questions/16208206/confused-by-python-file-mode-w
        with open(log_filename, mode='a') as f:
            f.write(msg)

    def __format_logmsg(self, msg, log_level):
        """

        :param msg: yyyymmdd hh:mm:ss.Microsecond tid log-level source:line msg
        :return:
        """

