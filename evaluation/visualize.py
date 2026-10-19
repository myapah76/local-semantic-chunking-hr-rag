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

    # 1. RQ1 Chart: Retrieval Metrics & Granularity Comparison (2 Subplots)
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

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), dpi=300, gridspec_kw={"width_ratios": [1.35, 1.0]})

    # Subplot 1: Retrieval Quality
    sns.barplot(data=metrics_df, x="Clean_Strategy", y="Score", hue="Metric", ax=ax1, palette="deep")
    ax1.set_title("(a) Retrieval Performance (Recall@K & MRR)", fontsize=13, weight="bold", pad=12)
    ax1.set_xlabel("Chunking Strategy", fontsize=11, labelpad=8)
    ax1.set_ylabel("Score (0.0 - 1.0)", fontsize=11)
    ax1.set_ylim(0, 1.15)
    for p in ax1.patches:
        val = p.get_height()
        if val > 0:
            ax1.annotate(f"{val:.2f}",
                        (p.get_x() + p.get_width() / 2., val),
                        ha='center', va='bottom', fontsize=8.5, xytext=(0, 2),
                        textcoords='offset points')

    # Subplot 2: Chunk Sizing & Granularity
    sns.barplot(data=df1, x="Clean_Strategy", y="Avg Chunk Chars", hue="Clean_Strategy", ax=ax2, palette="crest", legend=False)
    ax2.set_title("(b) Chunk Sizing: Avg Characters & Chunk Count", fontsize=13, weight="bold", pad=12)
    ax2.set_xlabel("Chunking Strategy", fontsize=11, labelpad=8)
    ax2.set_ylabel("Average Characters / Chunk", fontsize=11)
    max_chars = df1["Avg Chunk Chars"].max()
    ax2.set_ylim(0, max_chars * 1.25)
    for idx, p in enumerate(ax2.patches):
        chars = p.get_height()
        chunks = df1.iloc[idx]["Total Chunks"]
        if chars > 0:
            ax2.annotate(f"{chars:.1f} chars\n({chunks} chunks)",
                        (p.get_x() + p.get_width() / 2., chars),
                        ha='center', va='bottom', fontsize=9, weight="bold", xytext=(0, 4),
                        textcoords='offset points')

    fig.suptitle("RQ1: Overall Retrieval & Chunk Granularity Comparison Across 4 Strategies", fontsize=15, weight="bold", y=1.02)
    chart1_path = os.path.join(reports_dir, "rq1_retrieval_comparison.png")
    fig.savefig(chart1_path, bbox_inches="tight")
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

    # 3. CV-JD Matching Chart: Top-1 Match Similarity Across 4 Chunkers
    matching_csv = os.path.join(reports_dir, "results_cv_jd_matching_detailed.csv")
    if os.path.exists(matching_csv):
        df_match = pd.read_csv(matching_csv)
        # Filter for top-1 match per candidate and strategy
        top1_df = df_match[df_match["rank"] == 1].copy()

        fig, ax = plt.subplots(figsize=(14, 7), dpi=300)
        sns.barplot(
            data=top1_df, 
            x="candidate_name", 
            y="max_similarity", 
            hue="strategy_clean", 
            ax=ax, 
            palette="viridis"
        )
        ax.set_title("CV-to-JD Semantic Matching: Top-1 Similarity Score Across 4 Chunking Strategies", fontsize=14, weight="bold", pad=15)
        ax.set_xlabel("Candidate (CV)", fontsize=12, labelpad=10)
        ax.set_ylabel("Cosine Similarity (0.0 - 1.0)", fontsize=12)
        ax.set_ylim(0, 1.1)
        ax.tick_params(axis='x', rotation=18)

        # Add data labels
        for p in ax.patches:
            val = p.get_height()
            if val > 0:
                ax.annotate(f"{val:.2f}",
                            (p.get_x() + p.get_width() / 2., val),
                            ha='center', va='bottom', fontsize=8, xytext=(0, 2),
                            textcoords='offset points')

        chart3_path = os.path.join(reports_dir, "cv_jd_matching_comparison.png")
        fig.savefig(chart3_path)
        plt.close(fig)
        print(f"Generated CV-JD Matching chart: {chart3_path}")

if __name__ == "__main__":
    generate_evaluation_charts()
