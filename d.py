doc = open('mat_dv.txt', 'r')

maxName = list()
maxAlName = list()
maxGeoName = list()
maxResult = 0
maxAlResult = 0
maxGeoResult = 0
for i in doc:
    surname, name, clas, alB, geoB = i.split()
    if maxResult < int(alB)+int(geoB):
        maxResult = int(alB)+int(geoB)
        maxName = [surname+" "+name]
    if maxResult == int(alB)+int(geoB):
        maxName.append(surname+" "+name)
    if maxAlResult < int(alB):
        maxAlResult = int(alB)
        maxAlName = [surname+" "+name]
    if maxAlResult == int(alB):
        maxAlName.append(surname+" "+name)
    if maxGeoResult < int(geoB):
        maxGeoResult = int(geoB)
        maxGeoName = [surname+" "+name]
    if maxGeoResult == int(geoB):
        maxGeoName.append(surname+" "+name)
print(maxName, maxAlName, maxGeoName, sep = '\n')


