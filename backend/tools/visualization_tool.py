import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("Agg")

# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import os


class VisualizationTool:

    def __init__(self):
        os.makedirs("reports", exist_ok=True)

    # ---------------------------
    # Correlation Heatmap
    # ---------------------------
    def heatmap(self, dataset_path):

        df = pd.read_csv(dataset_path)

        numeric_df = df.select_dtypes(include=["number"])

        plt.figure(figsize=(10,6))
        sns.heatmap(numeric_df.corr(), cmap="coolwarm")

        plt.savefig("reports/correlation_heatmap.png")
        plt.close()

        return "Heatmap generated"


    # ---------------------------
    # Histogram
    # ---------------------------
    def histogram(self, dataset_path):

        df = pd.read_csv(dataset_path)

        column = df.columns[-1]  # usually target column

        plt.figure(figsize=(8,5))

        sns.histplot(df[column], bins=20, kde=True)

        plt.savefig(f"reports/hist_{column}.png")
        plt.close()

        return f"Histogram generated for {column}"


    # ---------------------------
    # Boxplot
    # ---------------------------
    def boxplot(self, dataset_path):

        df = pd.read_csv(dataset_path)

        column = df.columns[-1]

        plt.figure(figsize=(8,5))

        sns.boxplot(x=df[column])

        plt.savefig(f"reports/box_{column}.png")
        plt.close()

        return f"Boxplot generated for {column}"


    # ---------------------------
    # Scatter Plot
    # ---------------------------
    def scatter(self, dataset_path):

        df = pd.read_csv(dataset_path)

        numeric = df.select_dtypes(include=["number"]).columns

        if len(numeric) < 2:
            return "Not enough numeric columns"

        x = numeric[0]
        y = numeric[-1]

        plt.figure(figsize=(8,5))

        sns.scatterplot(x=df[x], y=df[y])

        plt.savefig(f"reports/scatter_{x}_{y}.png")
        plt.close()

        return f"Scatter plot generated between {x} and {y}"