# Análise rápida de Qtde. Expedida

Script para calcular a soma de **Qtde. Expedida** nos últimos 6 meses (baseado em **Data ultima movimentação**), filtrando por uma lista fixa de cidades e agrupando por **Setor do Item**.

## Formato esperado do CSV

O arquivo precisa conter as colunas:

- `Cidade`
- `Estado`
- `Data ultima movimentação`
- `Setor do Item`
- `Qtde. Expedida`

## Como executar

```bash
python main.py caminho/arquivo.csv --estado SP
```

- `--estado` é opcional. Se omitido, considera todos os estados.
- Saída no formato: `Setor do Item;Qtde. Expedida`.

## Observações

- O período de 6 meses é aproximado para 183 dias retroativos a partir da data atual.
- Datas aceitas (entre outras): `YYYY-MM-DD`, `DD/MM/YYYY`, com ou sem horário.
