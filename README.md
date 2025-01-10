# pyeda

This python package creates an exploratory data analysis utility designed to streamline the initial stages of data exploration and statistic overview. The three core functions are file validation, handling missing values, and generating summary statistics. pyead provided to users a practical toolkit for data preprocessing and exploration, enabling users to work more effectively with csv datasets in various projects.

## Contributors

Catherine Meng, Jessie Zhang, Zheng He

## Functions

- **`check_csv`**  
    Check if the given file is a CSV file by its extension.
- **`missing_value_summary`**  
    This function is to provide a summary of missing values in the dataset.
- **`get_summary_statistics`**  
    Generate summary statistics for specified columns or all columns if none are provided.

## Contributing to the Python Ecosystem
The `pyeda` package complements the Python ecosystem by providing simple and efficient tools for users to implement quick EDA in the first step of their analysis. While there are some other similar Python packages such as [Sweetviz](https://pypi.org/project/sweetviz/) (in-depth EDA with a focus on visualization) and [perform-eda](https://pypi.org/project/perform-eda/) (providing comprehensive EDA analysis), these tools can be too heavyweight for quick analysis. Instead, our `pyeda` package aims for simplicity and efficiency, enabling users to quickly complete the most basic and important steps, including validating dataset formats, checking for missing values, and generating statistical summaries for columns of interest. It is a lightweight alternative for small-scale tasks or the initial understanding of the dataset for in_depth research. Users can also combine `pyeda` with other visualization packages for deeper insights.

## Installation

``` bash
$ pip install pyeda
```

## Usage

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pyeda` was created by Catherine Meng, Jessie Zhang, Zheng He. It is licensed under the terms of the MIT license.

## Credits

`pyeda` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
