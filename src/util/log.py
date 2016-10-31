#coding=utf-8
'''
Created on 2016年10月12日

@author: dengdan
'''
import logging
import util.io
import sys


def init_logger(log_file = None, log_level = logging.DEBUG, mode = 'w'):
    """
    log_path: 日志文件的完整路径
    do_print: 是否打印到控制台
    mode: 'a', append; 'w', 覆盖原文件写入.
    """
    fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s'
    
    if log_file is None:
        log_file = '~/temp/log.log'
    # 此处不能使用logging输出
    print('log file path:' + log_file);
    util.io.make_parent_dir(log_file)
    logging.basicConfig(level = log_level,
                format= fmt,
                filename= util.io.get_absolute_path(log_file),
                filemode=mode)
        
    console = logging.StreamHandler(stream = sys.stdout)
    console.setLevel(log_level)
    formatter = logging.Formatter(fmt)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

