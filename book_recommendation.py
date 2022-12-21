'''
IDS2022 Project E17 Sangheon Lee

Book Recommendation System
based on Amazon Books reviews
'''

import tkinter as tk
import pandas as pd

'''
FUNCTION
'''

def display_books(file_name, keyword_list):
    #through algorithm display books
    #nested list: [[title1, review1], [title2, review2] ...]
    df_reviews = pd.read_csv('data/resized_review_file.csv')
    
    review_list = df_reviews.values.tolist()
    
    #nested loop: [title, count]
    df_titles = pd.read_csv(file_name)
    title_list = df_titles['Title'].values.tolist()
    
    counting_list = []
    for ind in range(len(title_list)):
        counting_list.append(0)

    for review in review_list:
        for keyword in keyword_list:
            counter = str(review[1]).count(keyword)
            
            if review[0] in title_list:
                ind = title_list.index(review[0])
                counting_list[ind] += counter

            
            print(review_list.index(review), review_list.index(review) / len(review_list))
    
    value1 = 0
    value2 = 0
    value3 = 0
    value4 = 0
    value5 = 0
    ind1 = 0
    ind2 = 0
    ind3 = 0
    ind4 = 0
    ind5 = 0

    for ind in range(len(counting_list)):
        if counting_list[ind] > value1:
            value5 = value4
            ind5 = ind4
            value4 = value3
            ind4 = ind3
            value3 = value2
            ind3 = ind2
            value2 = value1
            ind2 = ind1
            value1 = counting_list[ind]
            ind1 = ind
        elif counting_list[ind] > value2:
            value5 = value4
            ind5 = ind4
            value4 = value3
            ind4 = ind3
            value3 = value2
            ind3 = ind2
            value2 = counting_list[ind]
            ind2 = ind
        elif counting_list[ind] > value3:
            value5 = value4
            ind5 = ind4
            value4 = value3
            ind4 = ind3
            value3 = counting_list[ind]
            ind3 = ind
        elif counting_list[ind] > value4:
            value5 = value4
            ind5 = ind4
            value4 = counting_list[ind]
            ind4 = ind
        elif counting_list[ind] > value5:
            value5 = counting_list[ind]
            ind5 = ind



    

    for ind in range(5):
        print(counting_list[ind])

    #open GUI
    result_window = tk.Tk()
    result_window.title('RESULT')

    canvas_result_window = tk.Canvas(result_window, width = 300, height = 300, relief = 'raised')
    canvas_result_window.pack()

    #write program title
    label_title = tk.Label(result_window, text='BOOK RECOMMENDATION')
    label_title.config(font = ('helvetica', 20, 'bold'))
    canvas_result_window.create_window(150, 50, window = label_title)
    
    #write text info
    label_text_info = tk.Label(result_window, text='Recommended Books')
    label_text_info.config(font = ('helvetica', 14))
    canvas_result_window.create_window(150, 80, window = label_text_info)

    label_book1_info = tk.Label(result_window, text = title_list[ind1])
    label_book1_info.config(font = ('helvetica', 14))
    label_book2_info = tk.Label(result_window, text = title_list[ind2])
    label_book2_info.config(font = ('helvetica', 14))
    label_book3_info = tk.Label(result_window, text = title_list[ind3])
    label_book3_info.config(font = ('helvetica', 14))
    label_book4_info = tk.Label(result_window, text = title_list[ind4])
    label_book4_info.config(font = ('helvetica', 14))
    label_book5_info = tk.Label(result_window, text = title_list[ind5])
    label_book5_info.config(font = ('helvetica', 14))

    canvas_result_window.create_window(150, 150, window = label_book1_info)
    canvas_result_window.create_window(150, 180, window = label_book2_info)
    canvas_result_window.create_window(150, 210, window = label_book3_info)
    canvas_result_window.create_window(150, 240, window = label_book4_info)
    canvas_result_window.create_window(150, 270, window = label_book5_info)

