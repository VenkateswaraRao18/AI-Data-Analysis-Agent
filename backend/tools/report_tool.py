class ReportTool:

    def __init__(self, brain):
        self.brain = brain

    def run(self, dataset_path, eda_results, model_results,visualizations):

        best_model = model_results["best_model"]
        scores = model_results["results"]

        # ---- Prepare prompt for AI insights ----
        prompt = f"""
You are an expert data scientist preparing a professional analytical report.

Author: Venkateswararao Jannegorla
Project: AI Data Analysis Agent

Dataset Information
-------------------
Rows: {eda_results["rows"]}
Columns: {eda_results["columns"]}

EDA Summary Statistics
----------------------
{eda_results["summary"]}

Generated Visualizations
------------------------
{visualizations}

Machine Learning Results
------------------------
Model Scores: {scores}

Best Model: {best_model}

Instructions:
Write a clear professional report explaining the dataset and model results.

Follow this exact structure:

1. Executive Summary
Provide a short high-level explanation of the dataset and the modeling outcome.

2. Dataset Overview
Explain what the dataset represents and summarize key characteristics.

3. Feature Relationships
Explain important relationships between variables that may influence the target.

4. Data Distribution Insights
Discuss patterns observed in visualizations such as histograms, heatmaps, scatter plots, or boxplots.

5. Model Performance
Explain how the models performed and why the best model performed better.

6. Key Predictive Factors
Identify features that most likely influence the prediction target.

7. Conclusion
Provide a final summary of the findings and suggest possible improvements.

Important Rules:
- Use professional analytical language
- Do NOT repeat raw tables or logs
- Summarize insights instead of copying statistics
- Focus on meaningful interpretation of the data
"""
        insights = self.brain.llm.generate(prompt)

        # ---- Build final report ----
        report = f"""
# AI Data Analysis Report

Dataset: {dataset_path}

---

## AI Insights

{insights}

---

## Model Scores

{scores}

---

## Best Model

{best_model}

"""

        with open("reports/data_report.md", "w") as f:
            f.write(report)

        return "Report generated with AI insights"