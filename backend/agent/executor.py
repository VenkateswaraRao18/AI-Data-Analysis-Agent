from tools.data_loader import DataLoader
from tools.eda_tool import EDATool
from tools.visualization_tool import VisualizationTool
from tools.ml_tool import MLTool
from tools.report_tool import ReportTool
from tools.text_tool import TextTool

from agent.brain import AgentBrain
from agent.agent_controller import AgentController
from agent.tools_registry import get_tools
from agent.planner import AgentPlanner


class DataAnalysisAgent:

    def __init__(self):

        # -------------------------
        # Core AI Brain
        # -------------------------
        self.brain = AgentBrain()

        # -------------------------
        # Data Tools
        # -------------------------
        self.loader = DataLoader()
        self.eda = EDATool()
        self.viz = VisualizationTool()
        self.ml = MLTool()
        self.text_tool = TextTool()

        # -------------------------
        # Report Tool (needs LLM)
        # -------------------------
        self.report = ReportTool(self.brain)

        # -------------------------
        # Tool registry
        # -------------------------
        self.tools = get_tools(self)

        # -------------------------
        # Planner
        # -------------------------
        self.planner = AgentPlanner(self.brain.llm)

        # -------------------------
        # Controller
        # -------------------------
        self.controller = AgentController(
            self.brain,
            self.tools,
            self.planner
        )

    # --------------------------------
    # Detect text columns
    # --------------------------------
    def detect_text_columns(self, df):

        text_cols = []

        for col in df.columns:

            if df[col].dtype == "object":

                avg_length = df[col].astype(str).str.len().mean()

                if avg_length > 20:
                    text_cols.append(col)

        return text_cols

    # --------------------------------
    # Detect target column
    # --------------------------------
    def detect_target(self, df):

        return df.columns[-1]

    # --------------------------------
    # Main entry for agent
    # --------------------------------
    def analyze_dataset(self, dataset_path):

        print("Starting AI agent reasoning...\n")

        self.controller.run(dataset_path)