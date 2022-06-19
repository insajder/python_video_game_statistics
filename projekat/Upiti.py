import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-0DQ26DN\MSSQLSERVER02;'
                      'Database=dota;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

def lstIgraca():
    upit = """
        select *
        from igrac
    """
    lst = cursor.execute(upit)
    return lst

def izmenaIgraca(ime, rank, id):
    poruka = ''
    izmena = """
        update igrac 
        set ime = ?, rank = ? 
        where id_igraca = ?
    """
    vrednostiZaIzmenu = (ime, rank, id)

    cursor.execute(izmena, vrednostiZaIzmenu)
    data = cursor.messages
    poruka += str(data).split(']')[4].replace("')", "")
    conn.commit()
    return poruka

def dodajIgraca(ime, rank):
    poruka = ''
    dodaj = """
        insert into igrac(ime, rank)
        values (?, ?)
    """
    noveVrednosti = (ime, rank)

    cursor.execute(dodaj, noveVrednosti)
    data = cursor.messages
    poruka += str(data).split(']')[4].replace("')", "")
    conn.commit()
    return poruka

def lstHeroja():
    upit = """
       select h.*, s.naziv as spos
       from heroj h, sposobnost s
       where h.id_sposobnosti = s.id_sposobnosti
    """
    lst = cursor.execute(upit)
    return lst

def lstSposobnosti():
    upit = 'select * from sposobnost'
    lstSpos = cursor.execute(upit)
    return lstSpos

def izmenaHeroja(naziv, zdravlje, mana, steta, opseg, oklop, brzina, sposobnost, id):
    poruka = ''
    izmena = """
        update heroj
        set naziv=?, zdravlje=?, mana=?, steta=?, opseg=?, oklop=?, brzina=?, id_sposobnosti=(
            select id_sposobnosti from sposobnost where naziv=? ) 
        where id_heroja = ?
    """
    vrednostiZaIzmenu = (naziv, zdravlje, mana, steta, opseg, oklop, brzina, sposobnost, id)

    cursor.execute(izmena, vrednostiZaIzmenu)
    data = cursor.messages
    poruka += str(data).split(']')[4].replace("')", "")
    conn.commit()
    return poruka

def dodajHeroja(naziv, zdravlje, mana, steta, opseg, oklop, brzina, sposobnost):
    poruka = ''
    dodaj = """
        insert into heroj(naziv, zdravlje, mana, steta, opseg, oklop, brzina, id_sposobnosti)
        values (?, ?, ?, ?, ?, ?, ?, (
            select id_sposobnosti from sposobnost where naziv=?))
    """
    noveVrednosti = (naziv, zdravlje, mana, steta, opseg, oklop, brzina, sposobnost)

    cursor.execute(dodaj, noveVrednosti)
    data = cursor.messages
    poruka += str(data).split(']')[4].replace("')", "")
    conn.commit()
    return poruka

def lstPredmeta():
    upit = """
        select *
        from predmet
    """

    lst = cursor.execute(upit)
    return lst

def izmenaPredmeta(naziv, status, cena, zdravlje, mana, steta, opseg, oklop, brzina, id):
    poruka = ''
    izmena = """
        update predmet
        set naziv=?, status=?, cena=?, zdravlje=?, mana=?, steta=?, opseg=?, oklop=?, brzina=?
        where id_predmeta = ?
    """
    if mana == 'None' or mana == 0: mana = None
    if steta == 'None' or steta == 0: steta = None
    if opseg == 'None' or opseg == 0: opseg = None
    if oklop == 'None' or oklop == 0: oklop = None
    if brzina == 'None' or brzina == 0: brzina = None
    vrednostiZaIzmenu = (naziv, status, cena, zdravlje, mana, steta, opseg, oklop, brzina, id)
    cursor.execute(izmena, vrednostiZaIzmenu)
    data = cursor.messages
    poruka += str(data).split(']')[4].replace("')", "")
    conn.commit()
    return poruka

