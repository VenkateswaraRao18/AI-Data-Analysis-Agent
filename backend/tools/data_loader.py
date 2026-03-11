import pandas as pd

class DataLoader:

    def load_csv(self, path):

        df = pd.read_csv(path)

        info = {
            "rows": df.shape[0],
            "columns": df.shape[1],
            "column_names": list(df.columns)
        }

        return df, info