from pyeda31.pymissing_values_summary import missing_values_summary
import pytest
import pandas as pd

@pytest.fixture
def df():
    """
    Fixture to create a sample DataFrame for testing.
    """
    data = {
        'A': [1, 2, pd.NA, 4],
        'B': [pd.NA, pd.NA, 3, 4],
        'C': [1, 2, 3, 4]
    }
    return pd.DataFrame(data)

@pytest.fixture
def df_no_missing():
    """
    Fixture to create a DataFrame with no missing values.
    """
    data = {
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]
    }
    return pd.DataFrame(data)

@pytest.fixture
def df_with_none():
    """
    Fixture to create a DataFrame that contains None values.
    """
    data = {
        'A': [1, None, pd.NA, 4],  # None and pd.NA mixed in column A
        'B': [None, None, 3, 4],   # Only None values in column B
        'C': [1, 2, 3, 4]          # No missing values in column C
    }
    return pd.DataFrame(data)


def test_missing_values_summary(df):
    """
    Test for the missing_values_summary function.
    """
    result = missing_values_summary(df)

    # Expected results
    expected_index = ['B', 'A']  # Columns with missing values in descending order of missing count
    expected_values = ['2 (50.0%)', '1 (25.0%)']  # Expected values in the Series

    # Check if the result is a Series
    assert isinstance(result, pd.Series), "Result should be a Series."

    # Check if the resulting Series has the correct index
    assert list(result.index) == expected_index, "Index does not match the expected order."

    # Check the specific values in the Series
    assert list(result.values) == expected_values, "Values in the Series do not match the expected output."


def test_no_missing_values(df_no_missing):
    """
    Test case where no missing values exist in the DataFrame.
    """
    result = missing_values_summary(df_no_missing)

    # Check if the function returns an empty Series or the expected message
    assert result.empty or result == "No missing value!", (
        "Function should return 'No missing value!' or an empty Series when no missing values are present."
    )


def test_missing_values_summary_with_none(df_with_none):
    """
    Test case where the DataFrame contains None values.
    """
    result = missing_values_summary(df_with_none)

    # Expected results
    expected_index = {'B', 'A'}  # Use a set instead of a list (order-independent)
    expected_values = ['2 (50.0%)', '2 (50.0%)']  # None values counted as missing

    # Check if the result is a Series
    assert isinstance(result, pd.Series), "Result should be a Series."

    # Check if the resulting Series has the correct index (ignoring order)
    assert set(result.index) == expected_index, "Index does not match the expected order."

    # Check the specific values in the Series
    assert list(result.values) == expected_values, "Values in the Series do not match the expected output."
