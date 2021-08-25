import pandas as pd

import matplotlib.pyplot as plt

class IndividualProgressChart:
    def __init__(self, name : str):
        self.name = name
        self.df = pd.read_csv('datasets/progress_phase1_no_NaN.csv', sep=',', thousands=' ')

    # df_progress[['Minggu', 'Abe Kamil', 'Abe Isey', 'Kak Dayah', 'Kak Teh', 'Adz', 'Auni', 'Anis']].apply(pd.to_numeric, errors='coerce')

    """ Graf bagi setiap peserta """
    def output_graph(self):
        if self.name in self.df.columns[1:]:
            col_individu = self.df[self.name]
            col_minggu = self.df['Minggu']
            new_df = pd.DataFrame(list(zip(col_minggu, col_individu)), columns=['Minggu', self.name])
            new_df.plot(x ='Minggu', y=self.name, kind = 'line')
            plt.savefig('output/' + self.name + '.png')
            return f'Graph for {self.name} done'
        else:
            return f'No {self.name}'

class AllProgressChart:
    def __init__(self):
        self.df = pd.read_csv('datasets/progress_phase1_no_NaN.csv', sep=',', thousands=' ')

    """ Graf bagi setiap peserta """
    def output_together_graph(self):
        # self.df.set_index('Minggu')
        new_df = pd.DataFrame(
            data=self.df, 
            columns=['Minggu', 'Abe Kamil', 'Abe Isey', 'Kak Dayah', 'Kak Teh', 'Adz', 'Auni', 'Anis'])
        
        new_df.plot(
            x ='Minggu', 
            y=['Abe Kamil', 'Abe Isey', 'Kak Dayah', 'Kak Teh', 'Adz', 'Auni', 'Anis'], 
            kind = 'line',
            figsize = (10, 15),
            grid = True)
        
        plt.savefig('output/semua.png')
        
        return f'Graph for semua done'

if __name__ == '__main__':
    # print(df_progress.columns)

    for person in ['Abe Kamil', 'Abe Isey', 'Kak Dayah', 'Kak Teh', 'Adz', 'Auni', 'Anis']:
        print(IndividualProgressChart(person).output_graph())

    print(AllProgressChart().output_together_graph())