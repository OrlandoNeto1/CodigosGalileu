arenas = [
[1200, 1500, 1100, 1800, 1700],
[1000, 950, 1100, 1050, 980],
[2000, 1900,1950, 2100, 2200]

]
medias = [ ]
for a in arenas:
    media = sum(a)/ len(a)
    print (f"A media da arena {a[0]} é de: {media}")
    medias.append(media)
    print(medias)
    

print(max(medias))