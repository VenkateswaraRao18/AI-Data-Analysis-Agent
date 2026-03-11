import pandas as pd


class EDATool:

    def run(self, dataset_path):

        df = pd.read_csv(dataset_path)

        summary = df.describe(include="all")

        result = {
            "rows": df.shape[0],
            "columns": df.shape[1],
            "summary": summary
        }

        print("EDA Completed")

        return result