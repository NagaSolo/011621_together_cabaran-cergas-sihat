from os import error

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
        try:
            if choice == 0:
                cls.df_chosen = cls.df_with_nan
                return cls.df_chosen
            elif choice == 1:
                cls.df_chosen = cls.df_no_nan
                return cls.df_chosen
        except error as e:
            return f'Option {choice} is not viable: {e}'

    @classmethod
    def all_name(cls, choice : int):
        if choice == 0:
            return cls.df_with_nan.columns.values.tolist()
        elif choice == 1:
            return cls.df_no_nan.columns.values.tolist()
        else:
            return f'Non df is chosen'


class DataSetController:
    """ Aggregate name into list 
    
        return name for selection
    
    """
    df = DatasetClassmethod().option(1)
    df_all_name = DatasetClassmethod().all_name(1)

    @classmethod
    def all_data(cls):
        return cls.df

    @classmethod
    def all_name(cls):
        return cls.df_all_name[1:]
    
    @classmethod
    def plot_individual(cls, name):
        if name in cls.all_name():
            figure2 = plt.Figure(figsize=(5,4), dpi=100)
            ax2 = figure2.add_subplot(111)
            line2 = FigureCanvasTkAgg(figure2, root)
            line2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
            col_individu = cls.df[name]
            col_minggu = cls.df['Minggu']
            new_df = pd.DataFrame(list(zip(col_minggu, col_individu)), columns=['Minggu', name])
            new_df.plot(x ='Minggu', y=name, kind = 'line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
            ax2.set_title(f'{name} Progress')
        else:
            return f'No {name}'


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
        self.participant_choosen['values'] = DataSetController.all_name()
        
        # self.country_choosen.grid(column = 1, row = 5)
        self.participant_choosen.pack(padx=5, pady=5)
        self.participant_choosen.current()
        self.participant_choosen.bind('<<ComboboxSelected>>', self.participant_data)

        self.close_button = tk.Button(master, text="Close", bg='red', fg='white', command=master.quit)
        # self.close_button.grid(column = 3, padx = 10, pady = 25)
        self.close_button.pack(padx=5, pady=5, side=BOTTOM)

    def participant_data(self, event):
        chosen_participant = self.participant_choosen['values'][self.participant_choosen.current()]
        DataSetController().plot_individual(chosen_participant)

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