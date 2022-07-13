def parnibrojevi(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def neparnibrojevi(n):
    for i in range(n):
        if i % 2 != 0:
            yield i


a = int(input("Unesite broj: "))
generator_parnihbrojeva = parnibrojevi(a)
generator_neparnihbrojeva = neparnibrojevi(a)

brojevi = zip(generator_parnihbrojeva, generator_neparnihbrojeva)

for parni_br, neparni_br in brojevi:
    print("Parni:", parni_br, "Neparni:", neparni_br)