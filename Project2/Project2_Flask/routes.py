from Project2_Flask import app, forms
from flask import request, render_template


@app.route('/', methods=['GET', 'POST'])
def searchReviews():
    my_form = forms.MovieReviewsForm(request.form)
    if request.method == 'POST':
        keyword = request.form['keyword']  # this variable is assigned to the option selected by the user
        orderBy = request.form['orderBy']
        critics_Picks = request.form['critics_Picks']
        """TO BE CONTINUED"""
        response = forms.generateDataFromAPI(keyword, orderBy, critics_Picks)
        # Get the values provided by the user
        # Call the API
        # Generate the requested data
        return render_template('results.html', titles=response["titles"], critics=response["critics"], publicationDates=response["publicationDates"], reviewLinks=response["reviewLinks"], len=len(response["titles"]))

    return render_template('search.html', form=my_form)


@app.route('/searchResults')
def reviewResults():
    return render_template('results.html')
