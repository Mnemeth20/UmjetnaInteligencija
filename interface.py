import tkinter as tk
import requests, json, csv, time, os
from tkinter import *
import matplotlib.pyplot as plt
from  matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import pandas as pd
import sqlite3
from sqlite3 import Error


def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('./database.db')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            c=conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS podaci (Team text, Tournament text, Goals real, Shots real, yellow_cards real, red_card real, Possession real, Pass real, AerialsWon real, Rating real)''')
            print("Uspjesno kreirana tablica")
   

def select_data():
    conn = None;
    try:
        conn = sqlite3.connect('./database.db')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            c=conn.cursor()
            c.execute('''SELECT * FROM podaci''')
            rows = c.fetchall()
            for row in rows:
                print(row)
            
    


colors_blue = ["#132C33", "#264D58", '#17869E', '#51C4D3', '#B4DBE9']
colors_dark = ["#1F1F1F", "#313131", '#636363', '#AEAEAE', '#DADADA']
colors_red = ["#331313", "#582626", '#9E1717', '#D35151', '#E9B4B4']
colors_mix = ["#17869E", '#264D58', '#179E66', '#D35151', '#E9DAB4', '#E9B4B4', '#D3B651', '#6351D3']
colors_div = ["#132C33", '#17869E', '#DADADA', '#D35151', '#331313']

options = [ 
    "Italy", 
    "England", 
] 

url='http://127.0.0.1:5000//pocetna_csv'
r=requests.get(url)
url2='http://127.0.0.1:5000//pocetna_json'
r2=requests.get(url2)
#print(r.content)
#print(r2.content)
sadrzaj = csv.reader(r.content.decode('utf-8').splitlines(), delimiter=',')
lista = list(sadrzaj)

helpData = pd.DataFrame(lista)


#england = pd.read_csv()
italy = pd.DataFrame(json.loads(r2.content.decode('utf-8')))
#italy2 = pd.read_json('./staro.json')
min_score_italy = italy.iloc[-1]
mean_score_italy = italy["Goals"].mean()

#mean_score_england = 51.5
epl_idx = list(italy.index + 1)
EngleskaLiga = helpData.drop(0)
#EngleskaLiga2 = helpData.rename(columns={0: "Team", "1": "Tournament", "2": "Goals", "3": "Shots pg", "4": "yellow_cards", "5": "red_card", "6": "Possession%", "7": "Pass%", "8": "AerialsWon", "9": "Rating"}, inplace=True)
EngleskaLiga.columns = ["Team", "Tournament", "Goals", "Shots", "yellow_cards", "red_card", "Possession%", "Pass%", "AerialsWon", "Rating"]
#print(r2.content)
mean_score_england = EngleskaLiga["Goals"].mean()
#print(italy)

def spremiUBazu():
    conn = None;
    try:
        conn = sqlite3.connect('./database.db')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            c=conn.cursor()
            testPrint = c.execute('''SELECT * FROM podaci''')
            EngleskaLiga.to_sql('podaci', conn, if_exists='replace', index=False)
            #time.sleep(10)
            italy.to_sql('podaci', conn, if_exists='replace', index=False)
            
            print(italy)
            #print(helpData)
            for index in helpData.drop(0).index:
                if(index == 0):
                    continue
                print("Timovi su ",helpData[0][index])
                #helpData2 = helpData.drop(0)
                #row = [helpData[0][index], helpData[1][index], helpData[2][index], helpData[3][index], helpData[4][index], helpData[5][index], helpData[6][index], helpData[7][index], helpData[8][index], helpData[9][index]]
                #print(row)
                #listaNova = list(row)
                #upit = "INSERT INTO podaci(Team, Tournament, Goals, Shots, yellow_cards, red_card, Possession, Pass, AerialsWon, Rating) VALUES ( " + helpData[0][index] + ", " + helpData[1][index] + ", " + helpData[2][index] + ", " + helpData[3][index] + ", " + helpData[4][index] + ", " + helpData[5][index] + ", " + helpData[6][index] + ", " + helpData[7][index] + ", " + helpData[8][index] + ", " + helpData[9][index] + ")"
                #c.execute(upit)
            #print(helpData[0][0])
            #for row in helpData.drop(0):
            #    print(helpData[row])

            #for row in EngleskaLiga:
            #    print(row)
                #c.execute('''INSERT INTO podaci(Team, Tournament, Goals, Shots, yellow_cards, red_card, Possession, Pass, AerialsWon, Rating) VALUES (?,?,?,?,?,?,?,?,?,?)''', row)
            italy.to_sql('podaci', conn, if_exists='replace', index=False)

class GUI(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.title("Golovi Engleske i Talijanske lige")
        #self.geometry("500x500")
        self.createWidgets()
        
        print(type(self))

        #for item in dir(self):
            #print(type(item),item)
    
    #def show(): 
    #    label.config( text = clicked.get() ) 
    def createWidgets(self):

        
        self.minsize(1500,1000)
        f0 = tk.Frame()
        #drop = OptionMenu( f0 , clicked , *options )
        
        fig , ax = plt.subplots()
        fig1, ax2 = plt.subplots()
        f0.grid()
        
        bar0 = ax.barh(EngleskaLiga['Team'], EngleskaLiga['Goals'].sort_values(ascending=False), color=colors_red[3], alpha=0.6, edgecolor=colors_dark[0])
        
        bar1 = ax2.barh(italy['Team'], italy['Goals'].sort_values(ascending=False), color=colors_blue[3], alpha=0.6, edgecolor=colors_dark[0])
        #bar2 = ax.barh(min_score_italy['Team'], min_score_italy['Goals'], color=colors_red[2], alpha=0.6, edgecolor=colors_dark[0])
        ax.legend(["Average Goal", "Best Team", "Other Teams" ,"Worst Team"], loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=5, borderpad=1, frameon=False, fontsize=12)
        ax.grid(axis='x', alpha=0.3)
        ax.set_axisbelow(True)
        ax.set_xlabel("Goals", fontsize=14, labelpad=10, fontweight='bold', color=colors_dark[0])
        ax.set_ylabel("Teams", fontsize=14, labelpad=10, fontweight='bold', color=colors_dark[0])
        ax2.legend(["Average Goal", "Best Team", "Other Teams" ,"Worst Team"], loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=5, borderpad=1, frameon=False, fontsize=12)
        ax2.grid(axis='x', alpha=0.3)
        ax2.set_axisbelow(True)
        ax2.set_xlabel("Goals", fontsize=14, labelpad=10, fontweight='bold', color=colors_dark[0])
        ax2.set_ylabel("Teams", fontsize=14, labelpad=10, fontweight='bold', color=colors_dark[0])
        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()
        clicked = StringVar()
        clicked.set( "Italy" ) 
        tk.Button(f0, text="Quit", command=self.destroy).pack()
        avgl  = ax.text(
            s="Avarage\nGoal: {:.2f}".format(mean_score_england),
            y=ymax-4,
            x=mean_score_england+1,
            backgroundcolor=colors_dark[2],
            fontsize=14,
            fontweight='bold',
            rotation=270,
            color='white'
            ) 
        avgw  = ax2.text(
            s="Avarage\nGoal: {:.2f}".format(mean_score_italy),
            y=ymax-4,
            x=mean_score_italy+1,
            backgroundcolor=colors_dark[2],
            fontsize=14,
            fontweight='bold',
            rotation=270,
            color='white'
            ) 
        canvas = FigureCanvasTkAgg(fig, f0)
        canvas1 = FigureCanvasTkAgg(fig1, f0)
        toolbar = NavigationToolbar2Tk(canvas, 
                                   f0) 
        toolbar.update() 
    
        canvas._tkcanvas.pack(fill=tk.BOTH, expand=1)
        canvas1._tkcanvas.pack(fill=tk.BOTH, expand=1)
        #OptionMenu( f0 , clicked , *options ).pack()
        f0.pack(fill='x', expand=1)

def main():
    
    appstart = GUI()
    
    create_connection()
    spremiUBazu()
    
    appstart.mainloop()
    os.remove('./database.db')
    appstart.destroy()
    

if __name__ == "__main__":
    main()

