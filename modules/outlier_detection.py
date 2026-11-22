# ============================================================
# OUTLIER DETECTION MODULE
# ============================================================


def detect_outliers(dataset):
    """
    Detect outliers in all numerical columns
    using the IQR method.
    """

    numerical_data = dataset.select_dtypes(
        include="number"
    )

    if numerical_data.empty:
        return None

    results = {}

    for column in numerical_data.columns:

        # ----------------------------------------
        # Calculate Q1 and Q3
        # ----------------------------------------

        q1 = numerical_data[column].quantile(0.25)

        q3 = numerical_data[column].quantile(0.75)

        # ----------------------------------------
        # Calculate IQR
        # ----------------------------------------

        iqr = q3 - q1

        # ----------------------------------------
        # Calculate Lower Bound
        # ----------------------------------------

        lower_bound = q1 - (1.5 * iqr)

        # ----------------------------------------
        # Calculate Upper Bound
        # ----------------------------------------

        upper_bound = q3 + (1.5 * iqr)

        # ----------------------------------------
        # Find Outliers
        # ----------------------------------------

        outliers = numerical_data[
            (numerical_data[column] < lower_bound)
            |
            (numerical_data[column] > upper_bound)
        ][column]

        # ----------------------------------------
        # Store Results
        # ----------------------------------------

        results[column] = {
            "Q1": q1,
            "Q3": q3,
            "IQR": iqr,
            "Lower Bound": lower_bound,
            "Upper Bound": upper_bound,
            "Outliers": outliers.tolist(),
            "Outlier Count": len(outliers)
        }

    return results