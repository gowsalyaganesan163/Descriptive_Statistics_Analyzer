# ============================================================
# DESCRIPTIVE STATISTICS ANALYZER
# ============================================================

import tkinter as tk
from tkinter import filedialog

import pandas as pd

# ============================================================
# IMPORT STATISTICAL MODULES
# ============================================================

from modules.central_tendency import (
    calculate_central_tendency
)

from modules.dispersion import (
    calculate_dispersion
)

from modules.quartiles import (
    calculate_quartiles,
    calculate_percentiles
)

from modules.frequency_distribution import (
    categorical_frequency,
    numerical_frequency,
    get_categorical_columns,
    get_numerical_columns
)

from modules.outlier_detection import (
    detect_outliers
)

from modules.distribution_analysis import (
    analyze_distribution
)

from modules.correlation_analysis import (
    analyze_correlation
)

from modules.summary_report import (
    generate_summary_report,
    save_report
)


# ============================================================
# GLOBAL DATASET
# ============================================================

dataset = None


# ============================================================
# DISPLAY HEADER
# ============================================================

def display_header():

    print("\n" + "=" * 65)
    print("              DESCRIPTIVE STATISTICS ANALYZER")
    print("=" * 65)


# ============================================================
# DISPLAY MENU
# ============================================================

def display_menu():

    print("\n" + "-" * 65)
    print("                         MAIN MENU")
    print("-" * 65)

    print("1.  Load Dataset")
    print("2.  Data Overview")
    print("3.  Central Tendency")
    print("4.  Measures of Dispersion")
    print("5.  Quartiles & Percentiles")
    print("6.  Frequency Distribution")
    print("7.  Outlier Detection")
    print("8.  Distribution Analysis")
    print("9.  Correlation Analysis")
    print("10. Visualizations")
    print("11. Generate Statistical Report")
    print("12. Exit")

    print("-" * 65)


# ============================================================
# LOAD DATASET USING TKINTER
# ============================================================

def load_dataset():

    global dataset

    # ----------------------------------------
    # Create hidden Tkinter window
    # ----------------------------------------

    root = tk.Tk()

    root.withdraw()

    # ----------------------------------------
    # Open file selection dialog
    # ----------------------------------------

    file_path = filedialog.askopenfilename(
        title="Select Dataset",
        filetypes=[
            ("CSV Files", "*.csv"),
            ("Excel Files", "*.xlsx *.xls"),
            ("All Files", "*.*")
        ]
    )

    # ----------------------------------------
    # Close Tkinter window
    # ----------------------------------------

    root.destroy()

    # ----------------------------------------
    # Check file selection
    # ----------------------------------------

    if not file_path:

        print("\n❌ No dataset selected.")

        return

    try:

        # ----------------------------------------
        # Read CSV
        # ----------------------------------------

        if file_path.lower().endswith(".csv"):

            dataset = pd.read_csv(
                file_path
            )

        # ----------------------------------------
        # Read Excel
        # ----------------------------------------

        elif file_path.lower().endswith(
            (".xlsx", ".xls")
        ):

            dataset = pd.read_excel(
                file_path
            )

        else:

            print(
                "\n❌ Unsupported file format."
            )

            return

        # ----------------------------------------
        # Display Dataset Information
        # ----------------------------------------

        print("\n" + "=" * 65)
        print("              DATASET LOADED SUCCESSFULLY")
        print("=" * 65)

        print(
            f"\nFile    : {file_path}"
        )

        print(
            f"Rows    : {dataset.shape[0]}"
        )

        print(
            f"Columns : {dataset.shape[1]}"
        )

        print("\nColumn Names:")

        for column in dataset.columns:

            print(
                f"  • {column}"
            )

    except Exception as error:

        print(
            "\n❌ Error while loading dataset."
        )

        print(
            f"Error : {error}"
        )


# ============================================================
# CHECK DATASET
# ============================================================

def dataset_loaded():

    if dataset is None:

        print(
            "\n⚠️ Please load a dataset first."
        )

        return False

    return True


# ============================================================
# DATA OVERVIEW
# ============================================================

