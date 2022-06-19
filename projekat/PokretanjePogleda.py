import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Upiti import *
from Validacija import *

def PokretanjePogledaOkvir():
    root = Tk()
    root.geometry('1200x600')

    root.title("POKRETANJE POGLEDA")
    tabControl = ttk.Notebook(root)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)

    def igraci_rank():
        naslov = Label(tab1, text="Prikaz svih igraca po zadatom ranku")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        frame = Frame(tab1)
        frame.pack(pady=20)

        # labels
        spos = Label(frame, text="Unesite rank za pretragu")
        spos.grid(row=0, column=0, pady=10)

        # Entry boxes
        unos_rank = Entry(frame)
        unos_rank.grid(row=1, column=0, pady=10)

        game_frame = Frame(tab1)
        game_frame.pack()

        # scrollbar
        game_scroll = Scrollbar(game_frame)

        my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set)

        game_scroll.config(command=my_game.yview)

        # define our column

        my_game['columns'] = ('id_igraca', 'ime', 'rank', 'ukupno_meca', 'ukupno_pobeda', 'uk_ubistva', 'uk_asistencija', 'uk_smrti')

        # format our column
        my_game.column("#0", width=0, stretch=NO)
        my_game.column("id_igraca", anchor=CENTER, width=80)
        my_game.column("ime", anchor=CENTER, width=80)
        my_game.column("rank", anchor=CENTER, width=80)
        my_game.column("ukupno_meca", anchor=CENTER, width=80)
        my_game.column("ukupno_pobeda", anchor=CENTER, width=80)
        my_game.column("uk_ubistva", anchor=CENTER, width=80)
        my_game.column("uk_asistencija", anchor=CENTER, width=80)
        my_game.column("uk_smrti", anchor=CENTER, width=80)

        # Create Headings
        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("id_igraca", text="Id", anchor=CENTER)
        my_game.heading("ime", text="Ime", anchor=CENTER)
        my_game.heading("rank", text="Rank", anchor=CENTER)
        my_game.heading("ukupno_meca", text="Ukupno meca", anchor=CENTER)
        my_game.heading("ukupno_pobeda", text="Ukupno pobeda", anchor=CENTER)
        my_game.heading("uk_ubistva", text="Ubistva", anchor=CENTER)
        my_game.heading("uk_asistencija", text="Asistencije", anchor=CENTER)
        my_game.heading("uk_smrti", text="Smrti", anchor=CENTER)

        # add data
        def osveziTabelu():
            game_scroll.pack(side=RIGHT, fill=Y)
            my_game.delete(*my_game.get_children())

            if provera_unosa_broja(unos_rank.get()):
                lst = viewIgraciRank(unos_rank.get())
                for i in lst:
                    my_game.insert(parent='', index='end', text='',
                                values=(i[0], i[1], i[2], i[3], procenti(i[3], i[4]), i[5], i[6], i[7]))
            else:
                messagebox.showerror('Greska', 'Nepravilan unos')
            my_game.pack()

        btn = Button(frame, text='Pretrazi', command=osveziTabelu)
        btn.grid(row=2, column=0)

    def igrac_heroj():
        naslov = Label(tab2, text="Prikaz svih heroja za zadatog igraca")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        frame = Frame(tab2)
        frame.pack(pady=20)

        # labels
        lab = Label(frame, text="Unesite igraca za pretragu")
        lab.grid(row=0, column=0, pady=10)

        ime = Entry(frame)
        ime.grid(row=1, column=0, pady=10)

        game_frame = Frame(tab2)
        game_frame.pack()

        # scrollbar
        game_scroll = Scrollbar(game_frame)

        my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set)

        game_scroll.config(command=my_game.yview)

        # define our column

        my_game['columns'] = ('naziv', 'ukupno_partija', 'uk_pobeda')

        # format our column
        my_game.column("#0", width=0, stretch=NO)
        my_game.column("naziv", anchor=CENTER, width=80)
        my_game.column("ukupno_partija", anchor=CENTER, width=80)
        my_game.column("uk_pobeda", anchor=CENTER, width=80)

        # Create Headings
        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("naziv", text="Naziv", anchor=CENTER)
        my_game.heading("ukupno_partija", text="Ukupno odigranih meceva", anchor=CENTER)
        my_game.heading("uk_pobeda", text="Ukupno pobeda", anchor=CENTER)

        # add data
        def osveziTabelu():
            game_scroll.pack(side=RIGHT, fill=Y)
            my_game.delete(*my_game.get_children())

            lst = funIgracHeroj(ime.get())
            for i in lst:
                my_game.insert(parent='', index='end', text='',
                            values=(i[0], i[1], procenti(i[1], i[2])))
            my_game.pack()

        btn = Button(frame, text='Pretrazi', command=osveziTabelu)
        btn.grid(row=2, column=0)

    def igrac_mec():
        naslov = Label(tab3, text="Prikaz svih meceva za zadatog igraca")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        frame = Frame(tab3)
        frame.pack(pady=20)

        # labels
        lab = Label(frame, text="Unesite igraca za pretragu")
        lab.grid(row=0, column=0, pady=10)

        ime = Entry(frame)
        ime.grid(row=1, column=0, pady=10)

        game_frame = Frame(tab3)
        game_frame.pack()

        # scrollbar
        game_scroll = Scrollbar(game_frame)

        my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set)

        game_scroll.config(command=my_game.yview)

        # define our column

        my_game['columns'] = ('id_meca', 'datum', 'trajanje', 'naziv', 'strana', 'status', 'ubistva', 'asistencije', 'smrti')

        # format our column
        my_game.column("#0", width=0, stretch=NO)
        my_game.column("id_meca", anchor=CENTER, width=80)
        my_game.column("datum", anchor=CENTER, width=80)
        my_game.column("trajanje", anchor=CENTER, width=80)
        my_game.column("naziv", anchor=CENTER, width=80)
        my_game.column("strana", anchor=CENTER, width=80)
        my_game.column("status", anchor=CENTER, width=80)
        my_game.column("ubistva", anchor=CENTER, width=80)
        my_game.column("asistencije", anchor=CENTER, width=80)
        my_game.column("smrti", anchor=CENTER, width=80)

        # Create Headings
        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("id_meca", text="Id", anchor=CENTER)
        my_game.heading("datum", text="Datum", anchor=CENTER)
        my_game.heading("trajanje", text="Trajanje", anchor=CENTER)
        my_game.heading("naziv", text="Heroj", anchor=CENTER)
        my_game.heading("strana", text="Strana", anchor=CENTER)
        my_game.heading("status", text="Status", anchor=CENTER)
        my_game.heading("ubistva", text="Ubistva", anchor=CENTER)
        my_game.heading("asistencije", text="Asistencije", anchor=CENTER)
        my_game.heading("smrti", text="Smrti", anchor=CENTER)

        # add data
        def osveziTabelu():
            game_scroll.pack(side=RIGHT, fill=Y)
            my_game.delete(*my_game.get_children())

            lst = viewIgracMec(ime.get())
            for i in lst:
                my_game.insert(parent='', index='end', text='',
                            values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
            my_game.pack()

        btn = Button(frame, text='Pretrazi', command=osveziTabelu)
        btn.grid(row=2, column=0)

    def igrac_predmet():
        naslov = Label(tab4, text="Prikaz svih predmeta za zadatog igraca")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        frame = Frame(tab4)
        frame.pack(pady=20)

        # labels
        lab = Label(frame, text="Unesite igraca za pretragu")
        lab.grid(row=0, column=0, pady=10)

        ime = Entry(frame)
        ime.grid(row=1, column=0, pady=10)

        game_frame = Frame(tab4)
        game_frame.pack()

        # scrollbar
        game_scroll = Scrollbar(game_frame)

        my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set)

        game_scroll.config(command=my_game.yview)

        # define our column

        my_game['columns'] = ('naziv', 'iskoriscenost', 'pobeda')

        # format our column
        my_game.column("#0", width=0, stretch=NO)
        my_game.column("naziv", anchor=CENTER, width=80)
        my_game.column("iskoriscenost", anchor=CENTER, width=80)
        my_game.column("pobeda", anchor=CENTER, width=80)

        # Create Headings
        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("naziv", text="Naziv", anchor=CENTER)
        my_game.heading("iskoriscenost", text="Iskoriscenost", anchor=CENTER)
        my_game.heading("pobeda", text="Pobeda", anchor=CENTER)

        # add data
        def osveziTabelu():
            game_scroll.pack(side=RIGHT, fill=Y)
            my_game.delete(*my_game.get_children())

            lst = funIgracPredmet(ime.get())
            for i in lst:
                my_game.insert(parent='', index='end', text='',
                            values=(i[0], i[1], procenti(i[1], i[2])))
            my_game.pack()

        btn = Button(frame, text='Pretrazi', command=osveziTabelu)
        btn.grid(row=2, column=0)

    def igrac_ukupno():
        naslov = Label(tab5, text="Prikaz podataka za zadatog igraca")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        frame = Frame(tab5)
        frame.pack(pady=20)

        # labels
        lab = Label(frame, text="Unesite igraca za pretragu")
        lab.grid(row=0, column=0, pady=10)

        ime = Entry(frame)
        ime.grid(row=1, column=0, pady=10)

        game_frame = Frame(tab5)
        game_frame.pack()

        Label(frame, text='ID').grid(row=4, column=0, pady=5)
        Label(frame, text='IME').grid(row=5, column=0, pady=5)
        Label(frame, text='UKUPNO ODIGRANIH MECEVA').grid(row=6, column=0, pady=5)
        Label(frame, text='UKUPNO POBEDA').grid(row=7, column=0, pady=5)
        Label(frame, text='UKUPNO UBISTVA').grid(row=8, column=0, pady=5)
        Label(frame, text='UKUPNO ASISTENCIJA').grid(row=9, column=0, pady=5)
        Label(frame, text='UKUPNO SMRTI').grid(row=10, column=0, pady=5)
        Label(frame, text='NAJDUZI MEC').grid(row=11, column=0, pady=5)
        Label(frame, text='NAJVISE UBISTVA U TOKU JEDNE IGRE').grid(row=12, column=0, pady=5)
        Label(frame, text='NAJVISE ASISTENCIJA U TOKU JEDNE IGRE').grid(row=13, column=0, pady=5)
        Label(frame, text='NAJVISE SMRTI U TOKU JEDNE IGRE').grid(row=14, column=0, pady=5)
        def osveziTabelu():
            lst = viewIgracUkupno(ime.get())
            for i in lst:
                Label(frame, text=i[0]).grid(row=4, column=1)
                Label(frame, text=i[1]).grid(row=5, column=1)
                Label(frame, text=i[2]).grid(row=6, column=1)
                Label(frame, text=procenti(i[2], i[3])).grid(row=7, column=1)
                Label(frame, text=i[4]).grid(row=8, column=1)
                Label(frame, text=i[5]).grid(row=9, column=1)
                Label(frame, text=i[6]).grid(row=10, column=1)


            lst2 = viewIgracMax(ime.get())
            for i in lst2:
                Label(frame, text=i[0]).grid(row=11, column=1)
                Label(frame, text=i[1]).grid(row=12, column=1)
                Label(frame, text=i[2]).grid(row=13, column=1)
                Label(frame, text=i[3]).grid(row=14, column=1)

        btn = Button(frame, text='Pretrazi', command=osveziTabelu)
        btn.grid(row=2, column=0)

    igraci_rank()
    igrac_heroj()
    igrac_mec()
    igrac_predmet()
    igrac_ukupno()

    tabControl.add(tab1, text='    Rank    ')
    tabControl.add(tab2, text='    Heroj    ')
    tabControl.add(tab3, text='    Mec     ')
    tabControl.add(tab4, text='    Predmet     ')
    tabControl.add(tab5, text='    Igrac   ')
    tabControl.pack(expand=1, fill="both")

    root.mainloop()
    return root
