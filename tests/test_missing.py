from pyeda.pymissing_values_summary import missing_values_summary
import pytest
import pandas as pd

@pytest.fixture
def df():
    """
    Fixture to create a sample DataFrame for testing.
    """
    data = {
        'A': [1, 2, None, 4],
        'B': [None, None, 3, 4],
        'C': [1, 2, 3, 4]
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
