# from models.hf_model import HuggingFaceLLM
from models.gemini_model import GeminiLLM


class AgentBrain:

    def __init__(self):
        # self.llm = HuggingFaceLLM()
        self.llm = GeminiLLM()

    # General reasoning function for the agent loop
    def generate(self, prompt):
        return self.llm.generate(prompt)

    # Used at the end to create insights
    def generate_insights(self, dataset_info, eda_summary, model_results):

        prompt = f"""
You are a senior data scientist analyzing a dataset.

Dataset Information:
{dataset_info}

EDA Summary:
{eda_summary}

Model Results:
{model_results}

Write 3–5 clear insights about this dataset and model performance.

Focus on:
- Important patterns in the data
- What features may influence the target
- Why the best model performed better

Return ONLY bullet point insights.
Do NOT repeat the dataset summary.
Do NOT repeat the instructions.
"""

        response = self.llm.generate(prompt)

        return response