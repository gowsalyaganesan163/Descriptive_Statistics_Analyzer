# ============================================================
# QUARTILES & PERCENTILES MODULE
# ============================================================


def calculate_quartiles(dataset):
    """
    Calculate Q1, Q2, Q3 and IQR
    for all numerical columns.
    """

    numerical_data = dataset.select_dtypes(
        include="number"
    )

    if numerical_data.empty:
        return None

    # First Quartile
    q1 = numerical_data.quantile(0.25)

    # Second Quartile / Median
    q2 = numerical_data.quantile(0.50)

    # Third Quartile
    q3 = numerical_data.quantile(0.75)

    # Interquartile Range
    iqr = q3 - q1

    result = {
        "q1": q1,
        "q2": q2,
        "q3": q3,
        "iqr": iqr
    }

    return result


# ============================================================
# PERCENTILE CALCULATION
# ============================================================

def calculate_percentiles(dataset, percentile_values=None):
    """
    Calculate selected percentiles
    for all numerical columns.
    """

    numerical_data = dataset.select_dtypes(
        include="number"
    )

    if numerical_data.empty:
        return None

    # Default percentiles
    if percentile_values is None:
        percentile_values = [
            10,
            25,
            50,
            75,
            90
        ]

    result = {}

    for percentile in percentile_values:

        result[percentile] = numerical_data.quantile(
            percentile / 100
        )

    return result