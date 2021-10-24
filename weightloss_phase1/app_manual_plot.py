import pandas as pd
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt

class DataSet:
    """ Choose dataset 

        0 : choose dataset with NaN values
        1 : choose dataset without NaN values
    
    """
    def __init__(self) -> DataFrame:
        self.df_with_nan = pd.read_csv('datasets/progress_phase1.csv', sep=',', thousands=' ')
        self.df_no_nan = pd.read_csv('datasets/progress_phase1_no_NaN.csv', sep=',', thousands=' ')
        self.df_octo = pd.read_csv('datasets/october_fat_rain_down_challenge_row.csv', sep=',', thousands=' ')

    def option(self, choice):
        if choice == 0:
            return self.df_with_nan
        elif choice == 1:
            return self.df_no_nan
        elif choice == 2:
            return self.df_octo
        else:
            return f'{choice} is not a viable option, select 0 or 1 or 2'

class IndividualProgressChart:
    """ Plot individual data """
    def __init__(self, name : str, df : DataSet):
        self.name = name
        self.df = df

    """ Graf bagi setiap peserta """
    def output_graph(self):
        if self.name in self.df.columns[1:]:
            col_individu = self.df[self.name]
            col_minggu = self.df['Minggu']
            new_df = pd.DataFrame(list(zip(col_minggu, col_individu)), columns=['Minggu', self.name])
            new_df.plot(x ='Minggu', y=self.name, kind = 'line')
            plt.savefig('output_october/' + self.name + '.png')
            return f'Graph for {self.name} done'
        else:
            return f'No {self.name}'

class AllProgressChart:
    """ Plot all data together """
    def __init__(self, df : DataSet):
        self.df = df

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

    w_NaN_dataset = DataSet().option(0)
    wo_NaN_dataset = DataSet().option(1)
    octo_dataset = DataSet().option(2)

    """class method datasource, plot all individual graph, dataset without NaN """

    # for person in ['Abe Kamil', 'Abe Isey', 'Kak Dayah', 'Kak Teh', 'Adz', 'Auni', 'Anis']:
    #     print(IndividualProgressChart(person, wo_NaN_dataset).output_graph())

    # print(AllProgressChart(w_NaN_dataset).output_together_graph())

    for person in ['Kak Dayah', 'Abe Isey', 'Kak Teh', 'Auni', 'Anis']:
        print(IndividualProgressChart(person, octo_dataset).output_graph())

    print(AllProgressChart(octo_dataset).output_together_graph())