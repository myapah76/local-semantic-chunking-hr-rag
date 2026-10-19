import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_evaluation_charts():
    reports_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "reports"))
    rq1_path = os.path.join(reports_dir, "results_rq1.csv")
    rq2_path = os.path.join(reports_dir, "results_rq2.csv")

    if not os.path.exists(rq1_path) or not os.path.exists(rq2_path):
        print("CSV reports not found. Run benchmark_runner.py first.")
        return

    sns.set_theme(style="whitegrid", palette="muted")
    plt.rcParams.update({"font.size": 11, "figure.autolayout": True})

    # 1. RQ1 Chart: Retrieval Metrics Comparison
    df1 = pd.read_csv(rq1_path)
    # Simplify strategy names for plotting
    df1["Clean_Strategy"] = df1["Strategy"].apply(lambda s: s.split("(")[0])

    metrics_df = pd.melt(
        df1,
        id_vars=["Clean_Strategy"],
        value_vars=["Recall@3", "Recall@5", "MRR"],
        var_name="Metric",
        value_name="Score"
    )

    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    sns.barplot(data=metrics_df, x="Clean_Strategy", y="Score", hue="Metric", ax=ax, palette="deep")
    ax.set_title("RQ1: Retrieval Performance Comparison Across Chunking Strategies", fontsize=14, weight="bold", pad=15)
    ax.set_xlabel("Chunking Strategy", fontsize=12, labelpad=10)
    ax.set_ylabel("Score (0.0 - 1.0)", fontsize=12)
    ax.set_ylim(0, 1.1)

    # Add data labels
    for p in ax.patches:
        val = p.get_height()
        if val > 0:
            ax.annotate(f"{val:.2f}",
                        (p.get_x() + p.get_width() / 2., val),
                        ha='center', va='bottom', fontsize=9, xytext=(0, 3),
                        textcoords='offset points')

    chart1_path = os.path.join(reports_dir, "rq1_retrieval_comparison.png")
    fig.savefig(chart1_path)
    plt.close(fig)
    print(f"Generated RQ1 chart: {chart1_path}")

    # 2. RQ2 Chart: Subtype Breakdown (CV vs JD vs Policy)
    df2 = pd.read_csv(rq2_path)
    df2["Clean_Strategy"] = df2["Strategy"].apply(lambda s: s.split("(")[0])

    fig, ax = plt.subplots(figsize=(12, 6), dpi=300)
    sns.barplot(data=df2, x="Doc Type", y="MRR", hue="Clean_Strategy", ax=ax, palette="Set2")
    ax.set_title("RQ2: MRR Performance Disaggregated by HR Document Subtype", fontsize=14, weight="bold", pad=15)
    ax.set_xlabel("HR Document Subtype", fontsize=12, labelpad=10)
    ax.set_ylabel("Mean Reciprocal Rank (MRR)", fontsize=12)
    ax.set_ylim(0, 1.15)

    for p in ax.patches:
        val = p.get_height()
        if val > 0:
            ax.annotate(f"{val:.2f}",
                        (p.get_x() + p.get_width() / 2., val),
                        ha='center', va='bottom', fontsize=8, xytext=(0, 3),
                        textcoords='offset points')

    chart2_path = os.path.join(reports_dir, "rq2_subtype_mrr_comparison.png")
    fig.savefig(chart2_path)
    plt.close(fig)
    print(f"Generated RQ2 chart: {chart2_path}")

if __name__ == "__main__":
    generate_evaluation_charts()
