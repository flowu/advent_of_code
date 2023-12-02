def solver():
    result = 0
    for n in range(246515, 739105 + 1):
        ok = False
        ental = int(str(n)[5:6])
        tiotal = int(str(n)[4:5])
        hundratal = int(str(n)[3:4])
        tusental = int(str(n)[2:3])
        tiotusental = int(str(n)[1:2])
        hundratusental = int(str(n)[0:1])
        lista = [hundratusental, tiotusental, tusental, hundratal, tiotal, ental, -1]
        
        # dummy -1 because index oob when adding 2. Why is lista[num+2] oob? lista[num-1] is not oob..
        for num, (before, after) in enumerate(zip(lista, lista[1:])):
            if (before == after):
                if before != lista[num - 1]:
                    if after != lista[num + 2]:
                        ok = True
        if (hundratusental <= tiotusental) & (tiotusental <= tusental) & (tusental <= hundratal) & (hundratal <= tiotal) & (tiotal <= ental) & ok:
            result += 1
    return result

print(solver())