def data_overview():

    if not dataset_loaded():

        return

    print("\n" + "=" * 65)
    print("                       DATA OVERVIEW")
    print("=" * 65)

    # ----------------------------------------
    # First 5 rows
    # ----------------------------------------

    print("\nFirst 5 Rows:")

    print(
        dataset.head()
    )

    # ----------------------------------------
    # Last 5 rows
    # ----------------------------------------

    print("\n\nLast 5 Rows:")

    print(
        dataset.tail()
    )

    # ----------------------------------------
    # Shape
    # ----------------------------------------

    print("\n\nDataset Shape:")

    print(
        dataset.shape
    )

    # ----------------------------------------
    # Columns
    # ----------------------------------------

    print("\n\nColumn Names:")

    for column in dataset.columns:

        print(
            f"  • {column}"
        )

    # ----------------------------------------
    # Data Types
    # ----------------------------------------

    print("\n\nData Types:")

    print(
        dataset.dtypes
    )

    # ----------------------------------------
    # Missing Values
    # ----------------------------------------

    print("\n\nMissing Values:")

    print(
        dataset.isnull().sum()
    )

    # ----------------------------------------
    # Duplicate Rows
    # ----------------------------------------

    print("\n\nDuplicate Rows:")

    print(
        dataset.duplicated().sum()
    )


# ============================================================
# CENTRAL TENDENCY
# ============================================================

def show_central_tendency():

    if not dataset_loaded():

        return

    result = calculate_central_tendency(
        dataset
    )

    if result is None:

        print(
            "\n❌ No numerical columns found."
        )

        return

    print("\n" + "=" * 65)
    print("                     CENTRAL TENDENCY")
    print("=" * 65)

    print("\nMean:")

    print(
        result["mean"]
    )

    print("\nMedian:")

    print(
        result["median"]
    )

    print("\nMode:")

    print(
        result["mode"]
    )


# ============================================================
# DISPERSION
# ============================================================

def show_dispersion():

    if not dataset_loaded():

        return

    result = calculate_dispersion(
        dataset
    )

    if result is None:

        print(
            "\n❌ No numerical columns found."
        )

        return

    print("\n" + "=" * 65)
    print("                  MEASURES OF DISPERSION")
    print("=" * 65)

    print("\nRange:")

    print(
        result["range"]
    )

    print("\nVariance:")

    print(
        result["variance"]
    )

    print("\nStandard Deviation:")

    print(
        result["standard_deviation"]
    )


# ============================================================
# QUARTILES & PERCENTILES
# ============================================================

def show_quartiles():

    if not dataset_loaded():

        return

    result = calculate_quartiles(
        dataset
    )

    if result is None:

        print(
            "\n❌ No numerical columns found."
        )

        return

    print("\n" + "=" * 65)
    print("                  QUARTILES & IQR")
    print("=" * 65)

    print("\nQ1:")

    print(
        result["q1"]
    )

    print("\nQ2 / Median:")

    print(
        result["q2"]
    )

    print("\nQ3:")

    print(
        result["q3"]
    )

    print("\nIQR:")

    print(
        result["iqr"]
    )

    # ----------------------------------------
    # Percentiles
    # ----------------------------------------

    print("\n" + "-" * 65)
    print("                     PERCENTILES")
    print("-" * 65)

    percentile_result = calculate_percentiles(
        dataset
    )

    for percentile, values in (
        percentile_result.items()
    ):

        print(
            f"\n{percentile}th Percentile:"
        )

        print(
            values
        )


# ============================================================
# FREQUENCY DISTRIBUTION
# ============================================================

def show_frequency_distribution():

    if not dataset_loaded():

        return

    categorical_columns = (
        get_categorical_columns(
            dataset
        )
    )

    numerical_columns = (
        get_numerical_columns(
            dataset
        )
    )

    print("\n" + "=" * 65)
    print("                  FREQUENCY DISTRIBUTION")
    print("=" * 65)

    # ----------------------------------------
    # Categorical Columns
    # ----------------------------------------

    if categorical_columns:

        print("\nCategorical Columns:")

        for index, column in enumerate(
            categorical_columns,
            start=1
        ):

            print(
                f"{index}. {column}"
            )

        try:

            choice = int(
                input(
                    "\nSelect categorical column "
                    "number: "
                )
            )

            if (
                choice < 1
                or choice > len(
                    categorical_columns
                )
            ):

                print(
                    "\n❌ Invalid selection."
                )

                return

            selected_column = (
                categorical_columns[
                    choice - 1
                ]
            )

            result = categorical_frequency(
                dataset,
                selected_column
            )

            print(
                f"\nFrequency Distribution "
                f"for '{selected_column}':"
            )

            print(
                result
            )

        except ValueError:

            print(
                "\n❌ Please enter a valid number."
            )

    # ----------------------------------------
    # Numerical Columns
    # ----------------------------------------

    elif numerical_columns:

        print(
            "\nNo categorical columns found."
        )

        print(
            "\nNumerical Columns:"
        )

        for index, column in enumerate(
            numerical_columns,
            start=1
        ):

            print(
                f"{index}. {column}"
            )

        try:

            choice = int(
                input(
                    "\nSelect numerical column "
                    "number: "
                )
            )

            selected_column = (
                numerical_columns[
                    choice - 1
                ]
            )

            result = numerical_frequency(
                dataset,
                selected_column
            )

            print(
                f"\nFrequency Distribution "
                f"for '{selected_column}':"
            )

            print(
                result
            )

        except (
            ValueError,
            IndexError
        ):

            print(
                "\n❌ Invalid selection."
            )

    else:

        print(
            "\n❌ No suitable columns found."
        )


