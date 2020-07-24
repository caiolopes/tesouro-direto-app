import os

import pandas as pd

files = os.listdir(path="data")


def rentabilidade_dia(titulo):
    df = pd.read_json("data/" + files[0])
    df["data_carga"] = files[0][15:25]

    for n in range(1, len(files)):
        df_aux = pd.read_json("data/" + files[n])
        df_aux["data_carga"] = files[n][15:25]
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