def get_atmosphere_preference():
    def display_cheerful_fiction():
        fiction_window.withdraw()

        keyword_list = ["exciting", "cheerful", "bright"]
        display_books("data/fictions.csv", keyword_list)

    def display_humorous_fiction():
        fiction_window.withdraw()

        keyword_list = ["fun", "funny", "comic", "humor"]
        display_books("data/fictions.csv", keyword_list)

    def display_romantic_fiction():
        fiction_window.withdraw()

        keyword_list = ["romantic", "love"]
        display_books("data/fictions.csv", keyword_list)

    def display_idyllic_fiction():
        fiction_window.withdraw()

        keyword_list = ["idyll", "rural"]
        display_books("data/fictions.csv", keyword_list)

    def display_gloomy_fiction():
        fiction_window.withdraw()

        keyword_list = ["gloomy", "sad", "dark"]
        display_books("data/fictions.csv", keyword_list)

    def display_mysterious_fiction():
        fiction_window.withdraw()

        keyword_list = ["mystery", "curious"]
        display_books("data/fictions.csv", keyword_list)

    def display_tense_fiction():
        fiction_window.withdraw()

        keyword_list = ["tense", "thrill"]
        display_books("data/fictions.csv", keyword_list)

    def display_fearful_fiction():
        fiction_window.withdraw()

        keyword_list = ["fear", "horror"]
        display_books("data/fictions.csv", keyword_list)
    
    #open GUI
    root.destroy()

    fiction_window = tk.Tk()
    fiction_window.title('ATMOSPHERE')

    canvas_fiction_window = tk.Canvas(fiction_window, width = 300, height = 300, relief = 'raised')
    canvas_fiction_window.pack()

    #write program title
    label_title = tk.Label(fiction_window, text='BOOK RECOMMENDATION')
    label_title.config(font = ('helvetica', 20, 'bold'))
    canvas_fiction_window.create_window(150, 50, window = label_title)
    
    #write text info
    label_text_info = tk.Label(fiction_window, text='Click the atmosphere of the fiction you want')
    label_text_info.config(font = ('helvetica', 14))
    canvas_fiction_window.create_window(150, 80, window = label_text_info)

    #make buttons
    button_cheerful = tk.Button(fiction_window, text = "Cheerful", command = display_cheerful_fiction, font = ('helvetica', 12))
    button_humorous = tk.Button(fiction_window, text = "Humorous", command = display_humorous_fiction, font = ('helvetica', 12))
    button_romantic = tk.Button(fiction_window, text = "Romantic", command = display_romantic_fiction, font = ('helvetica', 12))
    button_idyllic = tk.Button(fiction_window, text = "Idyllic", command = display_idyllic_fiction, font = ('helvetica', 12))
    button_gloomy = tk.Button(fiction_window, text = "Gloomy", command = display_gloomy_fiction, font = ('helvetica', 12))
    button_mysterious = tk.Button(fiction_window, text = "Mysterious", command = display_mysterious_fiction, font = ('helvetica', 12))
    button_tense = tk.Button(fiction_window, text = "Tense", command = display_tense_fiction, font = ('helvetica', 12))
    button_fearful = tk.Button(fiction_window, text = "Fearful", command = display_fearful_fiction, font = ('helvetica', 12))

    canvas_fiction_window.create_window(100, 150, window = button_cheerful)
    canvas_fiction_window.create_window(200, 150, window = button_humorous)
    canvas_fiction_window.create_window(100, 183, window = button_romantic)
    canvas_fiction_window.create_window(200, 183, window = button_idyllic)
    canvas_fiction_window.create_window(100, 216, window = button_gloomy)
    canvas_fiction_window.create_window(200, 216, window = button_mysterious)
    canvas_fiction_window.create_window(100, 250, window = button_tense)
    canvas_fiction_window.create_window(200, 250, window = button_fearful)

    fiction_window.mainloop()

