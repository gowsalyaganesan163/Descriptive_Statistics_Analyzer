# ============================================================
# FREQUENCY DISTRIBUTION MODULE
# ============================================================

import pandas as pd


# ============================================================
# CATEGORICAL FREQUENCY
# ============================================================

def categorical_frequency(dataset, column):
    """
    Calculate frequency and percentage
    for a categorical column.
    """

    if column not in dataset.columns:
        return None

    frequency = dataset[column].value_counts(
        dropna=False
    )

    percentage = dataset[column].value_counts(
        normalize=True,
        dropna=False
    ) * 100

    result = pd.DataFrame({
        "Frequency": frequency,
        "Percentage": percentage.round(2)
    })

    return result


# ============================================================
# NUMERICAL FREQUENCY
# ============================================================

def numerical_frequency(dataset, column, bins=5):
    """
    Create a frequency distribution for
    a numerical column using intervals.
    """

    if column not in dataset.columns:
        return None

    if not pd.api.types.is_numeric_dtype(
        dataset[column]
    ):
        return None

    # Create intervals
    intervals = pd.cut(
        dataset[column],
        bins=bins
    )

    # Calculate frequency
    frequency = intervals.value_counts(
        sort=False
    )

    # Calculate percentage
    percentage = (
        intervals.value_counts(
            sort=False,
            normalize=True
        ) * 100
    )

    result = pd.DataFrame({
        "Frequency": frequency,
        "Percentage": percentage.round(2)
    })

    return result


# ============================================================
# ALL CATEGORICAL FREQUENCIES
# ============================================================

def get_categorical_columns(dataset):
    """
    Return all categorical columns
    available in the dataset.
    """

    categorical_columns = dataset.select_dtypes(
        include=["object", "category", "bool"]
    ).columns.tolist()

    return categorical_columns


# ============================================================
# ALL NUMERICAL COLUMNS
# ============================================================

def get_numerical_columns(dataset):
    """
    Return all numerical columns
    available in the dataset.
    """

    numerical_columns = dataset.select_dtypes(
        include="number"
    ).columns.tolist()

    return numerical_columns