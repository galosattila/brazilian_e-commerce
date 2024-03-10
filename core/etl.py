import pandas as pd
from core.data_loader import load_data_from_csv
from core.data_writer import write_df_to_parquet

def prepare_dataset(input_path: str, output_path: str, partition_cols: str):
    orders_df = load_data_from_csv(f"{input_path}/olist_orders_dataset.csv") 
    order_items_df = load_data_from_csv(f"{input_path}/olist_order_items_dataset.csv")
    products_df = load_data_from_csv(f"{input_path}/olist_products_dataset.csv")
    
    
    df = order_items_df.merge(products_df, how="left", on="product_id")
    df = df.merge(orders_df, how="left", on="order_id")

    final_df = transform_dataset(df, ["product_id", "product_category_name", "order_purchase_timestamp"])


    write_df_to_parquet(final_df, output_path, partition_cols)
    
    print(f"Dataset has been prepared.")

    return final_df


def transform_dataset(df: pd.DataFrame, columns: list):
    df = cast_as_timestamp(df, "order_purchase_timestamp")
    return df[columns]

def cast_as_timestamp(df: pd.DataFrame, column: str):
    df[column] = pd.to_datetime(df[column])
    return df
