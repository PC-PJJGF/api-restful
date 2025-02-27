# from config import Config
import sys
from login.login import UsuariosWindow
from PySide6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)  # 🔹 Solucionando el error: Debe instanciarse primero
    ventana = UsuariosWindow()
    ventana.show()
    sys.exit(app.exec())  # 🔹 Corrección: PySide6 usa exec() en lugar de exec_()

if __name__ == "__main__":
    main()