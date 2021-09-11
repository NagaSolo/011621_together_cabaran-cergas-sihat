from dataclasses import dataclass
from typing import List

import pandas as pd

import matplotlib.pyplot as plt

@dataclass
class Peserta:
    
    name : str
    progress : List

    def plot(self):
        plt.plot(self.progress, color='magenta', marker='o',mfc='pink') #plot the data
        plt.xticks(range(0,len(self.progress)+1, 1)) #set the tick frequency on x-axis

        plt.ylabel('KG') #set the label for y axis
        plt.xlabel('Minggu') #set the label for x-axis
        plt.title(f"Perkembangan Berat {self.name}") #set the title of the graph
        plt.show() #display the graph

if __name__ == '__main__':
    peserta_peserta = []

    df = pd.read_csv('datasets/progress_phase1_no_NaN.csv', sep=',', thousands=' ')
    
    # print(df['Adz'].values.tolist())
    for n in df.columns[1:]:
        peserta_dan_progress = df[n]
        peserta_peserta.append(Peserta(n, peserta_dan_progress.values.tolist()))
        
    print(peserta_peserta)

    fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(len(peserta_peserta))
    fig.suptitle('Perkembangan berat peserta-peserta')
    ax1.plot(
        peserta_peserta[0].progress, 
        color='magenta', marker='o',mfc='pink',
        label=f'{peserta_peserta[0].name}')

    ax2.plot(
        peserta_peserta[1].progress, 
        color='magenta', marker='o',mfc='pink',
        label=f'{peserta_peserta[1].name}')

    ax3.plot(
        peserta_peserta[2].progress, 
        color='magenta', marker='o',mfc='pink',
        label=f'{peserta_peserta[2].name}')

    ax4.plot(
        peserta_peserta[3].progress, 
        color='magenta', marker='o',mfc='pink',
        label=f'{peserta_peserta[3].name}')

    ax5.plot(
        peserta_peserta[4].progress, 
        color='magenta', marker='o',mfc='pink',
        label=f'{peserta_peserta[4].name}')

    ax6.plot(
        peserta_peserta[5].progress, 
        color='magenta', marker='o',mfc='pink',
        label=f'{peserta_peserta[5].name}')

    ax7.plot(
        peserta_peserta[6].progress, 
        color='magenta', marker='o',mfc='pink',
        label=f'{peserta_peserta[6].name}')

    plt.show()