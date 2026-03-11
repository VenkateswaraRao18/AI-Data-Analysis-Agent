class AgentPlanner:

    def __init__(self, llm):
        self.llm = llm

    def create_plan(self, dataset_path):

        prompt = f"""
You are an AI data scientist.

Create a short analysis plan for a dataset.

Dataset path:
{dataset_path}

Available tools:

- eda
- heatmap
- histogram
- boxplot
- scatter
- train_model
- generate_report

Rules:

1. Start with EDA
2. Generate 2–3 visualizations maximum
3. Train model
4. Generate report

Return ONLY the tool sequence.

Example:

eda
histogram
heatmap
train_model
generate_report
"""

        response = self.llm.generate(prompt)

        # convert response to list
        plan = []

        for line in response.split("\n"):

            line = line.strip()

            if line in [
                "eda",
                "heatmap",
                "histogram",
                "boxplot",
                "scatter",
                "train_model",
                "generate_report"
            ]:
                plan.append(line)

        return plan