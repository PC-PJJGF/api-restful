import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QPen

class ProductosWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Productos")
        self.setFixedSize(800, 600)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        self.table = QTableView()
        main_layout.addWidget(self.table)

        self.load_products()

        self.add_product_button = QPushButton("Agregar producto")
        main_layout.addWidget(self.add_product_button)

        self.add_product_button.clicked.connect(self.add_product)

    def load_products(self):
        database = Database()
        products = database.get_all_products()
        self.table.setModel(ProductModel(products))

    def add_product(self):
        add_product_dialog = AddProductDialog()
        add_product_dialog.exec_()