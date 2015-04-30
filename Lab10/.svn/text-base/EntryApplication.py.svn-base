import sys
import re

from PySide.QtGui import *

from EntryForm import *

class EntryApplication(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, parent=None):

        super(EntryApplication, self).__init__(parent)
        self.setupUi(self)
        self.btnClear.clicked.connect(lambda: self.clear())
        self.txtFirstName.textChanged.connect(lambda: self.enable())
        self.txtLastName.textChanged.connect(lambda: self.enable())
        self.txtAddress.textChanged.connect(lambda: self.enable())
        self.txtCity.textChanged.connect(lambda: self.enable())
        self.txtState.textChanged.connect(lambda: self.enable())
        self.txtZip.textChanged.connect(lambda: self.enable())
        self.txtEmail.textChanged.connect(lambda: self.enable())
        self.btnSave.clicked.connect(lambda: self.save())
        self.btnLoad.clicked.connect(lambda: self.loadData())
    def save(self):
        if(self.txtFirstName.text() == "" or self.txtLastName.text() == "" or self.txtAddress.text() == "" or self.txtCity.text() == "" or self.txtState.text() == "" or self.txtZip.text() == "" or self.txtEmail.text() == ""):
            self.lblError.setText("Populate All Fields")
            return

        if( self.txtState.text() not in self.states):
            self.lblError.setText("Enter Valid States")
            return

        if( len(self.txtZip.text()) != 5):
            print(len(self.txtState.text()))
            self.lblError.setText("Enter Valid ZIP")
            return

        if(re.match(r"\w+@\w+\.\w+", self.txtEmail.text() )== ""):
            self.lblError.setText("Enter Valid Email")
            return

        o = open("target.xml",'w', newline="\r\n")
        o.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
        o.write("\n<user>")
        o.write("\n      <FirstName>"+self.txtFirstName.text()+"</FirstName>")
        o.write("\n      <LastName>"+self.txtLastName.text()+"</LastName>")
        o.write("\n      <Address>"+self.txtAddress.text()+"</Address>")
        o.write("\n      <City>"+self.txtCity.text()+"</City>")
        o.write("\n      <State>"+self.txtState.text()+"</State>")
        o.write("\n      <ZIP>"+self.txtZip.text()+"</ZIP>")
        o.write("\n      <Email>"+self.txtEmail.text()+"</Email>")
        o.write("\n</user>")
        self.lblError.setText("")
        return

    def enable(self):
        self.btnSave.setEnabled(True);
        self.btnLoad.setEnabled(False);
    def clear(self):
        self.txtFirstName.clear();
        self.txtLastName.clear();
        self.txtAddress.clear();
        self.txtCity.clear();
        self.txtState.clear();
        self.txtZip.clear();
        self.txtEmail.clear();
        self.btnSave.setEnabled(False);
        self.btnLoad.setEnabled(True);

    def loadFromXmlFile(self, filePath):
        with open(filePath,"r") as f:
            lines = f.read()
        lines = lines.strip(" ")
        print(lines)
        firstname = re.findall(r"<FirstName>(.*?)</FirstName>",lines)
        self.txtFirstName.setText(str(firstname[0]))
        lastname = re.findall(r"<LastName>(.*?)</LastName>",lines)
        self.txtLastName.setText(str(lastname[0]))
        address = re.findall(r"<Address>(.*?)</Address>",lines)
        self.txtAddress.setText(str(firstname[0]))
        city = re.findall(r"<City>(.*?)</City>",lines)
        self.txtCity.setText(str(city[0]))
        state = re.findall(r"<State>(.*?)</State>",lines)
        self.txtState.setText(str(state[0]))
        firstname = re.findall(r"<ZIP>(.*?)</ZIP>",lines)
        self.txtZip.setText(str(firstname[0]))
        firstname = re.findall(r"<Email>(.*?)</Email>",lines)
        self.txtEmail.setText(str(firstname[0]))

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD, OR THE TEST WILL NOT PASS! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadFromXmlFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = EntryApplication()

    currentForm.show()
    currentApp.exec_()
