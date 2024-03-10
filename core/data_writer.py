import pandas as pd
import os
import pyarrow as pa
import pyarrow.parquet as pq


def write_df_to_parquet(df: pd.DataFrame, file_path: str, partition_cols: list):

    if not os.path.exists(file_path):
        os.mkdir(file_path)

    table = pa.Table.from_pandas(df)

    pq.write_to_dataset(table, f"{file_path}/output.parquet", partition_cols=partition_cols)

    