# ============================================================
# OUTLIER DETECTION
# ============================================================

def show_outliers():

    if not dataset_loaded():

        return

    result = detect_outliers(
        dataset
    )

    if result is None:

        print(
            "\n❌ No numerical columns found."
        )

        return

    print("\n" + "=" * 65)
    print("                    OUTLIER DETECTION")
    print("=" * 65)

    for column, values in result.items():

        print(
            f"\nColumn: {column}"
        )

        print(
            f"Q1            : "
            f"{values['Q1']:.2f}"
        )

        print(
            f"Q3            : "
            f"{values['Q3']:.2f}"
        )

        print(
            f"IQR           : "
            f"{values['IQR']:.2f}"
        )

        print(
            f"Lower Bound   : "
            f"{values['Lower Bound']:.2f}"
        )

        print(
            f"Upper Bound   : "
            f"{values['Upper Bound']:.2f}"
        )

        print(
            f"Outlier Count : "
            f"{values['Outlier Count']}"
        )

        print(
            f"Outliers      : "
            f"{values['Outliers']}"
        )


# ============================================================
# DISTRIBUTION ANALYSIS
# ============================================================

def show_distribution():

    if not dataset_loaded():

        return

    result = analyze_distribution(
        dataset
    )

    if result is None:

        print(
            "\n❌ No numerical columns found."
        )

        return

    print("\n" + "=" * 65)
    print("                  DISTRIBUTION ANALYSIS")
    print("=" * 65)

    for column, values in result.items():

        print(
            f"\nColumn: {column}"
        )

        print(
            f"Mean         : "
            f"{values['Mean']:.2f}"
        )

        print(
            f"Median       : "
            f"{values['Median']:.2f}"
        )

        print(
            f"Skewness     : "
            f"{values['Skewness']:.2f}"
        )

        print(
            f"Kurtosis     : "
            f"{values['Kurtosis']:.2f}"
        )

        print(
            f"Interpretation: "
            f"{values['Interpretation']}"
        )

    print(
        "\n📊 Distribution histograms "
        "have been generated."
    )


# ============================================================
# CORRELATION ANALYSIS
# ============================================================

def show_correlation():

    if not dataset_loaded():

        return

    result = analyze_correlation(
        dataset
    )

    if result is None:

        print(
            "\n❌ At least two numerical "
            "columns are required."
        )

        return

    print("\n" + "=" * 65)
    print("                    CORRELATION ANALYSIS")
    print("=" * 65)

    print("\nCorrelation Matrix:")

    print(
        result["matrix"]
    )

    print("\n" + "-" * 65)
    print("                    RELATIONSHIPS")
    print("-" * 65)

    for relationship, values in (
        result["relationships"].items()
    ):

        print(
            f"\n{relationship}"
        )

        print(
            f"Correlation : "
            f"{values['Correlation']:.2f}"
        )

        print(
            f"Interpretation : "
            f"{values['Interpretation']}"
        )

    print(
        "\n📊 Correlation heatmap "
        "has been generated."
    )


# ============================================================
# VISUALIZATION INFORMATION
# ============================================================

def show_visualizations():

    if not dataset_loaded():

        return

    print("\n" + "=" * 65)
    print("                     VISUALIZATIONS")
    print("=" * 65)

    print(
        "\nThe project automatically generates "
        "visualizations during analysis:"
    )

    print(
        "\n1. Distribution Analysis"
    )

    print(
        "   → Histogram"
    )

    print(
        "   → Mean and Median lines"
    )

    print(
        "\n2. Correlation Analysis"
    )

    print(
        "   → Correlation Heatmap"
    )

    print(
        "\nGenerated images are saved inside:"
    )

    print(
        "   visualizations/"
    )

    print(
        "\n💡 Run Option 8 or Option 9 "
        "to generate the respective charts."
    )


