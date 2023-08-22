import csv
import sqlite3

connect = sqlite3.connect('movieDb.db')
c = connect.cursor()
try:
    c.execute("""CREATE TABLE MOVIE
                (ID INT PRIMARY KEY   NOT NULL,
                NAME TEXT  NOT NULL,
                YEAR INT  NOT NULL,
                RATING TEXT,
                GENRE TEXT,
                RUNTIME INT,
                CASTS TEXT,
                DIRECTORS TEXT,
                WRITERS TEXT);""")
except Exception as e:
    print(e)

with open("IMDB Top 250 Movies.csv", 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    i=0
    for row in csvreader:
        if i == 0:
            i+=1
            continue
        ID = row[0]
        name = row[1]
        year = int(row[2])
        rating = float(row[3])
        genre = row[4]
        certificat = row[5]
        runtime = row[6]
        tagline = row[7]
        casts = row[10]
        directors = row[11]
        writers = row[12]
        try:
            c.execute("""INSERT INTO MOVIE (ID,NAME,YEAR,RATING,GENRE,
                        RUNTIME,CASTS,DIRECTORS,WRITERS) 
                        VALUES ("{}","{}",{},{},"{}","{}","{}","{}","{}");""".format(ID,name, year, rating, genre,runtime,casts,directors,writers))
            print(ID)
        except Exception as e:
            print(e)
    
    connect.commit()
    connect.close()
