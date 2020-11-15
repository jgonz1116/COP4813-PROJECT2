from Project2_Flask import app, forms
from flask import request, render_template

@app_route('/')
@app.route('/search', methods = ['GET', 'POST'])
def home:
    my_form = forms.NewsForm(request.form)
    if request.method == 'POST':
        format_ = request.form['format_'] # this variable is assigned to the option selected by the user
        """TO BE CONTINUED"""
        # Get the values provided by the user
        # Call the API
        # Generate the requested data

        return_template('results.html')

    render_template('search.html',form=my_form)
