from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap5
from functions import main

app = Flask(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'
bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)

class CheckerForm(FlaskForm):
    entered_password = StringField('Enter a password', validators=[DataRequired(), Length(1, 40)])
    submit = SubmitField('Submit')



@app.route("/")
def index():
    return render_template('index.html')


@app.route("/checker_submit", methods=['GET', 'POST'])
def checker_submit():
    form = CheckerForm()
   
    if request.method == "POST":
        if form.validate_on_submit():
            data = request.form.to_dict()
            result = main(data['entered_password'])
            print((result))

            return render_template('checker.html', form=form, result=result)
    
    return render_template('checker.html', form=form)


@app.route("/<string:path>")
def pages(path):
    form = CheckerForm()
    return render_template(path, form=form)

