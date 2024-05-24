from PyQt5.QtWidgets import QWidget, QVBoxLayout
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class DataVisualizer:
    @staticmethod
    def add_histogram_tab(df, col, tab_widget):
        tab = QWidget()
        layout = QVBoxLayout()
        canvas = FigureCanvas(plt.Figure())
        layout.addWidget(canvas)
        tab.setLayout(layout)

        ax = canvas.figure.add_subplot(111)
        df[col].plot(kind='hist', ax=ax, title=f'Histogram of {col}')
        tab_widget.addTab(tab, f'Histogram: {col}')