def get_genre_preference():
    def display_history_nonfiction():
        nonfiction_window.withdraw()

        keyword_list = ["history", "war"]
        display_books("data/nonfictions/history.csv", keyword_list)

    def display_biographies_nonfiction():
        nonfiction_window.withdraw()

        keyword_list = ["biography", "life"]
        display_books("data/nonfictions/biographies.csv", keyword_list)

    def display_economics_nonfiction():
        nonfiction_window.withdraw()

        keyword_list = ["economy", "bussiness", "money", "stock"]
        display_books("data/nonfictions/economics.csv", keyword_list)

    def display_religion_nonfiction():
        nonfiction_window.withdraw()

        keyword_list = ["religion", "faith"]
        display_books("data/nonfictions/religion.csv", keyword_list)

    def display_technology_nonfiction():
        nonfiction_window.withdraw()

        keyword_list = ["technology", "electronic", "evolution"]
        display_books("data/nonfictions/technology.csv", keyword_list)

    def display_social_science_nonfiction():
        nonfiction_window.withdraw()

        keyword_list = ["social", "society", "community", 'world']
        display_books("data/nonfictions/social_science.csv", keyword_list)

    def display_art_nonfiction():
        nonfiction_window.withdraw()

        keyword_list = ["art"]
        display_books("data/nonfictions/law.csv", keyword_list)

    def display_travel_nonfiction():
        nonfiction_window.withdraw()

        keyword_list = ["travel", "trip", "tour"]
        display_books("data/nonfictions/travel.csv", keyword_list)
    
    #open GUI
    root.destroy()
    
    nonfiction_window = tk.Tk()
    nonfiction_window.title('GENRE')

    canvas_nonfiction_window = tk.Canvas(nonfiction_window, width = 300, height = 300, relief = 'raised')
    canvas_nonfiction_window.pack()

    #write program title
    label_title = tk.Label(nonfiction_window, text='BOOK RECOMMENDATION')
    label_title.config(font = ('helvetica', 20, 'bold'))
    canvas_nonfiction_window.create_window(150, 50, window = label_title)
    
    #write text info
    label_text_info = tk.Label(nonfiction_window, text='Click the genre of the nonfiction you want')
    label_text_info.config(font = ('helvetica', 14))
    canvas_nonfiction_window.create_window(150, 80, window = label_text_info)

    #make buttons
    button_history = tk.Button(nonfiction_window, text = "History", command = display_history_nonfiction, font = ('helvetica', 12))
    button_biographies = tk.Button(nonfiction_window, text = "Biographies", command = display_biographies_nonfiction, font = ('helvetica', 12))
    button_economics = tk.Button(nonfiction_window, text = "Economics", command = display_economics_nonfiction, font = ('helvetica', 12))
    button_religion = tk.Button(nonfiction_window, text = "Religion", command = display_religion_nonfiction, font = ('helvetica', 12))
    button_technology = tk.Button(nonfiction_window, text = "Technology", command = display_technology_nonfiction, font = ('helvetica', 12))
    button_social_science = tk.Button(nonfiction_window, text = "Social Science", command = display_social_science_nonfiction, font = ('helvetica', 12))
    button_art = tk.Button(nonfiction_window, text = "Art", command = display_art_nonfiction, font = ('helvetica', 12))
    button_travel = tk.Button(nonfiction_window, text = "Travel", command = display_travel_nonfiction, font = ('helvetica', 12))

    canvas_nonfiction_window.create_window(100, 150, window = button_history)
    canvas_nonfiction_window.create_window(200, 150, window = button_biographies)
    canvas_nonfiction_window.create_window(100, 183, window = button_economics)
    canvas_nonfiction_window.create_window(200, 183, window = button_religion)
    canvas_nonfiction_window.create_window(100, 216, window = button_technology)
    canvas_nonfiction_window.create_window(200, 216, window = button_social_science)
    canvas_nonfiction_window.create_window(100, 250, window = button_art)
    canvas_nonfiction_window.create_window(200, 250, window = button_travel)

    nonfiction_window.mainloop()



#open GUI
root = tk.Tk()
root.title('CATEGORY')

canvas_root = tk.Canvas(root, width = 300, height = 300, relief = 'raised')
canvas_root.pack()

#write program title
label_title = tk.Label(root, text='BOOK RECOMMENDATION')
label_title.config(font = ('helvetica', 20, 'bold'))
canvas_root.create_window(150, 50, window = label_title)

#write text info
label_text_info = tk.Label(root, text='Click the category you want')
label_text_info.config(font = ('helvetica', 16))
canvas_root.create_window(150, 80, window = label_text_info)

#make buttons
button_fiction = tk.Button(text = "FICTION", command = get_atmosphere_preference, font = ('helvetica', 12))
button_non_fiction = tk.Button(text = "NON-FICTION", command = get_genre_preference, font = ('helvetica', 12))

canvas_root.create_window(150, 150, window = button_fiction)
canvas_root.create_window(150, 200, window = button_non_fiction)

root.mainloop()



