sosire = list(map(int, input().split(":")))

n = int(input())

ora_minima = [25, 60]
pret_minim = 999
film = ""

for i in range(n):
    ora = list(map(str, input().split()))
    ora_film = list(map(int, ora[0].split(":")))

    if ora_film[0] >= sosire[0]:
        if ora_film[0] == sosire[0] and ora_film[1] >= sosire[1]:
            if ora_film[1] < ora_minima[1]:
                ora_minima = ora_film
                pret_minim = int(ora[1])
                film = ora[2]
            else:
                if pret_minim > int(ora[1]):
                    ora_minima = ora_film
                    pret_minim = int(ora[1])
                    film = ora[2]
        else:
            if ora_film[0] < ora_minima[0]:
                ora_minima = ora_film
                pret_minim = int(ora[1])
                film = ora[2]
            else:
                if ora_film[0] == ora_minima[0]:
                    if ora_film[0] == sosire[0]:
                        if ora_film[1] > sosire[1]:
                            if ora_film[1] < ora_minima[1]:
                                ora_minima = ora_film
                                pret_minim = int(ora[1])
                                film = ora[2]
                        else:
                            if pret_minim > int(ora[1]):
                                ora_minima = ora_film
                                pret_minim = int(ora[1])
                                film = ora[2]
                    else:
                        if ora_film[1] < ora_minima[1]:
                            ora_minima = ora_film
                            pret_minim = int(ora[1])
                            film = ora[2]
                        else:
                            if pret_minim > int(ora[1]):
                                ora_minima = ora_film
                                pret_minim = int(ora[1])
                                film = ora[2]

print(film)
