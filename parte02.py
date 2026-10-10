import pandas as pd

df = pd.read_sql(
    "SELECT * FROM netflix1",
    conexao
)

df.to_parquet(
    "netflix.parquet",
    index=False
)