import nltk
import requests
from Project2_Flask import app
from nltk import sent_tokenize
from nltk import word_tokenize
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SelectField, RadioField

from Project2_Flask import main_functions


class MovieReviewsForm(FlaskForm):
    keyword = StringField('keyword')
    orderBy = SelectField('orderBy', choices=[('by-opening-date', 'Opening date'),
                                                ('by-publication-date', 'Publication date'),
                                                ('by-title', 'Title')])
    critics_Picks = RadioField('critics_Picks', choices=[('Y', 'Yes'),
                                                         ('No', 'No')])


def generateDataFromAPI(keyword, order_By, critics_Picks):
    my_key_dict = main_functions.read_from_file("Project2_Flask/JSON_Documents/api_keys.json")
    my_key = my_key_dict["my_ny_key"]
    url = "https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=" + keyword + "&order=" + order_By + "&critics-pick=" + critics_Picks + "&api-key=" + my_key
    response = requests.get(url).json()
    main_functions.save_to_file(response, "Project2_Flask/JSON_Documents/response.json")
    data_requested = main_functions.read_from_file("Project2_Flask/JSON_Documents/response.json")
    #data_requested = {}
    movieTitles = []
    for i in data_requested["results"]:
        movieTitles.append(i["display_title"])
    critics = []
    for i in data_requested["results"]:
        critics.append(i["byline"])
    publicationDates = []
    for i in data_requested["results"]:
        publicationDates.append(i["publication_date"])
    reviewUrls = []
    for i in data_requested["results"]:
        for j in data_requested["link"]:
            reviewUrls.append(j["url"])
    """From the response dictionary, you need to filter the data requested by the user"""
    data_requested["titles"] = movieTitles
    data_requested["critics"] = critics
    data_requested["publicationDates"] = publicationDates
    data_requested["reviewLinks"] = reviewUrls
    return data_requested
