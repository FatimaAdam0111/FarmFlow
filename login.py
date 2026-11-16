import sys
from PyQt6 import QtWidgets, uic
from menu import MenuWindow
import pyodbc

Role = ['Admin', 'Manager', 'General User']
server =  r'localhost\SQLEXPRESS'
database = 'FarmFlow'  # Name of your Northwind database
use_windows_authentication = True  # Set to True to use Windows Authentication
username = 'sa'  # Specify a username if not using Windows Authentication
password = 'Fall2022.dbms'  # Specify a password if not using Windows Authentication


# Create the connection string based on the authentication method chosen
if use_windows_authentication:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
else:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
connection = pyodbc.connect(connection_string)

cursor = connection.cursor()




class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("LoginScreen.ui", self)

        # Populate combo box
        self.comboBox.addItems(Role)

        #hiding password
        self.passwordlineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        # Connect signals
        self.loginButton.clicked.connect(self.handle_login)

    def handle_login(self):
        username= self.usernamelineEdit.text().strip()
        password= self.passwordlineEdit.text()
        role= self.comboBox.currentText()
        select_query = "SELECT 1 FROM Users WHERE Username = ? AND Password = ? AND Role = ?"
        cursor.execute(select_query, (username, password, role))

        if cursor.fetchone():
            QtWidgets.QMessageBox.information(self, "Login successful", f"Welcome, {username}!")
            self.next_window = MenuWindow()
            self.next_window.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Login failed", "Invalid username, password or role.")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
