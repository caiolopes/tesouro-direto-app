import requests

import pandas as pd

import datetime

response = requests.get('https://www.tesourodireto.com.br/json/br/com/b3/tesourodireto/service/api/treasurybondsinfo.json', verify=False)

base = response.json()

base_aux = []

for i in range(len((base["response"]["TrsrBdTradgList"]))):
    base_aux.append(base["response"]["TrsrBdTradgList"][i]['TrsrBd'])

base = pd.DataFrame(base_aux)

base = base[['nm','anulInvstmtRate','minInvstmtAmt','untrInvstmtVal','untrRedVal','mtrtyDt','anulRedRate']]

base.rename(columns = {'nm' : 'titulo','anulInvstmtRate' : 'rentabilidade_anual_investir','minInvstmtAmt' :'investimento_minimo_investir',
                      'untrInvstmtVal' : 'preco_unitario_investir', 'untrRedVal' : 'preco_unitario_resgate',
                      'mtrtyDt' : 'vencimento', 'anulRedRate' : 'rentabilidade_anual_resgate'}, inplace =True )

base['vencimento'] = pd.to_datetime(base['vencimento'], format ='%Y-%m-%d')

base['vencimento'] = base['vencimento'].astype(str)

base.to_json('bd_tesouro_app.json_' + str(datetime.datetime.now())[:10] ,orient = 'records')

