import pandas as pd
import pymongo


rawImdbDF, rawRottenDF = LoadCsv()

cleanImdbDF, cleanRottenDF = CleanData(rawImdbDF, rawRottenDF)





def CleanData(rawImdbDF, rawRottenDF):
    imdbTrimDF = rawImdbDF[['title','year', 'imdbRating', 'ratingCount']]
    rottenTrimDF = rawRottenDF[['movie_title','in_theaters_date', 'audience_rating','audience_count']]

def LoadCsv():
    #build file location string to read data
    imdbFile = "Resources/Sources/imdb.csv"
    rottenFile = "Resources/Sources/rotten_tomatoes_movies.csv"

    #load movie csv to data frames
    imdbDF = pd.read_csv(imdbFile)
    rottenDF = pd.read_csv(rottenFile)
    return imdbDF, rottenDF

#Create Connection to Mongo DB and create the DB
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
mydb = client["MovieAnalysis"]

