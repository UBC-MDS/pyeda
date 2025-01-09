def get_summary_statistics(df, col = None):
    """
    Generate summary statistics for specified columns or all columns if none are provided.

    This function will return the important statistics (e.g. mean, min, std) for numeric columns, as well as
    some key metrics (e.g. count, unique) for non-numeric columns.
    
    Parameters
    ----------
    df : pd.DataFrame
        The dataframe containing the data for analysis.
    col : list or None
        A list of column names for which to get statistics. 
        Default value is None, the function will apply for all columns.

    Returns
    ----------
    pd.DataFrame
        A DataFrame with summary statistics for the specified columns.
    """
    pass