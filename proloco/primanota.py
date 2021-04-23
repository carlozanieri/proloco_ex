import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from Connect import Connect

class App(QWidget):

    def __init__(self, datada, dataa):
        super().__init__()
        self.title = 'Prima Nota '
        self.datada = datada
        self.dataa = dataa
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 600
        self.initUI()
        print(datada)
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()


    def createTable(self):
        # Create table
        primanota = Connect.tab_primanota( self,self.datada, self.dataa)
        ##primanota = Connect.primanota('', self.datada, self.dataa)
        x=Connect.conta('', self.datada, self.dataa)
        print(self.datada)
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(x)
        self.tableWidget.setColumnCount(6)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Descrizione"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Data"))

        self.tableWidget.setItem(0, 2, QTableWidgetItem("Cassa Entrate"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("Cassa Uuscite"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("Banca Entrate"))
        self.tableWidget.setItem(0, 5, QTableWidgetItem("Banca Uscite"))
        y=1

        for a in primanota:
            self.tableWidget.setItem(y, 0, QTableWidgetItem(a[2]))
            self.tableWidget.setItem(y, 1, QTableWidgetItem(str(a[1])))

            self.tableWidget.setItem(y, 2, QTableWidgetItem(str(a[3]) + " €"))
            self.tableWidget.setItem(y, 3, QTableWidgetItem(str(a[4]) + " €"))
            self.tableWidget.setItem(y, 4, QTableWidgetItem(str(a[5]) + " €"))
            self.tableWidget.setItem(y, 5, QTableWidgetItem(str(a[6]) + " €"))
            y=y+1
        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 