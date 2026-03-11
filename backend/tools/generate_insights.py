import google.generativeai as genai

def generate_insights(eda_results, model_results):

    prompt = f"""
You are a professional data analyst.

Based on the dataset analysis below, generate a professional report.

Dataset Information:
Rows: {eda_results['rows']}
Columns: {eda_results['columns']}

Model Results:
{model_results}

Write the report with the following sections:

1. Executive Summary
2. Dataset Overview
3. Key Insights
4. Model Performance
5. Conclusion

Use clear professional language suitable for business reports.
"""

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)

    return response.text