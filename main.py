import pandas as pd

from pathlib import Path

base = Path("base")

CIDADES_PADRAO = [
    "RIBEIRAO PRETO"
    "SJ RIO PRETO",
    "S.J.V.RIO PRETO",
    "CATANDUVA",
    "MIRASSOL",
    "OLIMPIA",
    "FERNANDOPOLIS",
    "JALES",
    "SEBASTIANOPOIS",
    "SEBASTIANOP.SUL",
    "VOTUPORANGA",
    "BOTUCATU",
    "BOFETE",
    "MARIA",
    "CENTRO",
    "ITAI",
    "PARANAPANEMA",
    "ARACATUBA",
    "BIRIGUI",
    "PENAPOLI",
    "ANDRADINA",
    "ARARAQUARA",
    "BARRETOS",
    "PIRASSUNUNGA",
    "SAO CARLOS",
    "JABOTICABAL",
    "FRANCA",
    "SERTAOZINHO",
    "BEBEDOURO",
    "IBITINGA",
    "MATAO",
    "MOCOCA",
    "CORRENTE",
    "CORRENTES",
    "RIBEIR.CORRENTE",
    "ITIRAPUA",
    "CLARAVAL",
    "ITUVERAVA",
    "BELA VISTA",
    "BATATAIS",
]

tipos_validos = ["S01", "S02", "S04", "s05"]

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

    batch["BOX"] = batch["BOX"].astype("int64[pyarrow]")

    batchs.append(batch)

    print(f"arquivo {arq.name} lido\n")

df = pd.concat(batchs, ignore_index=True)

df['Cidade'] = (
    df['Cidade']
    .str.strip()
    .str.upper()
)

df['Tipo do pedido'] = (
    df['Tipo do pedido']
    .str.strip()
    .str.upper()
)

#df = df[df['Cidade'].isin(CIDADES_PADRAO)]
df = df[df['Tipo do pedido'].isin(tipos_validos)]

df["Data ultima movimentação"] = pd.to_datetime(
    df["Data ultima movimentação"],
    dayfirst=False,
    errors="coerce"
)

data_limite = pd.Timestamp.today() - pd.DateOffset(months=6)

df = df[df["Data ultima movimentação"] >= data_limite]

df['mes'] = df['Data ultima movimentação'].dt.to_period('M')

df.to_csv("city_for_template.csv", index=False)

print(df.head())
print("\n==========================\n")
print(df.shape)
print("\n==========================\n")
print(df.dtypes)
print("\n==========================\n")
print("\nMemória (MB):", df.memory_usage(deep=True).sum() / 1024**2)