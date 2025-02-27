import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QPen

class UsuariosWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Usuarios")
        self.setFixedSize(800, 600)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        self.table = QTableView()
        main_layout.addWidget(self.table)

        self.load_users()

        self.add_user_button = QPushButton("Agregar usuario")
        main_layout.addWidget(self.add_user_button)

        self.add_user_button.clicked.connect(self.add_user)

    def load_users(self):
        database = Database()
        users = database.get_all_users()
        self.table.setModel(UserModel(users))

    def add_user(self):
        add_user_dialog = AddUserDialog()
        add_user_dialog.exec_()