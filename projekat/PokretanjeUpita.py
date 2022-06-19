from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Upiti import *

def PokretanjeUpitaOkvir():
    root = Tk()
    root.geometry('1200x600')

    root.title("POKRETANJE UPITA")
    tabControl = ttk.Notebook(root)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tab6 = ttk.Frame(tabControl)

    def heroji():
        naslov = Label(tab1, text="Prikaz svih heroja po sposobnosti")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        frame = Frame(tab1)
        frame.pack(pady=20)

        # labels
        spos = Label(frame, text="Izabrati sposobnost za pretragu", pady=10)
        spos.grid(row=0, column=0)

        # Entry boxes
        varSpos = StringVar()
        sposobnost = ttk.Combobox(frame, textvariable=varSpos, state='readonly')
        sposobnost.grid(row=1, column=0, pady=10)

        lstSpos = lstSposobnosti()
        strLst = []
        for i in lstSpos:
            strLst.append(i[1])
        sposobnost['values'] = strLst


        game_frame = Frame(tab1)
        game_frame.pack()

        # scrollbar
        game_scroll = Scrollbar(game_frame)


        my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set)

        game_scroll.config(command=my_game.yview)

        # define our column

        my_game['columns'] = ('id_heroja', 'naziv_sposobnost', 'naziv', 'zdravlje', 'mana', 'steta', 'opseg', 'oklop', 'brzina')

        # format our column
        my_game.column("#0", width=0, stretch=NO)
        my_game.column("id_heroja", anchor=CENTER, width=80)
        my_game.column("naziv_sposobnost", anchor=CENTER, width=80)
        my_game.column("naziv", anchor=CENTER, width=80)
        my_game.column("zdravlje", anchor=CENTER, width=80)
        my_game.column("mana", anchor=CENTER, width=80)
        my_game.column("steta", anchor=CENTER, width=80)
        my_game.column("opseg", anchor=CENTER, width=80)
        my_game.column("oklop", anchor=CENTER, width=80)
        my_game.column("brzina", anchor=CENTER, width=80)

        # Create Headings
        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("id_heroja", text="Id", anchor=CENTER)
        my_game.heading("naziv_sposobnost", text="Sposobnost", anchor=CENTER)
        my_game.heading("naziv", text="Naziv", anchor=CENTER)
        my_game.heading("zdravlje", text="Zdravlje", anchor=CENTER)
        my_game.heading("mana", text="Mana", anchor=CENTER)
        my_game.heading("steta", text="Steta", anchor=CENTER)
        my_game.heading("opseg", text="Opseg", anchor=CENTER)
        my_game.heading("oklop", text="Oklop", anchor=CENTER)
        my_game.heading("brzina", text="Brzina", anchor=CENTER)

        # add data
        def osveziTabelu():
            game_scroll.pack(side=RIGHT, fill=Y)
            my_game.delete(*my_game.get_children())

            lst = lstHerojSposobnost(sposobnost.get())
            for i in lst:
                my_game.insert(parent='', index='end', text='',
                            values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
            my_game.pack()

        btn = Button(frame, text='Pretrazi', command=osveziTabelu)
        btn.grid(row=2, column=0)

    def predmeti():
        naslov = Label(tab2, text="Prikaz svih predmeta po statusu")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        frame = Frame(tab2)
        frame.pack(pady=20)

        # labels
        spos = Label(frame, text="Izabrati status za pretragu")
        spos.grid(row=0, column=0, pady=10)

        # Entry boxes
        varStatus = StringVar()
        status = ttk.Combobox(frame, textvariable=varStatus, state='readonly')
        status.grid(row=1, column=0, pady=10)

        strLst = ['aktivna', 'pasivna']
        status['values'] = strLst


        game_frame = Frame(tab2)
        game_frame.pack()

        # scrollbar
        game_scroll = Scrollbar(game_frame)

        my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set)

        game_scroll.config(command=my_game.yview)

        # define our column

        my_game['columns'] = ('id_predmeta', 'naziv', 'status', 'cena', 'zdravlje', 'mana', 'steta', 'opseg', 'oklop', 'brzina')

        # format our column
        my_game.column("#0", width=0, stretch=NO)
        my_game.column("id_predmeta", anchor=CENTER, width=80)
        my_game.column("naziv", anchor=CENTER, width=80)
        my_game.column("status", anchor=CENTER, width=80)
        my_game.column("cena", anchor=CENTER, width=80)
        my_game.column("zdravlje", anchor=CENTER, width=80)
        my_game.column("mana", anchor=CENTER, width=80)
        my_game.column("steta", anchor=CENTER, width=80)
        my_game.column("opseg", anchor=CENTER, width=80)
        my_game.column("oklop", anchor=CENTER, width=80)
        my_game.column("brzina", anchor=CENTER, width=80)

        # Create Headings
        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("id_predmeta", text="Id", anchor=CENTER)
        my_game.heading("naziv", text="Naziv", anchor=CENTER)
        my_game.heading("status", text="Status", anchor=CENTER)
        my_game.heading("cena", text="Cena", anchor=CENTER)
        my_game.heading("zdravlje", text="Zdravlje", anchor=CENTER)
        my_game.heading("mana", text="Mana", anchor=CENTER)
        my_game.heading("steta", text="Steta", anchor=CENTER)
        my_game.heading("opseg", text="Opseg", anchor=CENTER)
        my_game.heading("oklop", text="Oklop", anchor=CENTER)
        my_game.heading("brzina", text="Brzina", anchor=CENTER)

        # add data
        def osveziTabelu():
            game_scroll.pack(side=RIGHT, fill=Y)

            my_game.delete(*my_game.get_children())

            lst = lstPredmetStatus(status.get())
            for i in lst:
                my_game.insert(parent='', index='end', text='',
                            values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
            my_game.pack()

        btn = Button(frame, text='Pretrazi', command=osveziTabelu)
        btn.grid(row=2, column=0)

    def igraci():
        naslov = Label(tab3, text="Prikaz svih igraca")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        frame = Frame(tab3)
        frame.pack(pady=20)

        # labels
        lab = Label(frame, text="Izabrati filter za sortiranje")
        lab.grid(row=0, column=0, pady=10)

        game_frame = Frame(tab3)
        game_frame.pack()

        # scrollbar
        game_scroll = Scrollbar(game_frame)

        my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set)

        game_scroll.config(command=my_game.yview)

        # define our column

        my_game['columns'] = ('id_igraca', 'ime', 'rank', 'ukupno_meceva', 'ukupno_sati', 'pobeda')

        # format our column
        my_game.column("#0", width=0, stretch=NO)
        my_game.column("id_igraca", anchor=CENTER, width=80)
        my_game.column("ime", anchor=CENTER, width=80)
        my_game.column("rank", anchor=CENTER, width=80)
        my_game.column("ukupno_meceva", anchor=CENTER, width=80)
        my_game.column("ukupno_sati", anchor=CENTER, width=80)
        my_game.column("pobeda", anchor=CENTER, width=80)

        # Create Headings
        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("id_igraca", text="Id", anchor=CENTER)
        my_game.heading("ime", text="Ime", anchor=CENTER)
        my_game.heading("rank", text="Rank", anchor=CENTER)
        my_game.heading("ukupno_meceva", text="Ukupno meceva", anchor=CENTER)
        my_game.heading("ukupno_sati", text="Ukupno sati", anchor=CENTER)
        my_game.heading("pobeda", text="Ukupno pobeda", anchor=CENTER)

        # add data
        def osveziTabelu():
            game_scroll.pack(side=RIGHT, fill=Y)
            my_game.delete(*my_game.get_children())

            lst = lstSvihIgraca()
            for i in lst:
                my_game.insert(parent='', index='end', text='',
                            values=(i[0], i[1], i[2], i[3], i[4], i[5]))
            my_game.pack()
        osveziTabelu()

        def sortirajIgrace():
            game_scroll.pack(side=RIGHT, fill=Y)
            my_game.delete(*my_game.get_children())

            lst = ()
            if sort.get().__contains__('Sortiraj po ranku rastuce'):
                lst = lstSvihIgracaSortRankRastuce()
            elif sort.get().__contains__('Sortiraj po ranku opadajuce'):
                lst = lstSvihIgracaSortRankOpadajuce()
            elif sort.get().__contains__('Sortiraj po broju odigranih sati ukupno opadajuce'):
                lst = lstSvihIgracaSortSatiOpadajuce()
            else:
                lst = lstSvihIgraca()
            for i in lst:
                my_game.insert(parent='', index='end', text='',
                               values=(i[0], i[1], i[2], i[3], i[4], i[5]))
            my_game.pack()

        varSort = StringVar()
        sort = ttk.Combobox(frame, textvariable=varSort, state='readonly', width=50)
        sort.grid(row=1, column=0, pady=10)

        strLst = ['Sortiraj po ranku rastuce', 'Sortiraj po ranku opadajuce', 'Sortiraj po broju odigranih sati ukupno opadajuce']
        sort['values'] = strLst

        btn = Button(frame, text='Pretrazi', command=sortirajIgrace)
        btn.grid(row=2, column=0)

    def mecevi():
        naslov = Label(tab4, text="Prikaz svih odigranih meceva")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        frame = Frame(tab4)
        frame.pack(pady=20)

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
        my_game.heading("strana", text="Strana pobede", anchor=CENTER)

        # add data
        def osveziTabelu():
            game_scroll.pack(side=RIGHT, fill=Y)
            my_game.delete(*my_game.get_children())

            lst = lstMeceva()
            for i in lst:
                my_game.insert(parent='', index='end', text='',
                            values=(i[0], i[1], i[2], i[3]))
            my_game.pack()
        osveziTabelu()

        # btn = Button(frame, text='Pretrazi', command=osveziTabelu)
        # btn.grid(row=2, column=0)

    def herojiUspesnost():
        naslov = Label(tab5, text="Prikaz svih heroja po uspesnosti")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        frame = Frame(tab5)
        frame.pack(pady=20)

        game_frame = Frame(tab5)
        game_frame.pack()

        # scrollbar
        game_scroll = Scrollbar(game_frame)

        my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set)

        game_scroll.config(command=my_game.yview)

        # define our column

        my_game['columns'] = ('naziv', 'ukupno_odigranih', 'pobede')

        # format our column
        my_game.column("#0", width=0, stretch=NO)
        my_game.column("naziv", anchor=CENTER, width=80)
        my_game.column("ukupno_odigranih", anchor=CENTER, width=80)
        my_game.column("pobede", anchor=CENTER, width=80)

        # Create Headings
        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("naziv", text="Naziv", anchor=CENTER)
        my_game.heading("ukupno_odigranih", text="Ukupno odigranih meceva", anchor=CENTER)
        my_game.heading("pobede", text="Ukupno pobeda", anchor=CENTER)

        # add data
        def osveziTabelu():
            game_scroll.pack(side=RIGHT, fill=Y)
            my_game.delete(*my_game.get_children())

            lst = lstHerojUspesnost()
            for i in lst:
                my_game.insert(parent='', index='end', text='',
                            values=(i[0], i[1], i[2]))
            my_game.pack()
        osveziTabelu()

        # btn = Button(frame, text='Pretrazi', command=osveziTabelu)
        # btn.grid(row=2, column=0)

    def predmetiIskoriscenost():
        naslov = Label(tab6, text="Prikaz svih predmeta po iskoriscenosti")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        frame = Frame(tab6)
        frame.pack(pady=20)

        game_frame = Frame(tab6)
        game_frame.pack()

        # scrollbar
        game_scroll = Scrollbar(game_frame)

        my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set)

        game_scroll.config(command=my_game.yview)

        # define our column

        my_game['columns'] = ('naziv', 'status', 'cena', 'iskoriscenost')

        # format our column
        my_game.column("#0", width=0, stretch=NO)
        my_game.column("naziv", anchor=CENTER, width=80)
        my_game.column("status", anchor=CENTER, width=80)
        my_game.column("cena", anchor=CENTER, width=80)
        my_game.column("iskoriscenost", anchor=CENTER, width=80)

        # Create Headings
        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("naziv", text="Naziv", anchor=CENTER)
        my_game.heading("status", text="Status", anchor=CENTER)
        my_game.heading("cena", text="Cena", anchor=CENTER)
        my_game.heading("iskoriscenost", text="Iskoriscenost", anchor=CENTER)

        # add data
        def osveziTabelu():
            game_scroll.pack(side=RIGHT, fill=Y)
            my_game.delete(*my_game.get_children())

            lst = lstPredmetIskoriscenost()
            for i in lst:
                my_game.insert(parent='', index='end', text='',
                            values=(i[0], i[1], i[2], i[3]))
            my_game.pack()
        osveziTabelu()

        # btn = Button(frame, text='Pretrazi', command=osveziTabelu)
        # btn.grid(row=2, column=0)

    heroji()
    predmeti()
    herojiUspesnost()
    predmetiIskoriscenost()
    mecevi()
    igraci()

    tabControl.add(tab1, text='    Heroji   ')
    tabControl.add(tab2, text='    Predmeti    ')
    tabControl.add(tab3, text='    Igraci   ')
    tabControl.add(tab4, text='    Mecevi   ')
    tabControl.add(tab5, text='    Uspesnost heroja    ')
    tabControl.add(tab6, text='    Iskoriscenost predmeta   ')
    tabControl.pack(expand=1, fill="both")

    root.mainloop()
    return root
