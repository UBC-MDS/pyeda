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
    expected_columns = ['Missing Count', 'Missing Percentage']
    expected_index = ['B', 'A']  # Columns with missing values in descending order of missing count

    # Check if the resulting DataFrame has the correct structure
    assert list(result.columns) == expected_columns
    assert list(result.index) == expected_index

    # Check the specific values
    assert result.loc['B', 'Missing Count'] == 2
    assert result.loc['B', 'Missing Percentage'] == 50.0
    assert result.loc['A', 'Missing Count'] == 1
    assert result.loc['A', 'Missing Percentage'] == 25.0