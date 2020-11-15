from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SelectField, RadioField
import requests

class NewsForm(FlaskForm):
    format = SelectField('Format', choices = [('shared','shared'),
                                              ('emailed', 'emailed'),
                                              ('viewed', 'viewed')])

def generateDataFromAPI():
    url = "paste_the_api_url_here"
    my_key = main_functions.read_from_file("JSON_Documents/api_keys.json")
    my_key = my_key_dict["my_ny_key"]

    final_url = url + my_key
    """Maybe you need to provide extra information in the API url"""

    response = requests.get(final_url).json()
    main_functions.save_to_file(response, "JSON_Documents/response.json")
    response_dict = main_functions.read_from_file("JSON_Documents/response.json")

    """From the response dictionary, you need to filter the data requested by the user"""
    return data_requested