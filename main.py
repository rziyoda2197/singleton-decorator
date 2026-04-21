import pandas as pd
import numpy as np
import json
import os

class DashboardDataExporter:
    def __init__(self, data_path, export_path):
        self.data_path = data_path
        self.export_path = export_path

    def load_data(self):
        return pd.read_csv(self.data_path)

    def process_data(self, data):
        # Aggregation functions
        aggregation_functions = {
            'sum': np.sum,
            'avg': np.mean,
            'max': np.max,
            'min': np.min
        }

        # Group by columns
        group_by_columns = ['category', 'region']

        # Aggregate data
        aggregated_data = data.groupby(group_by_columns).agg(aggregation_functions)

        return aggregated_data

    def export_data(self, data):
        # Export data to JSON
        data.to_json(self.export_path, orient='records')

    def run(self):
        data = self.load_data()
        processed_data = self.process_data(data)
        self.export_data(processed_data)

if __name__ == '__main__':
    data_path = 'data.csv'
    export_path = 'export.json'
    exporter = DashboardDataExporter(data_path, export_path)
    exporter.run()
```

Kodni ishlatish uchun quyidagilar kerak:

1. `data.csv` faylini yaratib, unda ma'lumotlarni saqlab olish.
2. `export.json` faylini yaratib, unda ma'lumotlarni chiqarib olish.
3. `data.csv` faylini `DashboardDataExporter` klassiga berib, `run` metodi orqali ishlatish.
