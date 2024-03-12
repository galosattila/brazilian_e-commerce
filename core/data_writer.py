import pandas as pd
import os
import pyarrow as pa
import pyarrow.parquet as pq


def write_df_to_parquet(df: pd.DataFrame, file_path: str, partition_cols: list):

    if not os.path.exists(file_path):
        os.mkdir(file_path)

    try:
        table = pa.Table.from_pandas(df)
        pq.write_to_dataset(table, f"{file_path}/output.parquet", partition_cols=partition_cols)
    
    except KeyError as e:
        missing_cols = [col for col in partition_cols if col not in df.columns]
        if missing_cols:
            print(f"Error: Missing partition columns: {', '.join(missing_cols)}")
            exit(1)
   
        

    