import pandas as pd
from pandas.core.frame import DataFrame

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.constants import BOTTOM


class DatasetClassmethod:
    """ Choose dataset 

        implementation using classmethod

        0 : choose dataset with NaN values
        1 : choose dataset without NaN values
    
    """
    
    df_with_nan = pd.read_csv('datasets/progress_phase1.csv', sep=',', thousands=' ')
    df_no_nan = pd.read_csv('datasets/progress_phase1_no_NaN.csv', sep=',', thousands=' ')
    df_chosen = None

    @classmethod
    def option(cls, choice : int):
        if choice == 0:
            df_chosen = cls.df_with_nan
            return df_chosen
        elif choice == 1:
            df_chosen = cls.df_no_nan
            return df_chosen
        else:
            return f'Option {choice} is not viable'

    @classmethod
    def all_name(cls):
        if cls.df_chosen is None:
            return f'Non df is chosen'
        else:
            return cls.df_chosen.values.tolist()


class DataSetController:
    """ Aggregate name into list 
    
        return name for selection
    
    """
    df = DatasetClassmethod().option(1)

    @classmethod
    def all_data(cls):
        return cls.df

    @classmethod
    def all_name(cls):
        return cls.df.all_name()[1:]
    
    @classmethod
    def plot_individual(cls, name):
        if name in cls.all_data():
            col_individu = cls.df[cls.name]
            col_minggu = cls.df['Minggu']
            new_df = pd.DataFrame(list(zip(col_minggu, col_individu)), columns=['Minggu', cls.name])
            new_df.plot(x ='Minggu', y=cls.name, kind = 'line')
            plt.savefig('output/' + cls.name + '.png')
            return f'Graph for {cls.name} done'
        else:
            return f'No {cls.name}'



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
        all_name = DataSetController()
        self.participant_choosen['values'] = all_name.all_name()
        
        # self.country_choosen.grid(column = 1, row = 5)
        self.participant_choosen.pack(padx=5, pady=5)
        self.participant_choosen.current()
        self.participant_choosen.bind('<<ComboboxSelected>>', self.participant_data)

        self.close_button = tk.Button(master, text="Close", bg='red', fg='white', command=master.quit)
        # self.close_button.grid(column = 3, padx = 10, pady = 25)
        self.close_button.pack(padx=5, pady=5, side=BOTTOM)

    def participant_data(self, event):
        DataSetController().plot_individual(self.participant_choosen.current())
        # figure2 = plt.Figure(figsize=(5,4), dpi=100)
        # ax2 = figure2.add_subplot(111)
        # line2 = FigureCanvasTkAgg(figure2, root)
        # line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        # df2 = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
        # df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
        # ax2.set_title('Year Vs. Unemployment Rate')

    def greet(self):
        print("Greetings!")


if __name__ == '__main__':

    """ View using tkinter """
    root = tk.Tk()
    ViewTkinter(root)

    # set frame geometry
    root.geometry('500x250')

    # show window
    root.mainloop()