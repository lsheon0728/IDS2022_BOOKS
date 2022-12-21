'''
program to preprocess data
'''

import pandas as pd

'''
FUNCTION
'''

def resize_books_data_file():
    csv_file = pd.read_csv('data/books_data.csv')

    useful_columns = ['Title', 'categories']
    useless_columns = ['description', 'authors', 'publisher', 'image', 'previewLink', 'publishedDate', 'infoLink', 'ratingsCount']

    csv_file.drop(useless_columns, inplace = True, axis = 'columns')

    fictions = (csv_file[csv_file['categories'] == '[\'Fiction\']'])
    nonfictions_biographies  = (csv_file[csv_file['categories'] == '[\'Biography & Autobiography\']'])
    nonfictions_religion = (csv_file[csv_file['categories'] == '[\'Religion\']'])
    nonfictions_social_science = (csv_file[csv_file['categories'] == '[\'Social Science\']'])
    nonfictions_technology = (csv_file[csv_file['categories'] == '[\'Technology & Engineering\']'])
    nonfictions_history = (csv_file[csv_file['categories'] == '[\'History\']'])
    nonfictions_travel = (csv_file[csv_file['categories'] == '[\'Travel\']'])
    nonfictions_economics = (csv_file[csv_file['categories'] == '[\'Business & Economics\']'])
    nonfictions_art = (csv_file[csv_file['categories'] == '[\'Art\']'])

    fictions.to_csv('data/fictions.csv', index = False)
    nonfictions_biographies.to_csv('data/nonfictions/biographies.csv', index = False)
    nonfictions_religion.to_csv('data/nonfictions/religion.csv', index = False)
    nonfictions_social_science.to_csv('data/nonfictions/social_science.csv', index = False)
    nonfictions_technology.to_csv('data/nonfictions/technology.csv', index = False)
    nonfictions_history.to_csv('data/nonfictions/history.csv', index = False)
    nonfictions_travel.to_csv('data/nonfictions/travel.csv', index = False)
    nonfictions_economics.to_csv('data/nonfictions/economics.csv', index = False)
    nonfictions_art.to_csv('data/nonfictions/art.csv', index = False)

def resize_review_file():
    #read csv file
    csv_file = pd.read_csv('data/books_rating.csv')

    #choose reviews only with rating 5.0
    csv_file2 = (csv_file[csv_file['review/score'] == 5.0])

    #drop useless columns
    useful_columns = ['Title', 'review/text']
    useless_columns = ['Id', 'review/score', 'Price', 'User_id', 'profileName', 'review/helpfulness', 'review/time', 'review/summary']

    csv_file2.drop(useless_columns, inplace = True, axis = 'columns')

    csv_file2.to_csv('data/resized_review_file.csv', index = False)

def resize_review_file2():
    #read csv file
    csv_file = pd.read_csv('data/books_data.csv')

    #choose reviews only with rating 5.0
    csv_file2 = (csv_file[csv_file['categories'] == "Fiction"])

    #drop useless columns
    useful_columns = ['Title', 'review/text']
    useless_columns = ['description', 'authors', 'publisher', 'image', 'previewLink', 'publishedDate', 'infoLink', 'ratingsCount']

    csv_file2.drop(useless_columns, inplace = True, axis = 'columns')

    csv_file2.to_csv('data/fiction.csv', index = False)

'''
MAIN
'''

resize_books_data_file()
#resize_review_file()

