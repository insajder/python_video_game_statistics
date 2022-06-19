from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Upiti import *
from Validacija import *

def UnosAzuriranjeOkvir():
    root = Tk()
    root.geometry('1200x600')

    root.title("UNOS I AZURIRANJE PODATAKA")
    tabControl = ttk.Notebook(root)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='    Igraci    ')
    tabControl.add(tab2, text='    Heroji    ')
    tabControl.add(tab3, text='    Predmeti    ')
    tabControl.pack(expand=1, fill="both")


    def igraci():
        naslov = Label(tab1, text="Prikaz svih igraca")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        game_frame = Frame(tab1)
        game_frame.pack()

        # scrollbar
        game_scroll = Scrollbar(game_frame)
        game_scroll.pack(side=RIGHT, fill=Y)

        my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set)

        game_scroll.config(command=my_game.yview)

        # define our column

        my_game['columns'] = ('id_igraca', 'ime', 'rank')

        # format our column
        my_game.column("#0", width=0, stretch=NO)
        my_game.column("id_igraca", anchor=CENTER, width=80)
        my_game.column("ime", anchor=CENTER, width=80)
        my_game.column("rank", anchor=CENTER, width=80)

        # Create Headings
        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("id_igraca", text="Id", anchor=CENTER)
        my_game.heading("ime", text="Ime", anchor=CENTER)
        my_game.heading("rank", text="Rank", anchor=CENTER)

        # add data

        def osveziTabelu():
            my_game.delete(*my_game.get_children())

            lst = lstIgraca()
            for i in lst:
                my_game.insert(parent='', index='end', text='',
                            values=(i[0], i[1], i[2]))
            my_game.pack()
        osveziTabelu()

        frame = Frame(tab1)
        frame.pack(pady=20)

        # labels
        ime = Label(frame, text="ime")
        ime.grid(row=0, column=0)

        rank = Label(frame, text="rank")
        rank.grid(row=0, column=1)

        # Entry boxes
        ime_unos = Entry(frame)
        ime_unos.grid(row=1, column=0)

        rank_unos = Entry(frame)
        rank_unos.grid(row=1, column=1)

        # Select Record
        def select_record():
            # clear entry boxes
            ime_unos.delete(0, END)
            rank_unos.delete(0, END)

            # grab record
            selected = my_game.focus()
            # grab record values
            values = my_game.item(selected, 'values')
            # temp_label.config(text=selected)

            # output to entry boxes
            ime_unos.insert(0, values[1])
            rank_unos.insert(0, values[2])

        # save Record
        def update_record():
            selected = my_game.focus()

            values = my_game.item(selected, 'values')
            lst = lstIgraca()

            if provera_unosa_tekst(ime_unos.get()) and provera_unosa_broja(rank_unos.get()):
                if provera_naziva(ime_unos.get(), lst, values[0]):
                    messagebox.showinfo(title='Bravo', message=izmenaIgraca(ime_unos.get(), rank_unos.get(), values[0]))

                    osveziTabelu()
                    # clear entry boxes
                    ime_unos.delete(0, END)
                    rank_unos.delete(0, END)

                else:
                    messagebox.showerror(title='Greska', message="Naziv vec postoji!")
            else:
                messagebox.showerror(title='Greska', message="Nepravilan unos!")


        def add_record():
            selected = my_game.focus()

            lst = lstIgraca()
            if provera_unosa_tekst(ime_unos.get()) and provera_unosa_broja(rank_unos.get()):
                if provera_naziva(ime_unos.get(), lst):
                    messagebox.showinfo(title='Bravo', message=dodajIgraca(ime_unos.get(), rank_unos.get()))
                    osveziTabelu()
                    # clear entry boxes
                    ime_unos.delete(0, END)
                    rank_unos.delete(0, END)
                    # my_game.delete(0, END)
                else:
                    messagebox.showerror(title='Greska', message="Naziv vec postoji!")
            else:
                messagebox.showerror(title='Greska', message="Nepravilan unos!")

        # Buttons
        select_button = Button(tab1, text="Izaberi zapis", command=select_record)
        select_button.pack(pady=10)

        refresh_button = Button(tab1, text="Sacuvaj zapis", command=update_record)
        refresh_button.pack(pady=10)

        add_button = Button(tab1, text="Dodaj zapis", command=add_record)
        add_button.pack(pady=10)

        temp_label = Label(tab1, text="")
        temp_label.pack()

    def heroji():
        naslov = Label(tab2, text="Prikaz svih heroja")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        game_frame = Frame(tab2)
        game_frame.pack()

        # scrollbar
        game_scroll = Scrollbar(game_frame)
        game_scroll.pack(side=RIGHT, fill=Y)

        my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set)

        game_scroll.config(command=my_game.yview)

        # define our column

        my_game['columns'] = ('id_heroja', 'naziv', 'spos', 'zdravlje', 'mana', 'steta', 'opseg', 'oklop', 'brzina')

        # format our column
        my_game.column("#0", width=0, stretch=NO)
        my_game.column("id_heroja", anchor=CENTER, width=80)
        my_game.column("naziv", anchor=CENTER, width=80)
        my_game.column("spos", anchor=CENTER, width=80)
        my_game.column("zdravlje", anchor=CENTER, width=80)
        my_game.column("mana", anchor=CENTER, width=80)
        my_game.column("steta", anchor=CENTER, width=80)
        my_game.column("opseg", anchor=CENTER, width=80)
        my_game.column("oklop", anchor=CENTER, width=80)
        my_game.column("brzina", anchor=CENTER, width=80)

        # Create Headings
        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("id_heroja", text="Id", anchor=CENTER)
        my_game.heading("naziv", text="Naziv", anchor=CENTER)
        my_game.heading("spos", text="Sposobnost", anchor=CENTER)
        my_game.heading("zdravlje", text="Zdravlje", anchor=CENTER)
        my_game.heading("mana", text="Mana", anchor=CENTER)
        my_game.heading("steta", text="Steta", anchor=CENTER)
        my_game.heading("opseg", text="Opseg", anchor=CENTER)
        my_game.heading("oklop", text="Oklop", anchor=CENTER)
        my_game.heading("brzina", text="Brzina", anchor=CENTER)

        # add data
        def osveziTabelu():
            my_game.delete(*my_game.get_children())

            lst = lstHeroja()
            for i in lst:
                my_game.insert(parent='', index='end', text='',
                            values=(i[0], i[1], i[9], i[3], i[4], i[5], i[6], i[7], i[8]))
            my_game.pack()
        osveziTabelu()

        frame = Frame(tab2)
        frame.pack(pady=20)

        # labels
        naziv = Label(frame, text="naziv")
        naziv.grid(row=0, column=0)

        sposobnost = Label(frame, text="sposobnost")
        sposobnost.grid(row=0, column=1)

        zdravlje = Label(frame, text="zdravlje")
        zdravlje.grid(row=0, column=2)

        mana = Label(frame, text="mana")
        mana.grid(row=0, column=3)

        steta = Label(frame, text="steta")
        steta.grid(row=0, column=4)

        opseg = Label(frame, text="opseg")
        opseg.grid(row=0, column=5)

        oklop = Label(frame, text="oklop")
        oklop.grid(row=0, column=6)

        brzina = Label(frame, text="brzina")
        brzina.grid(row=0, column=7)

        # Entry boxes
        naziv = Entry(frame)
        naziv.grid(row=1, column=0)

        varSpos = StringVar()
        sposobnost = ttk.Combobox(frame, textvariable=varSpos, state='readonly')
        sposobnost.grid(row=1, column=1)

        lstSpos = lstSposobnosti()
        strLst = []
        for i in lstSpos:
            strLst.append(i[1])
        sposobnost['values'] = strLst

        zdravlje = Entry(frame)
        zdravlje.grid(row=1, column=2)

        mana = Entry(frame)
        mana.grid(row=1, column=3)

        steta = Entry(frame)
        steta.grid(row=1, column=4)

        opseg = Entry(frame)
        opseg.grid(row=1, column=5)

        oklop = Entry(frame)
        oklop.grid(row=1, column=6)

        brzina = Entry(frame)
        brzina.grid(row=1, column=7)

        # Select Record
        def select_record():
            # clear entry boxes
            naziv.delete(0, END)
            sposobnost.delete(0, END)
            zdravlje.delete(0, END)
            mana.delete(0, END)
            steta.delete(0, END)
            opseg.delete(0, END)
            oklop.delete(0, END)
            brzina.delete(0, END)

            # grab record
            selected = my_game.focus()
            # grab record values
            values = my_game.item(selected, 'values')
            # temp_label.config(text=selected)

            # output to entry boxes
            naziv.insert(0, values[1])
            sposobnost.set(values[2])
            zdravlje.insert(0, values[3])
            mana.insert(0, values[4])
            steta.insert(0, values[5])
            opseg.insert(0, values[6])
            oklop.insert(0, values[7])
            brzina.insert(0, values[8])

        # save Record
        def update_record():
            selected = my_game.focus()

            values = my_game.item(selected, 'values')
            lst = lstHeroja()

            if provera_unosa_tekst(naziv.get()) and \
                (int(sposobnost.index("end")) != 0) and\
                provera_unosa_broja(zdravlje.get()) and\
                provera_unosa_broja(mana.get()) and\
                provera_unosa_broja(steta.get()) and\
                provera_unosa_broja(opseg.get()) and \
                provera_unosa_broja(oklop.get()) and\
                provera_unosa_broja(brzina.get()):
                if provera_naziva(naziv.get(), lst, values[0]):
                    messagebox.showinfo(title='Bravo', message=izmenaHeroja(naziv.get(), zdravlje.get(), mana.get(), steta.get(), opseg.get(), oklop.get(), brzina.get(), sposobnost.get(), values[0]))

                    osveziTabelu()
                    # clear entry boxes
                    naziv.delete(0, END)
                    sposobnost.set('')
                    zdravlje.delete(0, END)
                    mana.delete(0, END)
                    steta.delete(0, END)
                    opseg.delete(0, END)
                    oklop.delete(0, END)
                    brzina.delete(0, END)

                else:
                    messagebox.showerror(title='Greska', message="Naziv vec postoji!")
            else:
                messagebox.showerror(title='Greska', message="Nepravilan unos!")

        def add_record():
            lst = lstHeroja()
            if provera_unosa_tekst(naziv.get()) and \
                    (int(sposobnost.index("end")) != 0) and \
                    provera_unosa_broja(zdravlje.get()) and \
                    provera_unosa_broja(mana.get()) and \
                    provera_unosa_broja(steta.get()) and \
                    provera_unosa_broja(opseg.get()) and \
                    provera_unosa_broja(oklop.get()) and \
                    provera_unosa_broja(brzina.get()):
                if provera_naziva(naziv.get(), lst):
                    messagebox.showinfo(title='Bravo', message=dodajHeroja(naziv.get(), zdravlje.get(), mana.get(), steta.get(), opseg.get(), oklop.get(), brzina.get(), sposobnost.get()))
                    osveziTabelu()
                    # clear entry boxes
                    naziv.delete(0, END)
                    sposobnost.set('')
                    zdravlje.delete(0, END)
                    mana.delete(0, END)
                    steta.delete(0, END)
                    opseg.delete(0, END)
                    oklop.delete(0, END)
                    brzina.delete(0, END)

                else:
                    messagebox.showerror(title='Greska', message="Naziv vec postoji!")
            else:
                messagebox.showerror(title='Greska', message="Nepravilan unos!")

        # Buttons
        select_button = Button(tab2, text="Izaberi zapis", command=select_record)
        select_button.pack(pady=10)

        refresh_button = Button(tab2, text="Sacuvaj zapis", command=update_record)
        refresh_button.pack(pady=10)

        refresh_button = Button(tab2, text="Dodaj zapis", command=add_record)
        refresh_button.pack(pady=10)

        temp_label = Label(tab2, text="")
        temp_label.pack()

    def predmeti():
        naslov = Label(tab3, text="Prikaz svih predmeta")
        naslov.pack(pady=10)
        naslov.config(font=(25))

        game_frame = Frame(tab3)
        game_frame.pack()

        # scrollbar
        game_scroll = Scrollbar(game_frame)
        game_scroll.pack(side=RIGHT, fill=Y)

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
            my_game.delete(*my_game.get_children())
            lst = lstPredmeta()
            for i in lst:
                my_game.insert(parent='', index='end', text='',
                            values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
            my_game.pack()
        osveziTabelu()

        frame = Frame(tab3)
        frame.pack(pady=20)

        # labels
        naziv = Label(frame, text="naziv")
        naziv.grid(row=0, column=0)

        status = Label(frame, text="status")
        status.grid(row=0, column=1)

        cena = Label(frame, text="cena")
        cena.grid(row=0, column=2)

        zdravlje = Label(frame, text="zdravlje")
        zdravlje.grid(row=0, column=3)

        mana = Label(frame, text="mana")
        mana.grid(row=0, column=4)

        steta = Label(frame, text="steta")
        steta.grid(row=0, column=5)

        opseg = Label(frame, text="opseg")
        opseg.grid(row=0, column=6)

        oklop = Label(frame, text="oklop")
        oklop.grid(row=0, column=7)

        brzina = Label(frame, text="brzina")
        brzina.grid(row=0, column=8)

        # Entry boxes
        naziv = Entry(frame)
        naziv.grid(row=1, column=0)

        varStatus = StringVar()
        status = ttk.Combobox(frame, textvariable=varStatus, state='readonly')
        status.grid(row=1, column=1)
        status['values'] = ['pasivna', 'aktivna']

        cena = Entry(frame)
        cena.grid(row=1, column=2)

        zdravlje = Entry(frame)
        zdravlje.grid(row=1, column=3)

        mana = Entry(frame)
        mana.grid(row=1, column=4)

        steta = Entry(frame)
        steta.grid(row=1, column=5)

        opseg = Entry(frame)
        opseg.grid(row=1, column=6)

        oklop = Entry(frame)
        oklop.grid(row=1, column=7)

        brzina = Entry(frame)
        brzina.grid(row=1, column=8)


        # Select Record
        def select_record():
            # clear entry boxes
            naziv.delete(0, END)
            status.delete(0, END)
            cena.delete(0, END)
            zdravlje.delete(0, END)
            mana.delete(0, END)
            steta.delete(0, END)
            opseg.delete(0, END)
            oklop.delete(0, END)
            brzina.delete(0, END)

            # grab record
            selected = my_game.focus()
            # grab record values
            values = my_game.item(selected, 'values')
            # temp_label.config(text=selected)

            # output to entry boxes
            naziv.insert(0, values[1])
            status.insert(0, values[2])
            cena.insert(0, values[3])
            zdravlje.insert(0, values[4])
            mana.insert(0, values[5])
            steta.insert(0, values[6])
            opseg.insert(0, values[7])
            oklop.insert(0, values[8])
            brzina.insert(0, values[9])

        # save Record
        def update_record():
            selected = my_game.focus()

            values = my_game.item(selected, 'values')
            lst = lstPredmeta()

            if provera_unosa_tekst(naziv.get()) and \
                (int(status.index("end")) != 0) and\
                provera_unosa_broja(cena.get()):
                if provera_naziva(naziv.get(), lst, values[0]):
                    messagebox.showinfo(title='Bravo', message=izmenaPredmeta(naziv.get(), status.get(), cena.get(), zdravlje.get(), mana.get(), steta.get(), opseg.get(), oklop.get(), brzina.get(), values[0]))
                    osveziTabelu()
                    # clear entry boxes
                    # clear entry boxes
                    naziv.delete(0, END)
                    status.set('')
                    cena.delete(0, END)
                    zdravlje.delete(0, END)
                    mana.delete(0, END)
                    steta.delete(0, END)
                    opseg.delete(0, END)
                    oklop.delete(0, END)
                    brzina.delete(0, END)

                else:
                    messagebox.showerror(title='Greska', message="Naziv vec postoji!")
            else:
                messagebox.showerror(title='Greska', message="Nepravilan unos!")

        def add_record():
            lst = lstPredmeta()
            if provera_unosa_tekst(naziv.get()) and \
                    (int(status.index("end")) != 0) and \
                    provera_unosa_broja(cena.get()):
                if provera_naziva(naziv.get(), lst):
                    messagebox.showinfo(title='Bravo', message=dodajPredmet(naziv.get(), status.get(), cena.get(), zdravlje.get(), mana.get(), steta.get(), opseg.get(), oklop.get(), brzina.get()))
                    osveziTabelu()
                    # clear entry boxes
                    naziv.delete(0, END)
                    status.set('')
                    cena.delete(0, END)
                    zdravlje.delete(0, END)
                    mana.delete(0, END)
                    steta.delete(0, END)
                    opseg.delete(0, END)
                    oklop.delete(0, END)
                    brzina.delete(0, END)

                else:
                    messagebox.showerror(title='Greska', message="Naziv vec postoji!")
            else:
                messagebox.showerror(title='Greska', message="Nepravilan unos!")

        # Buttons
        select_button = Button(tab3, text="Izaberi zapis", command=select_record)
        select_button.pack(pady=10)

        refresh_button = Button(tab3, text="Sacuvaj zapis", command=update_record)
        refresh_button.pack(pady=10)

        refresh_button = Button(tab3, text="Dodaj zapis", command=add_record)
        refresh_button.pack(pady=10)

        temp_label = Label(tab1, text="")
        temp_label.pack()

    igraci()
    heroji()
    predmeti()

    root.mainloop()
    return root

