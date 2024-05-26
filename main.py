# main.py
import sys
from PyQt5.QtWidgets import QApplication
from controllers.data_controller import DataController
from models.file_handler import FileHandler
from views.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    model = FileHandler()
    main_window = MainWindow()
    controller = DataController(model, main_window)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
