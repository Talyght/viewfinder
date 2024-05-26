# models/file_handler.py
import pandas as pd

class FileHandler:
    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        if file_path.endswith('.csv'):
            self.data = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            self.data = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format")
        return self.data

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

# I need to revamp the export_data function in order to make it save files as PDFs in a properly formatted document
# I'm not happy with it saving it as a CSV but it serves as a placeholder for the time being
    def export_data(self, file_path, overview_table, statistics_table):
        df_overview = pd.DataFrame({
            'Column': [overview_table.item(row, 0).text() for row in range(overview_table.rowCount())],
            'Data Type': [overview_table.item(row, 1).text() for row in range(overview_table.rowCount())],
            'Missing Values': [overview_table.item(row, 2).text() for row in range(overview_table.rowCount())],
            'Sample Data': [overview_table.item(row, 3).text() for row in range(overview_table.rowCount())]
        })

        df_statistics = pd.DataFrame({
            'Column': [statistics_table.item(row, 0).text() for row in range(statistics_table.rowCount())]
        })
        for col in range(1, statistics_table.columnCount()):
            df_statistics[statistics_table.horizontalHeaderItem(col).text()] = [statistics_table.item(row, col).text() for row in range(statistics_table.rowCount())]

        with pd.ExcelWriter(file_path) as writer:
            df_overview.to_excel(writer, sheet_name='Overview', index=False)
            df_statistics.to_excel(writer, sheet_name='Statistics', index=False)
