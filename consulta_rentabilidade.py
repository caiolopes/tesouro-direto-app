import os

import pandas as pd


def rentabilidade_dia(titulo):
    files = os.listdir(path="data")

    # from 15 to 15 is the date in the format YYYY-MM-DD
    data_slice = slice(15, 25)

    df = pd.DataFrame()

    for filename in files:
        df_aux = pd.read_json("data/" + filename)
        df_aux["data_carga"] = filename[data_slice]
        df = pd.concat([df, df_aux])

    df["data_carga"] = pd.to_datetime(df["data_carga"])
    df["vencimento"] = pd.to_datetime(df["vencimento"])
    cols = ["rentabilidade_anual_investir", "rentabilidade_anual_resgate"]
    res = df[df["titulo"] == titulo].groupby("data_carga")[cols].mean()

    res.rename(
        columns={
            "data_carga": "data",
            "rentabilidade_anual_investir": "investimento",
            "rentabilidade_anual_resgate": "resgate",
        },
        inplace=True,
    )

    return res
