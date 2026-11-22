# ============================================================
# CENTRAL TENDENCY MODULE
# ============================================================

def calculate_central_tendency(dataset):
    """
    Calculate mean, median and mode
    for all numerical columns.
    """

    numerical_data = dataset.select_dtypes(
        include="number"
    )

    if numerical_data.empty:
        return None

    result = {
        "mean": numerical_data.mean(),
        "median": numerical_data.median(),
        "mode": numerical_data.mode().iloc[0]
    }

    return result