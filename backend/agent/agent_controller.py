class AgentController:

    def __init__(self, brain, tools, planner):

        self.brain = brain
        self.tools = tools
        self.planner = planner

        self.memory = {
            "eda": None,
            "model": None,
            "visualizations": []
        }

    def run(self, dataset_path):

        print("Creating analysis plan...\n")

        # Step 1: create plan
        plan = self.planner.create_plan(dataset_path)

        print("Agent Plan:", plan)

        print("\nExecuting plan...\n")

        report_generated = False

        for action in plan:

            if action not in self.tools:
                print("Unknown tool:", action)
                continue

            try:

                # REPORT TOOL NEEDS MEMORY INPUTS
                if action == "generate_report":

                    result = self.tools[action](
                        dataset_path,
                        self.memory["eda"],
                        self.memory["model"],
                        self.memory["visualizations"]
                    )

                    report_generated = True

                else:

                    result = self.tools[action](dataset_path)

            except Exception as e:

                print("Tool error:", e)
                break

            print(f"{action} → {result}")

            # ------------------------
            # Store results in memory
            # ------------------------

            if action == "eda":
                self.memory["eda"] = result

            elif action == "train_model":
                self.memory["model"] = result

            elif action in ["heatmap", "histogram", "boxplot", "scatter"]:
                self.memory["visualizations"].append(result)

        # ------------------------
        # Safety: ensure report runs
        # ------------------------

        if not report_generated:

            print("\nGenerating final report...\n")

            result = self.tools["generate_report"](
                dataset_path,
                self.memory["eda"],
                self.memory["model"],
                self.memory["visualizations"]
            )

            print("generate_report →", result)

        print("\nAgent finished analysis.")