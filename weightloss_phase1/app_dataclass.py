from dataclasses import dataclass
from typing import List

import pandas as pd

@dataclass
class Peserta:
    
    name : str
    progress : List

if __name__ == '__main__':
    pserta_peserta = []

    df = pd.read_csv('datasets/progress_phase1_no_NaN.csv', sep=',', thousands=' ')
    
    # print(df['Adz'].values.tolist())
    for n in df.columns[1:]:
        peserta_dan_progress = df[n]
        pserta_peserta.append(Peserta(n, peserta_dan_progress.values.tolist()))

    print(pserta_peserta)