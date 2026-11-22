# ============================================================
# MEASURES OF DISPERSION MODULE
# ============================================================

def calculate_dispersion(dataset):
    """
    Calculate Range, Variance and Standard Deviation
    for all numerical columns.
    """

    numerical_data = dataset.select_dtypes(
        include="number"
    )

    if numerical_data.empty:
        return None

    # Range
    range_value = (
        numerical_data.max()
        - numerical_data.min()
    )

    # Variance
    variance = numerical_data.var()

    # Standard Deviation
    standard_deviation = numerical_data.std()

    result = {
        "range": range_value,
        "variance": variance,
        "standard_deviation": standard_deviation
    }

    return result