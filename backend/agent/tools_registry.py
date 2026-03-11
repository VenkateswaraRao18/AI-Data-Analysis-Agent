def get_tools(agent):

    return {

        "eda": lambda path: agent.eda.run(path),

        "heatmap": lambda path: agent.viz.heatmap(path),
        "histogram": lambda path: agent.viz.histogram(path),
        "boxplot": lambda path: agent.viz.boxplot(path),
        "scatter": lambda path: agent.viz.scatter(path),

        "train_model": lambda path: agent.ml.run(path),
        # "generate_report": lambda path: agent.report.run(path)
        "generate_report": lambda path, eda, model,visualizations:
            agent.report.run(path, eda, model, visualizations)
    }