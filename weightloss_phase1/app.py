import pandas as pd

import matplotlib.pyplot as plt

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