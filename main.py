import pandas as pd

from pathlib import Path

base = Path("base")

cols = [
    "Bandeira",
    "BOX",
    "Tipo do pedido",
    "Cidade",
    "Estado",
    "Setor do Item",
    "Status",
    "Qtde. Expedida",
    "Data ultima movimentação" 
]

batchs = []

for arq in base.glob("*.csv"):
    batch = pd.read_csv(
        arq,
        encoding="utf-16",
        sep="\t",
        usecols=cols,
        dtype_backend="pyarrow"
    )

    # Ajuste de schema
    batch["Data ultima movimentação"] = pd.to_datetime(
        batch["Data ultima movimentação"],
        format="%d/%m/%Y  %H:%M:%S", # Dois espaços
        errors="coerce"
    )

    batch["BOX"] = batch["BOX"].astype("int64[pyarrow]")

    batchs.append(batch)

    print(f"arquivo {arq.name} lido\n")

df = pd.concat(batchs, ignore_index=True)


print(df.head())
print("\n==========================\n")
print(df.shape)
print("\n==========================\n")
print(df.dtypes)
print("\n==========================\n")
print("\nMemória (MB):", df.memory_usage(deep=True).sum() / 1024**2)