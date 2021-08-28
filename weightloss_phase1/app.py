import pandas as pd

import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.constants import BOTTOM

class DataSet:
    """ Choose dataset 

        0 : choose dataset with NaN values
        1 : choose dataset without NaN values
    
    """
    def __init__(self) -> DataFrame:
        self.df_with_nan = pd.read_csv('datasets/progress_phase1.csv', sep=',', thousands=' ')
        self.df_no_nan = pd.read_csv('datasets/progress_phase1_no_NaN.csv', sep=',', thousands=' ')

    def option(self, choice):
        if choice == 0:
            return self.df_with_nan
        elif choice == 1:
            return self.df_no_nan
        else:
            return f'{choice} is not a viable option, select 0 or 1'


class DatasetClassmethod:
    """ Choose dataset 

        implementation using classmethod

        0 : choose dataset with NaN values
        1 : choose dataset without NaN values
    
    """
    df_with_nan = pd.read_csv('datasets/progress_phase1.csv', sep=',', thousands=' ')
    df_no_nan = pd.read_csv('datasets/progress_phase1_no_NaN.csv', sep=',', thousands=' ')

    @classmethod
    def option(cls, choice : int):
        if choice == 0:
            return cls.df_with_nan
        elif choice == 1:
            return cls.df_no_nan
        else:
            return f'Option {choice} is not viable'

    @classmethod
    def all_name(cls, choice : int):
        if choice == 0:
            return cls.df_with_nan.columns
        elif choice == 1:
            return cls.df_no_nan.columns
        else:
            return f'Option {choice} is not viable'


class AllNameController:
    """ Aggregate name into list 
    
        return name for selection
    
    """
    @classmethod
    def all_name(cls, option):
        return DatasetClassmethod().all_name(option).columns


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
            plt.savefig('output/' + self.name + '.png')
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


class ViewTkinter(tk.Frame):
    def __init__(self, master):
        self.master = master
        master.title("Together - Weightloss Program")

        self.label = tk.Label(master, text="Cipta graf")
        # self.label.grid(column = 3, padx = 10, pady = 25)
        self.label.pack(fill='x', padx=5, pady=5)

        self.greet_button = tk.Button(master, text="Greet", command=self.greet)
        # self.greet_button.grid(column = 3, padx = 10, pady = 25)
        self.greet_button.pack(padx=5, pady=5)

        self.participant_select_label = ttk.Label(
            master, 
            text = "Pilih peserta :",
            font = ("Times New Roman", 10))
        self.participant_select_label.pack(padx=5, pady=5)

        # Combobox creation
        n = tk.StringVar()
        self.participant_choosen = ttk.Combobox(master, width = 27, textvariable = n)
  
        # Adding combobox drop down list
        self.participant_choosen['values'] = AllNameController().all_name(0)
        
        # self.country_choosen.grid(column = 1, row = 5)
        self.participant_choosen.pack(padx=5, pady=5)
        self.participant_choosen.current()
        self.participant_choosen.bind('<<ComboboxSelected>>', self.participant_data)

        self.close_button = tk.Button(master, text="Close", bg='red', fg='white', command=master.quit)
        # self.close_button.grid(column = 3, padx = 10, pady = 25)
        self.close_button.pack(padx=5, pady=5, side=BOTTOM)

    def participant_data(self, event):
        pass
        # chosen_country = self.country_choosen['values'][self.country_choosen.current()]
        # data = StuntedGrowthData(chosen_country).output_data()
        # messagebox.showinfo(title='Kids growth of selected country', message=data)

    def greet(self):
        print("Greetings!")


if __name__ == '__main__':
    # print(df_progress.columns)

    w_NaN_dataset = DataSet().option(0)
    wout_NaN_dataset = DataSet().option(1)

    """class method datasource, plot all individual graph """ 
    # NaN_data = DatasetClassmethod().option(0)
    # wo_NaN_data = DatasetClassmethod().option(1)

    # for person in ['Abe Kamil', 'Abe Isey', 'Kak Dayah', 'Kak Teh', 'Adz', 'Auni', 'Anis']:
    #     print(IndividualProgressChart(person, wo_NaN_data).output_graph())

    # print(AllProgressChart(NaN_data).output_together_graph())


    """ View using tkinter """
    root = tk.Tk()
    ViewTkinter(root)