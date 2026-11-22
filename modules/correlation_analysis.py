# ============================================================
# CORRELATION ANALYSIS MODULE
# ============================================================

import os
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# CORRELATION INTERPRETATION
# ============================================================

def interpret_correlation(value):
    """
    Interpret the strength and direction
    of a correlation coefficient.
    """

    absolute_value = abs(value)

    if absolute_value == 1:
        strength = "Perfect"

    elif absolute_value >= 0.7:
        strength = "Strong"

    elif absolute_value >= 0.4:
        strength = "Moderate"

    elif absolute_value >= 0.2:
        strength = "Weak"

    else:
        strength = "Very Weak"

    if value > 0:
        direction = "Positive"

    elif value < 0:
        direction = "Negative"

    else:
        direction = "No"

    if value == 0:
        return "No Correlation"

    return f"{strength} {direction} Correlation"


# ============================================================
# CORRELATION ANALYSIS
# ============================================================

def analyze_correlation(dataset):

    # ----------------------------------------
    # Select Numerical Columns
    # ----------------------------------------

    numerical_data = dataset.select_dtypes(
        include="number"
    )

    # ----------------------------------------
    # Check Numerical Columns
    # ----------------------------------------

    if numerical_data.shape[1] < 2:

        return None

    # ----------------------------------------
    # Calculate Correlation Matrix
    # ----------------------------------------

    correlation_matrix = numerical_data.corr(
        method="pearson"
    )

    # ----------------------------------------
    # Create Results Dictionary
    # ----------------------------------------

    results = {}

    columns = correlation_matrix.columns

    for i in range(len(columns)):

        for j in range(i + 1, len(columns)):

            column_1 = columns[i]

            column_2 = columns[j]

            correlation_value = correlation_matrix.loc[
                column_1,
                column_2
            ]

            interpretation = interpret_correlation(
                correlation_value
            )

            results[
                f"{column_1} vs {column_2}"
            ] = {
                "Correlation": correlation_value,
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
    # Create Heatmap
    # ----------------------------------------

    plt.figure(
        figsize=(10, 7)
    )

    sns.heatmap(
        correlation_matrix,
        annot=True,
        fmt=".2f",
        linewidths=0.5,
        square=True
    )

    plt.title(
        "Correlation Matrix"
    )

    plt.tight_layout()

    # ----------------------------------------
    # Save Heatmap
    # ----------------------------------------

    file_path = (
        "visualizations/"
        "correlation_heatmap.png"
    )

    plt.savefig(
        file_path,
        dpi=300
    )

    # ----------------------------------------
    # Display Heatmap
    # ----------------------------------------

    plt.show()

    plt.close()

    return {
        "matrix": correlation_matrix,
        "relationships": results
    }