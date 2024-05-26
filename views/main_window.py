# views/main_window.py

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel, QAction, qApp,
    QTableWidget, QTableWidgetItem, QPushButton, QMessageBox
)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from views.data_visualizer import DataVisualizer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Viewfinder')
        self.setGeometry(100, 100, 1200, 800)
        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        exit_act = QAction(QIcon('exit.png'), '&Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('Exit application')
        exit_act.triggered.connect(qApp.quit)
        file_menu.addAction(exit_act)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.tab_widget = QTabWidget()
        layout.addWidget(self.tab_widget)

        self.drag_drop_area = QLabel("Drag and drop your CSV or Excel file here")
        self.drag_drop_area.setAlignment(Qt.AlignCenter)
        self.drag_drop_area.setStyleSheet("QLabel { border: 2px dashed #aaa; padding: 40px; }")
        self.drag_drop_area.setFont(QFont("Helvetica", 20))
        layout.addWidget(self.drag_drop_area)

        self.overview_tab = QWidget()
        self.overview_layout = QVBoxLayout()
        self.overview_table = QTableWidget()
        self.overview_layout.addWidget(self.overview_table)
        self.overview_tab.setLayout(self.overview_layout)

        self.statistics_tab = QWidget()
        self.statistics_layout = QVBoxLayout()
        self.statistics_table = QTableWidget()
        self.statistics_layout.addWidget(self.statistics_table)
        self.statistics_tab.setLayout(self.statistics_layout)

        self.visualization_tab = QWidget()
        self.visualization_layout = QVBoxLayout()
        self.visualization_tab.setLayout(self.visualization_layout)

        self.visualization_tabs = QTabWidget()
        self.visualization_layout.addWidget(self.visualization_tabs)

        self.export_tab = QWidget()
        self.export_layout = QVBoxLayout()
        self.export_button = QPushButton("Export Data Overview and Statistics")
        self.export_button.clicked.connect(self.export_data)
        self.export_button.setStyleSheet("QPushButton { padding: 10px; }")
        self.export_layout.addWidget(self.export_button)
        self.export_tab.setLayout(self.export_layout)

        self.tab_widget.addTab(self.overview_tab, "Overview")
        self.tab_widget.addTab(self.statistics_tab, "Statistics")
        self.tab_widget.addTab(self.visualization_tab, "Visualization")
        self.tab_widget.addTab(self.export_tab, "Export")

        self.setAcceptDrops(True)
        self.show()

    def set_controller(self, controller):
        self.controller = controller

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        file_path = files[0]
        self.drag_drop_area.setText(f'File dropped: {file_path}')
        self.controller.handle_file_dropped(file_path)

    def display_overview(self, df):
        self.overview_table.setRowCount(0)
        self.overview_table.setColumnCount(4)
        self.overview_table.setHorizontalHeaderLabels(['Column', 'Data Type', 'Missing Values', 'Sample Data'])

        for i, col in enumerate(df.columns):
            self.overview_table.insertRow(i)
            self.overview_table.setItem(i, 0, QTableWidgetItem(col))
            self.overview_table.setItem(i, 1, QTableWidgetItem(str(df[col].dtype)))
            self.overview_table.setItem(i, 2, QTableWidgetItem(str(df[col].isnull().sum())))
            self.overview_table.setItem(i, 3, QTableWidgetItem(str(df[col].iloc[0])))

    def display_statistics(self, df):
        self.statistics_table.setRowCount(0)
        numerical_df = df.select_dtypes(include=['number'])
        if not numerical_df.empty:
            stats = numerical_df.describe().T
            self.statistics_table.setRowCount(len(stats))
            self.statistics_table.setColumnCount(len(stats.columns) + 1)
            self.statistics_table.setHorizontalHeaderLabels(['Column'] + stats.columns.tolist())

            for i, (col, data) in enumerate(stats.iterrows()):
                self.statistics_table.setItem(i, 0, QTableWidgetItem(col))
                for j, val in enumerate(data):
                    self.statistics_table.setItem(i, j + 1, QTableWidgetItem(str(val)))

    def display_visualizations(self, df):
        self.visualization_tabs.clear()
        numerical_df = df.select_dtypes(include=['number'])
        for col in numerical_df.columns:
            DataVisualizer.add_histogram_tab(numerical_df, col, self.visualization_tabs)

    def export_data(self):
        self.controller.export_data(self.overview_table, self.statistics_table)

    def show_error_message(self, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText(message)
        msgBox.setWindowTitle("Error")
        msgBox.exec_()
