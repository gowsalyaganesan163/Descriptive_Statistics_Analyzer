# ============================================================
# STATISTICAL SUMMARY REPORT MODULE
# ============================================================

import os


# ============================================================
# GENERATE STATISTICAL SUMMARY
# ============================================================

def generate_summary_report(dataset):
    """
    Generate a complete descriptive statistical
    summary for all numerical columns.
    """

    numerical_data = dataset.select_dtypes(
        include="number"
    )

    if numerical_data.empty:
        return None

    report = {}

    for column in numerical_data.columns:

        data = numerical_data[column].dropna()

        # ----------------------------------------
        # Central Tendency
        # ----------------------------------------

        mean = data.mean()
        median = data.median()

        mode_values = data.mode()

        if not mode_values.empty:
            mode = mode_values.iloc[0]
        else:
            mode = None

        # ----------------------------------------
        # Dispersion
        # ----------------------------------------

        minimum = data.min()
        maximum = data.max()

        range_value = maximum - minimum

        variance = data.var()

        standard_deviation = data.std()

        # ----------------------------------------
        # Quartiles
        # ----------------------------------------

        q1 = data.quantile(0.25)
        q2 = data.quantile(0.50)
        q3 = data.quantile(0.75)

        iqr = q3 - q1

        # ----------------------------------------
        # Distribution
        # ----------------------------------------

        skewness = data.skew()
        kurtosis = data.kurt()

        # ----------------------------------------
        # Outlier Detection
        # ----------------------------------------

        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)

        outliers = data[
            (data < lower_bound)
            |
            (data > upper_bound)
        ]

        # ----------------------------------------
        # Store Results
        # ----------------------------------------

        report[column] = {

            "Count": len(data),

            "Mean": mean,
            "Median": median,
            "Mode": mode,

            "Minimum": minimum,
            "Maximum": maximum,
            "Range": range_value,

            "Variance": variance,
            "Standard Deviation": standard_deviation,

            "Q1": q1,
            "Q2": q2,
            "Q3": q3,
            "IQR": iqr,

            "Skewness": skewness,
            "Kurtosis": kurtosis,

            "Outlier Count": len(outliers)
        }

    return report


# ============================================================
# SAVE REPORT TO TEXT FILE
# ============================================================

def save_report(report, file_name="statistical_report.txt"):
    """
    Save the generated statistical report
    as a text file.
    """

    os.makedirs(
        "reports",
        exist_ok=True
    )

    file_path = os.path.join(
        "reports",
        file_name
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "=" * 70 + "\n"
        )

        file.write(
            "             DESCRIPTIVE STATISTICS REPORT\n"
        )

        file.write(
            "=" * 70 + "\n\n"
        )

        for column, values in report.items():

            file.write(
                f"\nCOLUMN: {column}\n"
            )

            file.write(
                "-" * 50 + "\n"
            )

            for statistic, value in values.items():

                if isinstance(
                    value,
                    float
                ):

                    file.write(
                        f"{statistic:<25}: "
                        f"{value:.2f}\n"
                    )

                else:

                    file.write(
                        f"{statistic:<25}: "
                        f"{value}\n"
                    )

            file.write("\n")

    return file_path