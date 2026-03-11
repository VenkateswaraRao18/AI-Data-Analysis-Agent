from agent.executor import DataAnalysisAgent

print("Starting Data Analysis Agent...")

agent = DataAnalysisAgent()

print("Agent initialized")

agent.analyze_dataset("dataset/winequality-red.csv")
# backend/dataset/winequality-red.csv

print("Analysis finished")