import pandas as pd
import numpy as np
import requests
import csv 
import matplotlib.pyplot as plt 
import seaborn as sns 
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap
from soccerplots.radar_chart import Radar

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
            c.execute('''CREATE TABLE IF NOT EXISTS podaci (Team text, Tournament text, Goals integer, Shots pg integer, yellow_cards integer, red_card integer, Possession integer, Pass integer, AerialsWon integer, Rating integer)''')
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



url='http://127.0.0.1:5000//pocetna_csv'
r=requests.get(url)
url2='http://127.0.0.1:5000//pocetna_json'
r2=requests.get(url2)
#url_for('static', filename='novo.csv')
#df=pd.read_csv(csvLoader.reader(r.content.decode('utf-8').splitlines(), delimiter=','))
sadrzaj = csv.reader(r.content.decode('utf-8').splitlines(), delimiter=',')
lista = list(sadrzaj)
#podaci=pd.DataFrame(lista, columns=lista["Team", "Tournament", "Goals", "Shots pg", "yellow_cards", "red_card", "Possession%", "Pass%", "AerialsWon", "Rating"])
create_connection()
select_data()
print(r2.content.decode('utf-8').splitlines())



