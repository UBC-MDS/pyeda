import pandas as pd


def missing_values_summary(df):
    """
    This function is to provide a summary of missing values in the dataset.

    Parameters
    ----------
    df (pd.DataFrame): The DataFrame containing the data.

    Returns
    -------
    pd.DataFrame: A DataFrame showing the count and percentage of missing values.

    Examples
    --------
    >>> missing_values_summary(df)
    """
    # Calculate the count of missing values for each column
    missing_count = df.isnull().sum()
    
    # Calculate the percentage of missing values for each column
    missing_percentage = (missing_count / len(df)) * 100

    # Create a summary DataFrame
    missing_summary = pd.DataFrame({
        'Missing Count': missing_count,
        'Missing Percentage': missing_percentage
    })

    # Filter out columns with no missing values
    missing_summary = missing_summary[missing_summary['Missing Count'] > 0]

    # Sort the DataFrame by the count of missing values in descending order
    missing_summary = missing_summary.sort_values(by='Missing Count', ascending=False)

    return missing_summary

