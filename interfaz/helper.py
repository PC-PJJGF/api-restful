import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from usuarios.usuarios import UsuariosWindow
from productos.productos import ProductosWindow

class HelperView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Helper")
        self.setFixedSize(800, 600)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        buttons_layout.setSpacing(20)
        main_layout.addLayout(buttons_layout)

        users_button = QPushButton("Usuarios")
        users_button.setMinimumSize(200, 50)
        users_button.setStyleSheet("padding: 8px; background-color: #4CAF50; color: white;")
        users_button.clicked.connect(self.open_users)
        buttons_layout.addWidget(users_button)

        products_button = QPushButton("Productos")
        products_button.setMinimumSize(200, 50)
        products_button.setStyleSheet("padding: 8px; background-color: #4CAF50; color: white;")
        products_button.clicked.connect(self.open_products)
        buttons_layout.addWidget(products_button)

        self.users_window = None
        self.products_window = None

    def open_users(self):
        """Abrir ventana de usuarios sin que se cierre inmediatamente"""
        if self.users_window is None or not self.users_window.isVisible():
            self.users_window = UsuariosWindow()
            self.users_window.show()

    def open_products(self):
        """Abrir ventana de productos sin que se cierre inmediatamente"""
        if self.products_window is None or not self.products_window.isVisible():
            self.products_window = ProductosWindow()
            self.products_window.show()

# 🔹 Código para ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = HelperView()
    ventana.show()
    sys.exit(app.exec())
