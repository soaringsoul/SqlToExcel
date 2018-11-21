from PyQt5 import QtCore, QtGui, QtWidgets
from utils.sql_to_csv import Sql_to_Csv
from utils.sql_to_excel import SqlToExcel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(914, 648)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        # MainWindow.setStyleSheet("""background-image: url();
        #         background-color: rgba(0, 255, 0, 50);""")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 30, 841, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.iPLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.iPLabel.setFont(font)
        self.iPLabel.setObjectName("iPLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.iPLabel)
        self.iPLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.iPLineEdit.setObjectName("iPLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.iPLineEdit)
        self.usernameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit)
        self.passwdLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.passwdLabel.setFont(font)
        self.passwdLabel.setObjectName("passwdLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.passwdLabel)
        self.passwdLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwdLineEdit.setObjectName("passwdLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwdLineEdit)
        self.databaseLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.databaseLabel.setFont(font)
        self.databaseLabel.setObjectName("databaseLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.databaseLabel)
        self.databaseLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.databaseLineEdit.setObjectName("databaseLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.databaseLineEdit)
        self.sql_wordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.sql_wordLabel.setFont(font)
        self.sql_wordLabel.setObjectName("sql_wordLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.sql_wordLabel)
        self.sql_wordLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.sql_wordLineEdit.setObjectName("sql_wordLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sql_wordLineEdit)
        self.Label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.Label.setFont(font)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.explort_filepath_LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.explort_filepath_LineEdit.setObjectName("explort_filepath_LineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.explort_filepath_LineEdit)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 210, 661, 41))

        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_csv = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_csv.setFont(font)
        self.pushButton_csv.setMouseTracking(True)
        self.pushButton_csv.setAcceptDrops(False)
        self.pushButton_csv.setObjectName("pushButton_csv")
        self.horizontalLayout.addWidget(self.pushButton_csv)
        self.pushButton_reset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.horizontalLayout.addWidget(self.pushButton_reset)
        self.pushButton_excel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_excel.setFont(font)
        self.pushButton_excel.setObjectName("pushButton_excel")
        self.horizontalLayout.addWidget(self.pushButton_excel)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 270, 841, 350))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("""background-image: url();
        background-color: rgba(255, 255, 0, 50);""")
        MainWindow.setCentralWidget(self.centralWidget)
        self.pushButton_reset.setStyleSheet("""background-image: url();
               background-color: rgba(0, 255, 0, 50);""")
        self.pushButton_csv.setStyleSheet("""background-image: url();
                       background-color: rgba(0, 255, 12, 50);""")
        self.pushButton_excel.setStyleSheet("""background-image: url();
                       background-color: rgba(0, 255, 1, 50);""")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "mysql导出工具_BY_夜雨微寒"))
        self.setWindowIcon(QtGui.QIcon(r'F:\my_PythonClass_to_exe\file.ico'))
        self.iPLabel.setText(_translate("MainWindow", "主机名或IP"))
        self.iPLineEdit.setText(_translate("MainWindow", "localhost"))
        self.usernameLabel.setText(_translate("MainWindow", "username"))
        self.usernameLineEdit.setText(_translate("MainWindow", "test"))
        self.passwdLabel.setText(_translate("MainWindow", "passwd"))
        self.passwdLineEdit.setText(_translate("MainWindow", "123456"))
        self.databaseLabel.setText(_translate("MainWindow", "database"))
        self.databaseLineEdit.setText(_translate("MainWindow", "crawl_data"))
        self.sql_wordLabel.setText(_translate("MainWindow", "sql_word"))
        self.sql_wordLineEdit.setText(_translate("MainWindow", r"sql查询语句，例如：SELECT * from china_village "))
        self.Label.setText(_translate("MainWindow", "文件名"))
        self.explort_filepath_LineEdit.setText(_translate("MainWindow", "输入文件名(可选，不要带扩展名)"))
        self.pushButton_csv.setText(_translate("MainWindow", "导出为CSV"))
        self.pushButton_reset.setText(_translate("MainWindow", "清空并重置"))
        self.pushButton_excel.setText(_translate("MainWindow", "导出为Excel"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_excel.clicked.connect(self.do_sql_to_excel)
        self.pushButton_csv.clicked.connect(self.do_sql_to_csv)
        self.pushButton_reset.clicked.connect(self._pushbutton_rest)
        show_str = \
            """
            说明：
                在sql_word里输入取数sql语句后，按需要选择导出为excel或者csv即可即可
            注意：
                python语句的限制，若在取数的sql语句中使用了'%'一定要用'%%'代替！
                python语句的限制，若在取数的sql语句中使用了'%'一定要用'%%'代替！
                python语句的限制，若在取数的sql语句中使用了'%'一定要用'%%'代替！

            """
        self.textBrowser.setText(show_str)

    def display_str(self, mystr):
        self.textBrowser.setText(mystr)

    def _pushbutton_rest(self):
        self.pushButton_excel.setEnabled(True)
        self.pushButton_csv.setEnabled(True)
        self.textBrowser.setText('已重置！请再次输入查询指令！')

    def do_sql_to_csv(self):
        try:
            self.baseinit()
            self.display_str('初始化完毕！')
            print('初始化完毕')
            self.SqlToCsv = Sql_to_Csv(self.ipAddress,
                                       self.username,
                                       self.passwd,
                                       self.database,
                                       self.sql_word,
                                       self.export_filepath)
            self.SqlToCsv._signal.connect(self.display_str)
            print("开始运行sql——to——csv")
            self.SqlToCsv.start()
            self.pushButton_csv.setEnabled(False)
        except Exception as e:
            self.textBrowser.setText("执行查询指令时出错！\n请检查输入的参数和指令是否正确！")
            self.textBrowser.append("具体错误如下：\n %s" % e)


    def do_sql_to_excel(self):
        try:
            self.baseinit()
            self.SqlToExcel = SqlToExcel(self.ipAddress,
                                         self.username,
                                         self.passwd,
                                         self.database,
                                         self.sql_word,
                                         self.export_filepath)
            self.SqlToExcel._signal.connect(self.display_str)
            self.SqlToExcel.start()
            self.pushButton_excel.setEnabled(False)
        except:
            self.display_str('参数错误，请检查后重新运行！')

    def baseinit(self):
        self.ipAddress = self.iPLineEdit.text().strip()
        print(self.ipAddress)
        self.username = self.usernameLineEdit.text().strip()
        print(self.username)
        self.passwd = self.passwdLineEdit.text().strip()
        self.database = self.databaseLineEdit.text().strip()
        self.sql_word = self.sql_wordLineEdit.text().strip()
        print(self.sql_word)
        self.export_filepath = self.explort_filepath_LineEdit.text().strip()
        print('初始化数据完毕')
