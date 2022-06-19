import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Upiti import *
from Validacija import *

def PokretanjeSPOkvir():
    root = Tk()
    root.geometry('1200x600')

    root.title("POKRETANJE SP")
    tabControl = ttk.Notebook(root)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)

    def heroj_sposobnost():
        naslov = Label(tab1, text="Promeni sposobnost heroju")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        frame = Frame(tab1)
        frame.pack(pady=20)

        # labels
        lab1 = Label(frame, text="Izaberite heroja:")
        lab1.grid(row=0, column=0, pady=10)

        lab2 = Label(frame, text="Izaberite sposobnost:")
        lab2.grid(row=0, column=1, pady=10)

        varHeroji = StringVar()
        heroj = ttk.Combobox(frame, textvariable=varHeroji, state='readonly')
        heroj.grid(row=1, column=0, pady=10)

        lstHer = lstHeroja()
        strLst1 = []
        for i in lstHer:
            strLst1.append(i[1])
        heroj['values'] = strLst1

        varSpos = StringVar()
        sposobnost = ttk.Combobox(frame, textvariable=varSpos, state='readonly')
        sposobnost.grid(row=1, column=1, pady=10)

        lstSpos = lstSposobnosti()
        strLst = []
        for i in lstSpos:
            strLst.append(i[1])
        sposobnost['values'] = strLst

        game_frame = Frame(tab1)
        game_frame.pack()

        poruka_prikaz = Label(frame, text='')
        poruka_prikaz.grid(row=3, column=0, pady=10)
        poruka_prikaz.config(font=(18))

        # add data
        def promeniSposobnostHeroju():
            if (int(sposobnost.index("end")) != 0) and (int(sposobnost.index("end")) != 0):
                poruka = spHerojSposobnost(heroj.get(), sposobnost.get())
                poruka_prikaz.config(text=poruka)
            else:
                poruka_prikaz.config(text='')

        btn = Button(frame, text='Promeni', command=promeniSposobnostHeroju)
        btn.grid(row=2, column=0)

    def predmet_cena():
        naslov = Label(tab2, text="Promeni cenu zadatom predmeti")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        frame = Frame(tab2)
        frame.pack(pady=20)

        # labels
        lab1 = Label(frame, text="Unesite naziv predmeta:")
        lab1.grid(row=0, column=0, pady=10)

        lab2 = Label(frame, text="Unesite procenat:")
        lab2.grid(row=0, column=1, pady=10)

        naziv = Entry(frame)
        naziv.grid(row=1, column=0, pady=10)

        procenat = Entry(frame)
        procenat.grid(row=1, column=1, pady=10)

        game_frame = Frame(tab2)
        game_frame.pack()

        poruka_prikaz = Label(frame, text='')
        poruka_prikaz.grid(row=3, column=0, pady=10)
        poruka_prikaz.config(font=(18))

        def promeniCenu():
            if provera_unosa_tekst(naziv.get()) and provera_unosa_broja(procenat.get()):
                poruka = spPredmetCena(naziv.get(), procenat.get())
                poruka_prikaz.config(text=poruka)
            else:
                messagebox.showerror("Greska", 'Nepravilan unos')

        btn = Button(frame, text='Promeni', command=promeniCenu)
        btn.grid(row=2, column=0, pady=10)

    def igrac_mec():
        naslov = Label(tab3, text="Obrisi zadatog igraca ukoliko nema nijedan odigrani mec")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        frame = Frame(tab3)
        frame.pack(pady=20)

        # labels
        lab1 = Label(frame, text="Unesite ime igraca:")
        lab1.grid(row=0, column=0, pady=10)

        ime = Entry(frame)
        ime.grid(row=1, column=0, pady=10)

        game_frame = Frame(tab3)
        game_frame.pack()

        poruka_prikaz = Label(frame, text='')
        poruka_prikaz.grid(row=3, column=0)
        poruka_prikaz.config(font=(18))

        def obrisiIgraca():
            if provera_unosa_tekst(ime.get()):
                poruka = spIgracMecBrisanje(ime.get())
                poruka_prikaz.config(text=poruka)
            else:
                messagebox.showerror("Greska", 'Nepravilan unos')

        btn = Button(frame, text='Obrisi', command=obrisiIgraca)
        btn.grid(row=2, column=0)

    def mecevi_pobeda():
        naslov = Label(tab4, text="Kreiraj tabelu svih pobednickih meceva")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        frame = Frame(tab4)
        frame.pack(pady=20)

        # labels
        lab1 = Label(frame, text="Kreiranje table i prikaz")
        lab1.grid(row=0, column=0, pady=10)

        game_frame = Frame(tab4)
        game_frame.pack()

        poruka_prikaz = Label(frame, text='')
        poruka_prikaz.grid(row=3, column=0, pady=10)
        poruka_prikaz.config(font=(25))

        def kreirajTabelu():
            poruka = spKreiranjeTabele()
            poruka_prikaz.config(text=poruka)

            def tabela():
                game_frame = Frame(tab4)
                game_frame.pack()

                # scrollbar
                game_scroll = Scrollbar(game_frame)

                my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set)

                game_scroll.config(command=my_game.yview)

                # define our column

                my_game['columns'] = ('id_meca', 'datum', 'trajanje', 'strana')

                # format our column
                my_game.column("#0", width=0, stretch=NO)
                my_game.column("id_meca", anchor=CENTER, width=80)
                my_game.column("datum", anchor=CENTER, width=80)
                my_game.column("trajanje", anchor=CENTER, width=80)
                my_game.column("strana", anchor=CENTER, width=80)

                # Create Headings
                my_game.heading("#0", text="", anchor=CENTER)
                my_game.heading("id_meca", text="Id", anchor=CENTER)
                my_game.heading("datum", text="Datum", anchor=CENTER)
                my_game.heading("trajanje", text="Trajanje", anchor=CENTER)
                my_game.heading("strana", text="Pobednicka strana", anchor=CENTER)

                # add data
                def osveziTabelu():
                    game_scroll.pack(side=RIGHT, fill=Y)
                    my_game.delete(*my_game.get_children())

                    lst = lstSPMecevi()
                    for i in lst:
                        my_game.insert(parent='', index='end', text='',
                                       values=(i[0], i[1], i[2], i[3]))
                    my_game.pack()
                osveziTabelu()
            tabela()

        btn = Button(frame, text='Kreiraj', command=kreirajTabelu)
        btn.grid(row=1, column=0)

    heroj_sposobnost()
    predmet_cena()
    igrac_mec()
    mecevi_pobeda()

    tabControl.add(tab1, text='    Heroj    ')
    tabControl.add(tab2, text='    Predmet    ')
    tabControl.add(tab3, text='    Igrac     ')
    tabControl.add(tab4, text='    Pobede    ')
    tabControl.pack(expand=1, fill="both")

    root.mainloop()
    return root
