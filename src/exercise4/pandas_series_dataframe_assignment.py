# CMP 269: Programming Methods III
# In-Class Assignment: Pandas Series and DataFrames

import pandas as pd


def task_1_series_creation():
    """
    TASK 1: Create a Series
    """

    print("--- Task 1: Building Series ---")

    buildings = {
        "Gillet": 4,
        "Carman": 3,
        "Music": 3,
        "Library": 4
    }

    building_series = pd.Series(buildings)

    print(building_series)


def task_2_dataframe_creation():
    """
    TASK 2: Create a DataFrame
    """

    print("\n--- Task 2: Course DataFrame ---")

    course_data = {
        "CourseCode": ["CMP168", "CMP269", "CMP338"],
        "Credits": [4, 4, 4],
        "Enrolled": [25, 30, 20]
    }

    df = pd.DataFrame(course_data)

    print(df)


def task_3_data_manipulation():
    """
    TASK 3: Filtering and Math
    """

    print("\n--- Task 3: Filtering and Math ---")

    course_data = {
        "CourseCode": ["CMP168", "CMP269", "CMP338"],
        "Credits": [4, 4, 4],
        "Enrolled": [25, 30, 20]
    }

    df = pd.DataFrame(course_data)

    filtered_df = df[df["Enrolled"] > 20]

    print("Courses with more than 20 students:")
    print(filtered_df)

    total_students = df["Enrolled"].sum()

    print("\nTotal Students:", total_students)


def task_4_csv_integration():
    """
    TASK 4: The Pandas CSV Advantage
    """

    print("\n--- Task 4: Easy CSV I/O ---")

    stock_data = {
        "Symbol": ["AAPL", "TSLA", "MSFT"],
        "Price": [210, 180, 430]
    }

    df = pd.DataFrame(stock_data)

    df.to_csv("stocks.csv", index=False)

    df_loaded = pd.read_csv("stocks.csv")

    print(df_loaded)


if __name__ == "__main__":
    task_1_series_creation()
    task_2_dataframe_creation()
    task_3_data_manipulation()
    task_4_csv_integration()