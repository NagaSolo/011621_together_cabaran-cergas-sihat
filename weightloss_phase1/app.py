import pandas as pd

import matplotlib.pyplot as plt

import tkinter as tk

class Window:
    def __init__(self, root, title, geometry, message):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        tk.Label(self.root, message).pack()

def main():
    root = tk()
    windows1 = Window(root, 'Example', '300x300', 'Window 1 From class Window')


df_progress = pd.read_csv(
    'datasets/progress_phase1.csv', 
    sep=',', 
    thousands=' ')

df_progress[['Minggu', 'Abe Kamil', 'Abe Isey', 'Kak Dayah', 'Kak Teh', 'Adz', 'Auni', 'Anis']].apply(pd.to_numeric, errors='coerce')

""" Graf bagi setiap peserta """
def output_graph(name):
    df_progress.plot(x ='Minggu', y=name, kind = 'line')
    plt.savefig('output/' + name + '.png')
    return f'Graph for {name} done'

if __name__ == '__main__':
    # print(df_progress.columns)

    for person in df_progress.columns[1:]:
        output_graph(person)