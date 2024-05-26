# controllers/data_controller.py
from PyQt5.QtWidgets import QFileDialog
from models.file_handler import FileHandler

class DataController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def load_file(self, file_path):
        try:
            df = self.model.load_file(file_path)
            self.view.display_overview(df)
            self.view.display_statistics(df)
            self.view.display_visualizations(df)
        except Exception as e:
            self.view.show_error_message(f"Failed to load file: {str(e)}")

    def handle_file_dropped(self, file_path):
        self.load_file(file_path)

    def export_data(self, overview_table, statistics_table):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(None, "Save Data Overview and Statistics", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        if file_path:
            self.model.export_data(file_path, overview_table, statistics_table)