# ============================================================
# STATISTICAL REPORT
# ============================================================

def show_report():

    if not dataset_loaded():

        return

    report = generate_summary_report(
        dataset
    )

    if report is None:

        print(
            "\n❌ No numerical columns found."
        )

        return

    print("\n" + "=" * 65)
    print("                  STATISTICAL REPORT")
    print("=" * 65)

    for column, values in report.items():

        print(
            f"\nCOLUMN: {column}"
        )

        print(
            "-" * 50
        )

        print(
            f"Count              : "
            f"{values['Count']}"
        )

        print(
            f"Mean               : "
            f"{values['Mean']:.2f}"
        )

        print(
            f"Median             : "
            f"{values['Median']:.2f}"
        )

        print(
            f"Mode               : "
            f"{values['Mode']}"
        )

        print(
            f"Minimum            : "
            f"{values['Minimum']:.2f}"
        )

        print(
            f"Maximum            : "
            f"{values['Maximum']:.2f}"
        )

        print(
            f"Range              : "
            f"{values['Range']:.2f}"
        )

        print(
            f"Variance           : "
            f"{values['Variance']:.2f}"
        )

        print(
            f"Standard Deviation : "
            f"{values['Standard Deviation']:.2f}"
        )

        print(
            f"Q1                 : "
            f"{values['Q1']:.2f}"
        )

        print(
            f"Q2                 : "
            f"{values['Q2']:.2f}"
        )

        print(
            f"Q3                 : "
            f"{values['Q3']:.2f}"
        )

        print(
            f"IQR                : "
            f"{values['IQR']:.2f}"
        )

        print(
            f"Skewness           : "
            f"{values['Skewness']:.2f}"
        )

        print(
            f"Kurtosis           : "
            f"{values['Kurtosis']:.2f}"
        )

        print(
            f"Outlier Count      : "
            f"{values['Outlier Count']}"
        )

    # ----------------------------------------
    # Save Report
    # ----------------------------------------

    file_path = save_report(
        report
    )

    print(
        "\n" + "=" * 65
    )

    print(
        "✅ Statistical report saved successfully."
    )

    print(
        f"📄 Location: {file_path}"
    )


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    display_header()

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        # ----------------------------------------
        # 1. Load Dataset
        # ----------------------------------------

        if choice == "1":

            load_dataset()

        # ----------------------------------------
        # 2. Data Overview
        # ----------------------------------------

        elif choice == "2":

            data_overview()

        # ----------------------------------------
        # 3. Central Tendency
        # ----------------------------------------

        elif choice == "3":

            show_central_tendency()

        # ----------------------------------------
        # 4. Dispersion
        # ----------------------------------------

        elif choice == "4":

            show_dispersion()

        # ----------------------------------------
        # 5. Quartiles & Percentiles
        # ----------------------------------------

        elif choice == "5":

            show_quartiles()

        # ----------------------------------------
        # 6. Frequency Distribution
        # ----------------------------------------

        elif choice == "6":

            show_frequency_distribution()

        # ----------------------------------------
        # 7. Outlier Detection
        # ----------------------------------------

        elif choice == "7":

            show_outliers()

        # ----------------------------------------
        # 8. Distribution Analysis
        # ----------------------------------------

        elif choice == "8":

            show_distribution()

        # ----------------------------------------
        # 9. Correlation Analysis
        # ----------------------------------------

        elif choice == "9":

            show_correlation()

        # ----------------------------------------
        # 10. Visualizations
        # ----------------------------------------

        elif choice == "10":

            show_visualizations()

        # ----------------------------------------
        # 11. Statistical Report
        # ----------------------------------------

        elif choice == "11":

            show_report()

        # ----------------------------------------
        # 12. Exit
        # ----------------------------------------

        elif choice == "12":

            print("\n" + "=" * 65)

            print(
                "Thank you for using "
                "Descriptive Statistics Analyzer!"
            )

            print("=" * 65)

            break

        # ----------------------------------------
        # Invalid Choice
        # ----------------------------------------

        else:

            print(
                "\n❌ Invalid choice."
            )

            print(
                "Please select a number between 1 and 12."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()