from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
import database
import encript


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(927, 686)
        Form.setMaximumSize(QtCore.QSize(927, 686))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(820, 380, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(820, 460, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(810, 540, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(810, 630, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(220, 30, 331, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(40, 110, 721, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(600, 470, 171, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(600, 550, 171, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(600, 640, 171, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Form, clicked=self.insert_values_passwords)
        self.pushButton.setGeometry(QtCore.QRect(370, 160, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form, clicked=self.update_values_from_treeview)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 160, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form, clicked=self.delete_value_from_treeview)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 160, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.treeWidget = QtWidgets.QTreeWidget(Form, clicked=self.insert_values_to_line_edit)
        self.treeWidget.setGeometry(QtCore.QRect(50, 260, 501, 401))
        self.treeWidget.setObjectName("treeWidget")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(600, 390, 171, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_4 = QtWidgets.QPushButton(Form, clicked=self.insert_values_to_treeview)
        self.pushButton_4.setGeometry(QtCore.QRect(740, 260, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form, clicked=self.search_value_from_line_edit)
        self.pushButton_5.setGeometry(QtCore.QRect(590, 260, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(580, 320, 281, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # function database
        database.create_table_passwords()






    def _create_items(self):
        values = database.show_all_values()
        num = 0
        number = len(values)
        while num < number:
            self.item = QtWidgets.QTreeWidgetItem(self.treeWidget)
            num += 1

    def _create_items_from_search(self, value):

        website = self.lineEdit_2.text()
        weak = self.lineEdit_3.text()
        note = self.lineEdit_4.text()
        password = self.lineEdit_5.text()
        if value == password:
            self.values = database.search_value(password=password)
        elif value == website:
            self.values = database.search_value(website=website)
        elif value == weak:
            self.values = database.search_value(weak=weak)
        elif value == note:
            self.values = database.search_value(note=note)

        num = 0
        number = len(self.values)
        while num < number:
            self.item2 = QtWidgets.QTreeWidgetItem(self.treeWidget)
            num += 1








    def insert_values_passwords(self):
        website = self.lineEdit_2.text()
        weak = self.lineEdit_3.text()
        note = self.lineEdit_4.text()
        password = self.lineEdit_5.text()
        database.insert_values(password, website,weak,note)
        self.insert_values_to_treeview()






    def delete_value_from_treeview(self):
        try:
            select = self.treeWidget.selectedItems()
            get = select[0]
            get_password = get.text(0)
            get_website = get.text(1)
            get_weak = get.text(2)
            get_note = get.text(3)
            database.delete_value(get_password,get_website,get_weak,get_note)
            self.insert_values_to_treeview()
        except:
            pass




    def insert_values_to_treeview(self):
        self.treeWidget.clear()
        self._create_items()
        values = database.show_all_values()
        num = 0
        number = len(values)


        while num < number:
            self.treeWidget.topLevelItem(num).setText(0, values[num]["password"])
            self.treeWidget.topLevelItem(num).setText(1, values[num]["website"])
            self.treeWidget.topLevelItem(num).setText(2, values[num]["weak"])
            self.treeWidget.topLevelItem(num).setText(3, values[num]["note"])
            num += 1

    def insert_values_to_treeview_from_search(self, value):
        website = self.lineEdit_2.text()
        weak = self.lineEdit_3.text()
        note = self.lineEdit_4.text()
        password = self.lineEdit_5.text()
        if value == password:
            self.values = database.search_value(password=password)
            self.treeWidget.clear()
            self._create_items_from_search(value)
        elif value == website:
            self.values = database.search_value(website=website)
            self.treeWidget.clear()
            self._create_items_from_search(value)
        elif value == weak:
            self.values = database.search_value(weak=weak)
            self.treeWidget.clear()
            self._create_items_from_search(value)
        elif value == note:
            self.values = database.search_value(note=note)
            self.treeWidget.clear()
            self._create_items_from_search(value)


        num = 0
        number = len(self.values)




        while num < number:
            if value == password:
                self.treeWidget.topLevelItem(num).setBackground(0, QColor(255, 255, 0))
            elif value == website:
                self.treeWidget.topLevelItem(num).setBackground(1, QColor(255, 255, 0))
            elif value == weak:
                self.treeWidget.topLevelItem(num).setBackground(2, QColor(255, 255, 0))
            elif value == note:
                self.treeWidget.topLevelItem(num).setBackground(3, QColor(255, 255, 0))
            self.treeWidget.topLevelItem(num).setText(0, self.values[num]["password"])
            self.treeWidget.topLevelItem(num).setText(1, self.values[num]["website"])
            self.treeWidget.topLevelItem(num).setText(2, self.values[num]["weak"])
            self.treeWidget.topLevelItem(num).setText(3, self.values[num]["note"])
            num += 1




    def update_values_from_treeview(self):
        try:
            select = self.treeWidget.selectedItems()
            get = select[0]
            website = self.lineEdit_2.text()
            weak = self.lineEdit_3.text()
            note = self.lineEdit_4.text()
            password = self.lineEdit_5.text()

            get_password = get.text(0)
            get_website = get.text(1)
            get_note = get.text(2)
            get_weak = get.text(3)


            database.update_value(password, website, weak, note, get_password, get_website, get_weak, get_note)



            self.insert_values_to_treeview()
        except Exception:
            pass


    def insert_values_to_line_edit(self):
        try:
            select = self.treeWidget.selectedItems()
            get = select[0]
            get_password = get.text(0)
            get_website = get.text(1)
            get_note = get.text(2)
            get_weak = get.text(3)
            self.lineEdit_5.setText(get_password)
            self.lineEdit_2.setText(get_website)
            self.lineEdit_3.setText(get_note)
            self.lineEdit_4.setText(get_weak)
        except:
            pass

    def search_value_from_line_edit(self):
        website = self.lineEdit_2.text()
        weak = self.lineEdit_3.text()
        note = self.lineEdit_4.text()
        password = self.lineEdit_5.text()

        if password:
            database.search_value(password)
            self.insert_values_to_treeview_from_search(password)
        elif website:
            database.search_value(website=website)
            self.insert_values_to_treeview_from_search(website)
        elif weak:
            database.search_value(weak=weak)
            self.insert_values_to_treeview_from_search(weak)
        elif note:
            database.search_value(note=note)
            self.insert_values_to_treeview_from_search(note)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "מנהל סיסמאות"))
        self.label.setText(_translate("Form", "סיסמה"))
        self.label_2.setText(_translate("Form", "אתר"))
        self.label_3.setText(_translate("Form", "חלש"))
        self.label_4.setText(_translate("Form", "הערה"))
        self.label_5.setText(_translate("Form", "מנהל סיסמאות"))
        self.pushButton.setText(_translate("Form", "הוסף"))
        self.pushButton_2.setText(_translate("Form", "ערוך"))
        self.pushButton_3.setText(_translate("Form", "מחק"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_4.setText(_translate("Form", "הראה הכל"))
        self.pushButton_5.setText(_translate("Form", "חפש"))
        self.treeWidget.headerItem().setText(0, "password")
        self.treeWidget.headerItem().setText(1, "website")
        self.treeWidget.headerItem().setText(2, "weak")
        self.treeWidget.headerItem().setText(3, "note")
        self.treeWidget.setColumnWidth(0,130)
        self.treeWidget.setColumnWidth(1, 130)
        self.treeWidget.setColumnWidth(2, 130)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
