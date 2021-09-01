from dataclasses import dataclass
from typing import List

import pandas as pd

@dataclass
class Minggu:

    minggu : str
    berat : List

@dataclass
class Peserta:
    
    name : str
    progress : List[Minggu]

if __name__ == '__main__':
    df = pd.read_csv('datasets/progress_phase1_no_NaN.csv', sep=',', thousands=' ')
    print(df.columns)