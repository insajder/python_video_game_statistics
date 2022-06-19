
def provera_unosa_tekst(unos):
    if len(unos.strip()) < 0:
        return False
    else:
        return True

def provera_unosa_broja(unos):
    try:
        float(unos)
        if float(unos) < 0:
            return False
        else:
            return True
    except ValueError:
        return False

def provera_naziva(unos, lst, id=-1):
    for i in lst:
        if int(id) is not int(i[0]):
            if unos == i[1]:
                return False
    return True

def procenti(ukupno, pojedinacno):
    return (str(round(pojedinacno * 100 / ukupno,1))+'%')