def dodajPredmet(naziv, status, cena, zdravlje, mana, steta, opseg, oklop, brzina):
    poruka = ''
    dodaj = """
        insert into predmet(naziv, status, cena, zdravlje, mana, steta, opseg, oklop, brzina)
        values(?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    if mana == 'None': mana = None
    if steta == 'None': steta = None
    if opseg == 'None': opseg = None
    if oklop == 'None': oklop = None
    if brzina == 'None': brzina = None
    noveVrednosti = (naziv, status, cena, zdravlje, mana, steta, opseg, oklop, brzina)

    cursor.execute(dodaj, noveVrednosti)
    data = cursor.messages
    poruka += str(data).split(']')[4].replace("')", "")
    conn.commit()
    return poruka

def lstHerojSposobnost(sposobnost):
    upit = """
       select * from dbo.fun_HerojSposobnost(?)
    """
    lst = cursor.execute(upit, sposobnost)
    return lst

def lstPredmetStatus(status):
    upit = """
       select * from dbo.fun_PredmetStatus(?)
    """
    lst = cursor.execute(upit, status)
    return lst

def lstHerojUspesnost():
    upit = """
       select * from dbo.fun_HerojUspesnost()
       order by ukupno_odigranih desc
    """
    lst = cursor.execute(upit)
    return lst

def lstPredmetIskoriscenost():
    upit = """
       select * from dbo.fun_PredmetIskoriscenost()
       order by iskoriscenost desc
    """
    lst = cursor.execute(upit)
    return lst

def funIgracHeroj(imeIgraca):
    upit = """
       select * from dbo.fun_IgracHeroj(?)
        order by ukupno_partija desc
    """
    lst = cursor.execute(upit, imeIgraca)
    return lst

def viewIgracMec(imeIgraca):
    upit = """
       select * from view_IgracMec
       where ime = ?
       order by datum desc
    """
    lst = cursor.execute(upit, imeIgraca)
    return lst

def funIgracPredmet(imeIgraca):
    upit = """
       select * from dbo.fun_IgracPredmet(?)
       order by iskoriscenost desc
    """
    lst = cursor.execute(upit, imeIgraca)
    return lst

def viewIgracUkupno(imeIgraca):
    upit = """
       select * from view_IgracUkupno
       where ime = ?
    """
    lst = cursor.execute(upit, imeIgraca)
    return lst

def lstMeceva():
    upit = """
       select * from dbo.fun_Mec()
       order by datum desc
    """
    lst = cursor.execute(upit)
    return lst

def lstSvihIgraca():
    upit = """
       select * from dbo.fun_SviIgraci()
    """
    lst = cursor.execute(upit)
    return lst

def lstSvihIgracaSortRankRastuce():
    upit = """
       select * from dbo.fun_SviIgraci()
       order by rank
    """
    lst = cursor.execute(upit)
    return lst

def lstSvihIgracaSortRankOpadajuce():
    upit = """
       select * from dbo.fun_SviIgraci()
       order by rank desc
    """
    lst = cursor.execute(upit)
    return lst

def lstSvihIgracaSortSatiOpadajuce():
    upit = """
       select * from dbo.fun_SviIgraci()
       order by ukupno_sati desc
    """
    lst = cursor.execute(upit)
    return lst

def viewIgracMax(imeIgraca):
    upit = """
       select * from view_IgracMax
       where ime = ?
    """
    lst = cursor.execute(upit, imeIgraca)
    return lst

def viewIgraciRank(rank):
    upit = """
       select * from view_IgraciRank
       where rank > ?
       order by rank desc
    """
    lst = cursor.execute(upit, rank)
    return lst

def spHerojSposobnost(nazivHeroja, nazivSposobnosti):
    upit = "exec sp_heroj_sposobnost_premesti ?, ?"
    noveVrednosti = (nazivHeroja, nazivSposobnosti)
    cursor.execute(upit, noveVrednosti)
    poruka = cursor.fetchone()[0]
    return poruka

def spPredmetCena(naziv, procenat):
    upit = "exec sp_predmet_cena ?, ?"
    noveVrednosti = (naziv, procenat)
    cursor.execute(upit, noveVrednosti)
    poruka = cursor.fetchone()[0]
    return poruka

def spIgracMecBrisanje(ime):
    upit = "exec sp_igrac_obrisi ?"
    cursor.execute(upit, ime)
    poruka = cursor.fetchone()[0]
    return poruka

def spKreiranjeTabele():
    upit = "exec sp_mecevi_pobede"
    cursor.execute(upit)
    poruka = cursor.fetchone()[0]
    return poruka

def lstSPMecevi():
    upit = """
        select *
        from MeceviPobede
    """
    lst = cursor.execute(upit)
    return lst
