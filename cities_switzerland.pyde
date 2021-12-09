import csv

citiesData = None

def setup():
    global citiesData
    size(900, 600)
    citiesFileHandle = open("cities.csv")
    citiesData = list(csv.DictReader(citiesFileHandle))
    
#  lat : Breitengrad
#  lng : Längengrad
#  ortXYP : VAriable mit Koordinaten (x,y) und Bevölkerungszahl
#  citiesData : CSV Datei
#  population: Bevölkerungszahl
#  city: Ortschaft
#  "u" vor dem Text ermöglicht die Darstellung von Umlauten
        
def draw():
    background (255, 255, 255)
    
#Titel
    fill (200, 200, 100)
    textAlign(CENTER)
    textSize(50)
    text("Ortschaften der Schweiz", 450, 50)
    textAlign(CENTER)
    fill (150, 150, 200)
    textSize(20)
    text(u"Die Grösse der Kreise entsprechen den Einwohnerzahlen", 450, 80)

# Koordianten und Einwohnerzahl werden aus der CSV-Datei ausgelsen        
    global einwohner
    for row in citiesData:
        lat = float(row["lat"])
        lng = float(row["lng"])
        population = int(row["population"])
        city = (row["city"])
        ortXYP(city, lat, lng, population)

# x-Koordinate und y-Koordinate werden definiert                            
def ortXYP(city, lat, lng, population):
    x = 80 + (5.9789 - lng) * -180
    y = ((47.7493 - lat) * 200) + 100

    
# Farbe (Die Anteile an rot & gelb im "r-g-b-Schema" werden mit Hilfe der Bevölkerungszahl berchnet) und Grösse der Kreise wird bestimmt
    if int(population) < 1000:
        fill (population/3, population/3, 20)
        circle (x, y, 4)
    elif 1001 < int(population) < 5000: 
        fill (population/30, population/30, 20)
        circle (x, y, 5)
    elif 5001 < int(population) < 10000: 
        fill (population/50, population/50, 20)
        circle (x, y, 8)
    elif 10001 < int(population) < 25000: 
        fill (population/100, population/100, 20)
        circle (x, y, 12)
    elif 25001 < int(population) < 50000: 
        fill (population/200, population/200, 20)
        circle (x, y, 26)
    elif 50001 < int(population) < 75000: 
        fill (population/400, population/400, 20)
        circle (x, y, 20)
    elif 75001 < int(population) < 100000: 
        fill (population/900, population/900, 20)
        circle (x, y, 24)
    elif 100001 < int(population) < 150000: 
        fill (population/1000, population/1000, 20)
        circle (x, y, 28)
    elif 150001 < int(population) < 200000:
        fill (population/1000, population/1000, 20)
        circle (x, y, 32)
    elif int(population) > 200001:
        fill (population/1000, population/1000, 20)
        circle (x, y, 36)
    
    
      
    if (10 * x - 10 * mouseX < 3) and (10 * y - 10 * mouseY < 3):
        text (city, 100, 100)
    else:
        text ("", 100, 100)
        

    
