import pandas as pd

def check_csv(file_path):
    """Check if the given file has a CSV file extension and whether it can be read by the pandas library.

    Parameters
    ----------
    file_path: str
        Path to the file.

    Returns
    -------
    bool
        True if the file has a CSV extension and can be read by the pandas library.
        False otherwise (e.g., incorrect file extension or read error).

    Examples
    --------
    >>> from pyeda31.check_csv import check_csv
    >>> check_csv("../data/raw/data.csv")
    True
    >>> check_csv("../data/raw/data.txt")
    False
    """
    # Check if file extension is .csv
    if not file_path.endswith(".csv"):
        print("The file name does not end with '.csv'.")
        return False

    # Try to read the file using pandas (this will raise an error if it's not a CSV file)
    try:
        pd.read_csv(file_path)
        return True
    except Exception as e:
        print("There is an error when try to read the data file using pandas:")
        print(e)
        return False