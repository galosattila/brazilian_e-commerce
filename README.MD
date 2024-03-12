# Readme

This document provides instructions for setting up, running, and testing the ETL project for processing e-commerce data.


# Project description

This project implements an Extract, Transform, Load (ETL) pipeline to process e-commerce data from CSV files and write the transformed data to Parquet format with partitioning.


# Environment setup

1. Python Version
    This project is tested with Python 3.12 (Specify the compatible Python version). Ensure you have a compatible version installed. You can check your Python version using: `python --version`
2. Create a Virtual Environment (Recommended)
    It's recommended to use a virtual environment to isolate project dependencies. You can create a virtual environment using: `python -m venv .venv`
    This will create a virtual environment named .venv in your current directory. Activate it using the following command: `source .venv/bin/activate`
3. Install dependencies
    Activate your virtual environment (if created). Then, install the required libraries using pip: `pip install -r requirements.txt`


# Configuration

The project uses a YAML configuration file (config/dev.yaml) to specify environment-specific settings. You can copy the provided dev.yaml file and adjust the values for different environments (e.g., test.yaml, prod.yaml).


# Configuration Options:

   - `input_path`: Path to the directory containing the input CSV files (e.g., `olist_orders_dataset.csv`, `olist_order_items_dataset.csv`, `olist_products_dataset.csv`).
   - `output_path`: Path to the directory where the processed data will be written as a Parquet file.
   - `partition_cols`: List of column names to use for partitioning the output Parquet data (currently set to `["product_category_name"]`).


# Editing Configuration Files:

Modify the values for `input_path`, `output_path`, and `partition_cols` (if applicable) within the respective configuration file (e.g., `dev.yaml`) according to your environment and data setup.


# Dataset files

Place your input CSV files (e.g., `olist_orders_dataset.csv`, `olist_order_items_dataset.csv`, `olist_products_dataset.csv`) in the directory specified by the input_path configuration option in the YAML file. Ensure they have the same structure as the expected data.


# Running the Script

1. Navigate to the project directory in your terminal.
2. Make sure your virtual environment is activated (if created).
3. Execute the script using the following command, specifying the environment you want to use (replace `dev` with the appropriate environment name): `python main.py --env dev`

This will read the configuration from `config/dev.yaml`, load the data, process it, and write the results to Parquet format in the specified `output_path`.

# Running Tests

The project includes unit tests to ensure the data transformation logic works as expected. To run the tests, navigate to the project directory and execute: `pytest`