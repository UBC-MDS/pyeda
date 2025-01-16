import pytest
import pandas as pd
from pyeda.data_summary import get_summary_statistics

@pytest.fixture
def sample_df():
    data = {
        "numeric": [1, 2, 3, 4, 5],
        "categorical": ["a", "b", "a", "a", "c"],
        "missing": [None, None, None, None, None]
    }
    return pd.DataFrame(data)

def test_for_all_columns(sample_df):
    """Test the result of get summary function for all columns"""
    result = get_summary_statistics(sample_df)

    assert isinstance(result, pd.DataFrame)
    assert "mean" in result.index
    assert "std" in result.index
    assert "median" in result.index
    assert "unique_values" in result.index
    assert "most_frequent_value" in result.index
    assert result.loc["mean", "numeric"] == 3
    assert result.loc["most_frequent_value", "categorical"] == "a"

def test_for_selected_columns(sample_df):
    """Test the result of get summary function for selected columns"""
    result = get_summary_statistics(sample_df, col=["numeric", "categorical"])

    assert "numeric" in result.columns
    assert "categorical" in result.columns

def test_for_empty_dataframe():
    """Test the result of empty dataframe"""
    df = pd.DataFrame()
    result = get_summary_statistics(df)
    assert result.empty

def test_for_invalid_columns(sample_df):
    """Test the result of invalid columns"""
    with pytest.raises(KeyError):
        get_summary_statistics(sample_df, col=["non_exist"])