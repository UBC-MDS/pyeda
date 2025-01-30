import pytest
import os
from pyeda31.check_csv import check_csv


@pytest.fixture
def csv_content():
    # Create a mock valid CSV content
    csv_content = "name,age\nJohn,25\nAlice,30"
    return csv_content


def test_check_csv_valid_file(csv_content):
    # Create a test CSV file
    file_path = 'test_valid.csv'
    with open(file_path, 'w') as f:
        f.write(csv_content)

    # Call the check_csv function
    result = check_csv(file_path)
    # Assert that the function returns True for a valid CSV
    assert result == True

    # Clean the test data file
    if os.path.exists(file_path):
        os.remove(file_path)


def test_check_csv_invalid_file_name(csv_content):
    # Create a test txt file
    file_path = 'test_invalid_name.txt'
    with open(file_path, 'w') as f:
        f.write(csv_content)

    # Call the check_csv function on a non-CSV file
    result = check_csv(file_path)
    # Assert that the function returns False for a non-CSV file
    assert result == False

    # Clean the test data file
    if os.path.exists(file_path):
        os.remove(file_path)


def test_check_csv_invalid_file_content():
    # Create a mock invalid file (non-CSV content)
    invalid_csv_content = """
        Name,Age,Score
        Alice,25,85
        Charlie,Thirty,70, 40
        David,40
    """
    
    # Create a test CSV file with invalid content
    file_path = 'test_invalid_content.csv'
    with open(file_path, 'w') as f:
        f.write(invalid_csv_content)

    # Call the check_csv function on a non-CSV file
    result = check_csv(file_path)
    # Assert that the function returns False for a non-CSV file
    assert result == False

    # Clean the test data file
    if os.path.exists(file_path):
        os.remove(file_path)