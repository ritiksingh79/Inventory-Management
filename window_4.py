# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_3.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc

conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=LAPTOP-F8010458\SQLEXPRESS;DATABASE=warehouse;Trusted_connection=yes')

class Ui_InventoryStock(object):
    def setupUi(self, InventoryStock):
        InventoryStock.setObjectName("InventoryStock")
        InventoryStock.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(InventoryStock)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 391, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(13)
        self.tableWidget.setHorizontalHeaderLabels(["S_No", "Items", "Qty", "Price"])
        self.loaddata()
        '''item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)'''
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(20)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 70, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(16)
        font.setItalic(True)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 150, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(570, 160, 60, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(480, 270, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(570, 280, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 360, 101, 31))
        self.pushButton.setObjectName("pushButton")
        InventoryStock.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(InventoryStock)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        InventoryStock.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(InventoryStock)
        self.statusbar.setObjectName("statusbar")
        InventoryStock.setStatusBar(self.statusbar)

        self.retranslateUi(InventoryStock)
        QtCore.QMetaObject.connectSlotsByName(InventoryStock)

    def loaddata(self):
        cursor = conn.cursor()
        cursor.execute('select S_No, Items, Qty, Price from shop_items')
        tableindex = 0
        for row in cursor:
            self.tableWidget.setItem(tableindex, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tableindex, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tableindex, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(tableindex, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            tableindex += 1

    def retranslateUi(self, InventoryStock):
        _translate = QtCore.QCoreApplication.translate
        InventoryStock.setWindowTitle(_translate("InventoryStock", "Order Items"))
        '''item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("InventoryStock", "S_No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("InventoryStock", "Items"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("InventoryStock", "Qty"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("InventoryStock", "Price"))'''
        self.label.setText(_translate("InventoryStock", "Inventory in Stock"))
        self.label.adjustSize()
        self.label_2.setText(_translate("InventoryStock", "Place Order"))
        self.label_2.adjustSize()
        self.label_3.setText(_translate("InventoryStock", "S_No"))
        self.comboBox.setItemText(0, _translate("InventoryStock", "1"))
        self.comboBox.setItemText(1, _translate("InventoryStock", "2"))
        self.comboBox.setItemText(2, _translate("InventoryStock", "3"))
        self.comboBox.setItemText(3, _translate("InventoryStock", "4"))
        self.comboBox.setItemText(4, _translate("InventoryStock", "5"))
        self.comboBox.setItemText(5, _translate("InventoryStock", "6"))
        self.comboBox.setItemText(6, _translate("InventoryStock", "7"))
        self.comboBox.setItemText(7, _translate("InventoryStock", "8"))
        self.comboBox.setItemText(8, _translate("InventoryStock", "9"))
        self.comboBox.setItemText(9, _translate("InventoryStock", "10"))
        self.comboBox.setItemText(10, _translate("InventoryStock", "11"))
        self.comboBox.setItemText(11, _translate("InventoryStock", "12"))
        self.comboBox.setItemText(12, _translate("InventoryStock", "13"))
        self.label_5.setText(_translate("InventoryStock", "Qty"))
        self.pushButton.setText(_translate("InventoryStock", "Add to Cart"))
        self.pushButton.clicked.connect(self.AddToCart)

    def AddToCart(self):
        s_no = int(self.comboBox.currentText())
        item = ""
        amt = 0
        qty = int(self.lineEdit_2.text())
        cursor = conn.cursor()
        cursor.execute('select S_No, Items, Price from shop_items')
        for i in cursor:
            if i[0] == s_no:
                item = i[1]
                amt = i[2]
        cursor.execute('insert into cart(S_No, Items, Qty, Price, Total_Amount) values(?,?,?,?,?);',(s_no, item, qty, amt, qty*amt))
        conn.commit()
        self.x1 = self.lineEdit_2.clear()
        return self.x1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InventoryStock = QtWidgets.QMainWindow()
    ui = Ui_InventoryStock()
    ui.setupUi(InventoryStock)
    InventoryStock.show()
    sys.exit(app.exec_())
