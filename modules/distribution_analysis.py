# ============================================================
# DISTRIBUTION ANALYSIS MODULE
# ============================================================

import os
import matplotlib.pyplot as plt


# ============================================================
# DISTRIBUTION INTERPRETATION
# ============================================================

def interpret_skewness(skewness):

    if skewness > 1:
        return "Highly Positively Skewed"

    elif 0.5 < skewness <= 1:
        return "Moderately Positively Skewed"

    elif -0.5 <= skewness <= 0.5:
        return "Approximately Symmetric"

    elif -1 <= skewness < -0.5:
        return "Moderately Negatively Skewed"

    else:
        return "Highly Negatively Skewed"


# ============================================================
# DISTRIBUTION ANALYSIS
# ============================================================

def analyze_distribution(dataset):

    numerical_data = dataset.select_dtypes(
        include="number"
    )

    if numerical_data.empty:
        return None

    results = {}

    for column in numerical_data.columns:

        # ----------------------------------------
        # Statistical Values
        # ----------------------------------------

        mean = numerical_data[column].mean()

        median = numerical_data[column].median()

        skewness = numerical_data[column].skew()

        kurtosis = numerical_data[column].kurt()

        interpretation = interpret_skewness(
            skewness
        )

        # ----------------------------------------
        # Store Results
        # ----------------------------------------

        results[column] = {
            "Mean": mean,
            "Median": median,
            "Skewness": skewness,
            "Kurtosis": kurtosis,
            "Interpretation": interpretation
        }

        # ----------------------------------------
        # Create Visualization Folder
        # ----------------------------------------

        os.makedirs(
            "visualizations",
            exist_ok=True
        )

        # ----------------------------------------
        # Create Histogram
        # ----------------------------------------

        plt.figure(figsize=(9, 5))

        plt.hist(
            numerical_data[column].dropna(),
            bins=10,
            edgecolor="black"
        )

        # ----------------------------------------
        # Mean Line
        # ----------------------------------------

        plt.axvline(
            mean,
            linestyle="--",
            linewidth=2,
            label=f"Mean = {mean:.2f}"
        )

        # ----------------------------------------
        # Median Line
        # ----------------------------------------

        plt.axvline(
            median,
            linestyle=":",
            linewidth=2,
            label=f"Median = {median:.2f}"
        )

        # ----------------------------------------
        # Chart Labels
        # ----------------------------------------

        plt.title(
            f"Distribution of {column}"
        )

        plt.xlabel(column)

        plt.ylabel("Frequency")

        plt.legend()

        plt.tight_layout()

        # ----------------------------------------
        # Save Chart
        # ----------------------------------------

        safe_column_name = (
            str(column)
            .replace(" ", "_")
            .replace("/", "_")
            .replace("\\", "_")
        )

        file_path = (
            f"visualizations/"
            f"{safe_column_name}_distribution.png"
        )

        plt.savefig(
            file_path,
            dpi=300
        )

        # ----------------------------------------
        # Display Chart
        # ----------------------------------------

        plt.show()

        plt.close()

    return results