import pytest
import pandas as pd
import sys
import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from core.etl import transform_dataset

@pytest.fixture
def sample_data():
  data = {"product_id": ["test_product_id"], "product_category_name": ["test_product_category"], 
          "order_purchase_timestamp": ["2024-01-01 10:00:00"], "extra_column": ["test"]}
  return pd.DataFrame(data)
 

def test_transform_dataset(sample_data):
    df = transform_dataset(sample_data, ["product_id", "product_category_name", "order_purchase_timestamp"])

    assert list(df.columns) == ["product_id", "product_category_name", "order_purchase_timestamp"]
    assert len(df) > 0
    assert df.dtypes["order_purchase_timestamp"] == "datetime64[ns]"

