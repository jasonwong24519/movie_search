import sqlite3
import pandas as pd

connect = sqlite3.connect('movieDb.db')
c = connect.cursor()

movies = pd.read_sql("""SELECT * FROM MOVIE WHERE ID = 3 OR ID = 4""", connect)
a = movies['WRITERS'].values

element = {"NAME", "YEAR", "CASTS", "DIRECTORS", "WRITERS"}

def match_element(inputSTR: str) -> str:
  global element 
  score = ["NAME",0]
  inputSTR = inputSTR.upper() 
  for i in element:
    match_score = 0
    element_set = set(i)
    for l in range(len(inputSTR)):
      if inputSTR[l] in element_set:
        element_set.remove(inputSTR[l])
        match_score+=1
    if match_score > score[1]:
      score[0] = i
      score[1] = match_score
  return score[0]
      

def searching(element: str, value: str) -> list[str]:
  movies = pd.read_sql("SELECT * FROM MOVIE WHERE {} LIKE '%{}%' ORDER BY YEAR DESC".format(element, value), connect)
  result = []
  for i in range(len(movies)):
    name = movies['NAME'].values[i]
    year = movies['YEAR'].values[i]
    runtime = movies['RUNTIME'].values[i]
    casts = movies['CASTS'].values[i]
    directors = movies['DIRECTORS'].values[i]
    writers = movies['WRITERS'].values[i]
    movie = "Name: " + name + "  " + str(year) + "  runtime:" + runtime + "\n" +\
            "Casts: " + casts + "\n" + "Directors: " + directors + "\n" +\
            "Writers: " + writers
    result.append(movie)
  return result
  
while (True):
  element_of_movie = input("I want to find movie based on: ")
  element_of_movie = match_element(element_of_movie)
  keyword = input("{}:Im finding: ".format(element_of_movie))
  result = searching(element_of_movie, keyword)
  for i in range(len(result)):
    print(result[i]+"\n")
    if i == 9:
      show = input("The number of results is more than 10,\n if want to show all enter (y): ")
      if show == 'y':
        pass
      else:
        break
