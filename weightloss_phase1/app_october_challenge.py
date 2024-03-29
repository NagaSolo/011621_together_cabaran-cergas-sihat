from dataclasses import dataclass
from typing import List

import pandas as pd

import matplotlib.pyplot as plt

@dataclass
class Peserta:
    
    name : str
    progress : List

    def plot(self):
        
        # plot the data
        plt.plot(self.progress, color='magenta', marker='o',mfc='pink')
        
        # set the tick frequency on x-axis
        plt.xticks(range(0,len(self.progress)+1, 1))

        # set the label for y axis
        plt.ylabel('KG')
        
        # set the label for x-axis
        plt.xlabel('Minggu')
        
        # set the title of the graph
        plt.title(f"Perkembangan Berat {self.name}") 
        
        # display the graph
        plt.show()

@dataclass
class PesertaPeserta:

    peserta_peserta : List[Peserta]
    
    def plot_all(self):
        
        for p in self.peserta_peserta:
            plt.plot(p.progress, color='magenta', marker='o',mfc='pink')

        plt.title('Perkembangan Berat Peserta')
        plt.xlabel('Minggu')
        plt.ylabel('Kilogram')
        plt.legend([p.name for p in self.peserta_peserta])
        plt.show()


if __name__ == '__main__':
    peserta_peserta = []

    df = pd.read_csv('datasets/october_fat_rain_down_challenge.csv', sep=',', thousands=' ')
    
    # print(df['Adz'].values.tolist())
    for n in df.columns[1:]:
        peserta_dan_progress = df[n]
        peserta_peserta.append(Peserta(n, peserta_dan_progress.values.tolist()))
        
    semua_peserta = PesertaPeserta(peserta_peserta=peserta_peserta)
    semua_peserta.plot_all()