from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel, QAction, qApp,
    QTableWidget, QTableWidgetItem, QPushButton, QFileDialog, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from file_handler import FileHandler
from data_visualizer import DataVisualizer

#the ui module hanldes the display of the different Pyqt5 components and renders the visualizations from data_visualizer into the screen.

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Viewfinder')
        self.setGeometry(100, 100, 1200, 800)
        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAct)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)

        self.tabWidget = QTabWidget()
        layout.addWidget(self.tabWidget)

        self.dragDropArea = QLabel("Drag and drop your CSV or Excel file here")
        self.dragDropArea.setAlignment(Qt.AlignCenter)
        self.dragDropArea.setStyleSheet("QLabel { border: 2px dashed #aaa; padding: 40px; }")
        self.dragDropArea.setFont(QFont("Helvetica", 20))
        layout.addWidget(self.dragDropArea)

        self.overviewTab = QWidget()
        self.overviewLayout = QVBoxLayout()
        self.overviewTable = QTableWidget()
        self.overviewLayout.addWidget(self.overviewTable)
        self.overviewTab.setLayout(self.overviewLayout)

        self.statisticsTab = QWidget()
        self.statisticsLayout = QVBoxLayout()
        self.statisticsTable = QTableWidget()
        self.statisticsLayout.addWidget(self.statisticsTable)
        self.statisticsTab.setLayout(self.statisticsLayout)

        self.visualizationTab = QWidget()
        self.visualizationLayout = QVBoxLayout()
        self.visualizationTab.setLayout(self.visualizationLayout)

        self.visualizationTabs = QTabWidget()
        self.visualizationLayout.addWidget(self.visualizationTabs)

        self.exportTab = QWidget()
        self.exportLayout = QVBoxLayout()
        self.exportButton = QPushButton("Export Data Overview and Statistics")
        self.exportButton.clicked.connect(self.exportData)
        self.exportButton.setStyleSheet("QPushButton { padding: 10px; }")
        self.exportLayout.addWidget(self.exportButton)
        self.exportTab.setLayout(self.exportLayout)

        self.tabWidget.addTab(self.overviewTab, "Overview")
        self.tabWidget.addTab(self.statisticsTab, "Statistics")
        self.tabWidget.addTab(self.visualizationTab, "Visualization")
        self.tabWidget.addTab(self.exportTab, "Export")

        self.setAcceptDrops(True)
        self.show()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        file_path = files[0]
        self.dragDropArea.setText(f'File dropped: {file_path}')
        self.loadFile(file_path)

    def loadFile(self, file_path):
        try:
            df = FileHandler.load_file(file_path)
            self.displayOverview(df)
            self.displayStatistics(df)
            self.displayVisualizations(df)
        except Exception as e:
            self.showErrorMessage(f"Failed to load file: {str(e)}")

    def displayOverview(self, df):
        self.overviewTable.setRowCount(0)
        self.overviewTable.setColumnCount(4)
        self.overviewTable.setHorizontalHeaderLabels(['Column', 'Data Type', 'Missing Values', 'Sample Data'])

        for i, col in enumerate(df.columns):
            self.overviewTable.insertRow(i)
            self.overviewTable.setItem(i, 0, QTableWidgetItem(col))
            self.overviewTable.setItem(i, 1, QTableWidgetItem(str(df[col].dtype)))
            self.overviewTable.setItem(i, 2, QTableWidgetItem(str(df[col].isnull().sum())))
            self.overviewTable.setItem(i, 3, QTableWidgetItem(str(df[col].iloc[0])))

    def displayStatistics(self, df):
        self.statisticsTable.setRowCount(0)
        numerical_df = df.select_dtypes(include=['number'])
        if not numerical_df.empty:
            stats = numerical_df.describe().T
            self.statisticsTable.setRowCount(len(stats))
            self.statisticsTable.setColumnCount(len(stats.columns) + 1)
            self.statisticsTable.setHorizontalHeaderLabels(['Column'] + stats.columns.tolist())

            for i, (col, data) in enumerate(stats.iterrows()):
                self.statisticsTable.setItem(i, 0, QTableWidgetItem(col))
                for j, val in enumerate(data):
                    self.statisticsTable.setItem(i, j + 1, QTableWidgetItem(str(val)))

    def displayVisualizations(self, df):
        self.visualizationTabs.clear()
        numerical_df = df.select_dtypes(include=['number'])
        for col in numerical_df.columns:
            DataVisualizer.add_histogram_tab(numerical_df, col, self.visualizationTabs)

    def exportData(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Data Overview and Statistics", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        if file_path:
            df_overview = pd.DataFrame({
                'Column': [self.overviewTable.item(row, 0).text() for row in range(self.overviewTable.rowCount())],
                'Data Type': [self.overviewTable.item(row, 1).text() for row in range(self.overviewTable.rowCount())],
                'Missing Values': [self.overviewTable.item(row, 2).text() for row in range(self.overviewTable.rowCount())],
                'Sample Data': [self.overviewTable.item(row, 3).text() for row in range(self.overviewTable.rowCount())]
            })

            df_statistics = pd.DataFrame({
                'Column': [self.statisticsTable.item(row, 0).text() for row in range(self.statisticsTable.rowCount())]
            })
            for col in range(1, self.statisticsTable.columnCount()):
                df_statistics[self.statisticsTable.horizontalHeaderItem(col).text()] = [self.statisticsTable.item(row, col).text() for row in range(self.statisticsTable.rowCount())]

            with pd.ExcelWriter(file_path) as writer:
                df_overview.to_excel(writer, sheet_name='Overview', index=False)
                df_statistics.to_excel(writer, sheet_name='Statistics', index=False)

    def showErrorMessage(self, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText(message)
        msgBox.setWindowTitle("Error")
        msgBox.exec_()
