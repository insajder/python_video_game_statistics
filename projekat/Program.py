from tkinter import *
from Unos import *
from PokretanjeUpita import *
from PokretanjePogleda import *
from PokretanjeSP import *

ws = Tk()
ws.title('Statistika Dota2')
ws.geometry('500x500')
ws['bg'] = '#1E2F97'
ws.option_add('*Font', 25)

def unos_i_azuriranje():
    UnosAzuriranjeOkvir()

def pokretanje_upita():
    PokretanjeUpitaOkvir()

def pokretanje_pogleda():
    PokretanjePogledaOkvir()

def pokretanje_sp():
    PokretanjeSPOkvir()

naslov = Label(ws, text='Statistika video igre DOTA2', bg='#1E2F97', fg='white')
naslov.pack(pady=(10, 50))

btnUnos = Button(ws, text='UNOS I AZURIRANJE PODATAKA', width=30, command=unos_i_azuriranje)
btnUnos.pack(pady=(10, 10))

btnUpiti = Button(ws, text='POKRETANJE UPITA', width=30, command=pokretanje_upita)
btnUpiti.pack(pady=(10, 10))

btnPogledi = Button(ws, text='POKRETANJE POGLEDA', width=30, command=pokretanje_pogleda)
btnPogledi.pack(pady=(10, 10))

btnSP = Button(ws, text='POKRETANJE SP', width=30, command=pokretanje_sp)
btnSP.pack(pady=(10, 10))

ws.mainloop()
