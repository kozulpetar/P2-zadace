from csv  import reader
with open("rezultati.csv", "r", encoding="utf8") as read_obj:
    csv_reader=reader(read_obj)
    rezultati=list(map(tuple, csv_reader))

nova_lista=[]
for ime, prezime, bodovi in rezultati:
     nova_lista.append((prezime, ime, bodovi))
nova_lista.sort()


def ocjene(bodovi):
    if bodovi < 50:
        return "nedovoljan"
    elif bodovi < 65:
        return "dovoljan"
    elif bodovi < 80:
        return "dobar" 
    elif bodovi < 90:
        return "vrlo_dobar" 
    else:
        return "odlican"

popis_ocjena=[]    
for student in nova_lista:    
    rjecnik={"ime": student[0],
             "prezime": student[1],
             "ocjena": ocjene(int(student[2])), }
    popis_ocjena.append(rjecnik)



popis=[]

for student in popis_ocjena:
    popis.append((student["prezime"],student["ime"], student["ocjena"] ))

print(popis)