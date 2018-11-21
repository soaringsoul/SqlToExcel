from PyQt5 import QtCore
from sqlalchemy import create_engine
import pandas as pd

class Sql_to_Csv(QtCore.QThread):
    _signal = QtCore.pyqtSignal(str)

    def __init__(self, ipAddress, username, passwd, database, sql_word, export_filepath):
        super(Sql_to_Csv, self).__init__()
        self.ipAddress = ipAddress
        self.username = username
        self.passwd = passwd
        self.database = database
        self.sql_word = sql_word
        self.export_filepath = export_filepath

    def sql_to_dataframe(self):
        self._signal.emit('开始读取sql数据到内存中!\n时间长度视数据表大小而定！\n耐心等待，不要关闭窗口！')
        print('开始读取sql数据到内存中！')
        # engine = 'mysql+pymysql://root:123456@%s:3306/%s?charset=utf8' % (self.ipAddress, self.database)
        engine_str = 'mysql+pymysql://%s:%s@%s:3306/%s?charset=utf8' \
                     % (self.username, self.passwd, self.ipAddress, self.database)
        engine = create_engine(engine_str, echo=False)
        try:
            df = pd.read_sql(self.sql_word, engine)
            df.fillna("", inplace=True)
        except:
            df = None
            self._signal.emit("mysql相关参数输入错误！请检查并更正后重新运行程序！")
        return df

    def sql_to_csv(self):
        self._signal.emit('导出数据到本地csv！')
        try:
            if self.export_filepath != '输入文件名(可选，不要带扩展名)':
                export_filepath = self.export_filepath
            else:
                export_filepath = 'sql_to_csv_result'
            df = self.sql_to_dataframe()
            df.to_csv(r'%s_for_ptyhon.csv' % export_filepath, encoding='utf8', index=False)
            df.to_csv(r'%s_for_excel.csv' % export_filepath, index=False)
            self._signal.emit("""
    导出成功！请到程序所在目录查看！
    导出两个csv文件到本程序文件所在目录!
    1.【%s_for_excel.csv】可以使用excel直接打开，但不能被python直接读取。
    2.【%s_for_python.csv】可以被python直接读取但不能被excel直接打开，会乱码！
    数据概览：
    %s   """ % (export_filepath, export_filepath, df))
        except Exception as e:
            self._signal.emit('出错了!请检查您的sql语句及其它设置！，具体错误如下：\n %s' % e)

    def run(self):
        self._signal.emit('开始从数据库存中查询数据！')
        self.sql_to_dataframe()
        self.sql_to_csv()
