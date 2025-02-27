import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QPushButton, QDialog, QLineEdit, QLabel
import sqlite3



class UsuariosWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Iniciar Sesión")
        self.setFixedSize(300, 200)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        self.email_field = QLineEdit()
        main_layout.addWidget(self.email_field)
        self.email_field.setPlaceholderText("Email")
        self.email_field.setStyleSheet("padding: 8px; font-size: 12pt;")

        self.password_field = QLineEdit()
        main_layout.addWidget(self.password_field)
        self.password_field.setPlaceholderText("Contraseña")
        self.password_field.setEchoMode(QLineEdit.Password)
        self.password_field.setStyleSheet("padding: 8px; font-size: 12pt;")

        self.add_user_button = QPushButton("Iniciar Sesión")
        main_layout.addWidget(self.add_user_button)
        self.add_user_button.setStyleSheet("padding: 8px; background-color: #4CAF50; color: white;")

        self.add_user_button.clicked.connect(self.login)

    def login(self):
        """Comprueba las credenciales del usuario."""
        email = self.email_field.text()
        password = self.password_field.text()
        # Conectar a la base de datos (se creará si no existe)
        conn = sqlite3.connect('..\database.db')
        cursor = conn.cursor()
        if email and password:
            # Comprueba las credenciales en la base de datos
            if cursor.execute("SELECT * FROM usuarios WHERE email = ? AND password = ?", (email, password)).fetchone():
                print("Inicio de sesión exitoso")
            else:
                error = QDialog()
                error.setWindowTitle("Error")
                error.setFixedSize(200, 100)
                error_layout = QVBoxLayout()
                error.setLayout(error_layout)
                error_layout.addWidget(QLabel("Credenciales inválidas"))
                error.exec_()
        else:
            error = QDialog()
            error.setWindowTitle("Error")
            error.setFixedSize(200, 100)
            error_layout = QVBoxLayout()
            error.setLayout(error_layout)
            error_layout.addWidget(QLabel("Por favor, complete todos los campos"))
            error.exec_()
