from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, InputRequired
import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)


class CafeForm(FlaskForm):
    input_required = InputRequired(message="Input Required.")
    url_required =  URL(message="URL required.")
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), url_required])
    open_time = StringField("Opening Time", validators=[DataRequired()])
    close_time = StringField("Closing Time", validators=[DataRequired()])
    coffee_rating = SelectField(label="Coffee Rating", 
                                choices=["✘",
                                        "☕", 
                                        "☕☕", 
                                        "☕☕☕", 
                                        "☕☕☕☕", 
                                        "☕☕☕☕☕"],
                                validators=[DataRequired()])
    wifi_strength = SelectField(label="Wifi Strength", 
                                choices=["✘",
                                         "📶",
                                         "📶📶",
                                         "📶📶📶",
                                         "📶📶📶📶",
                                         "📶📶📶📶📶"],
                                validators=[DataRequired()])
    power_sockets_available = SelectField(label="Power Sockets Available", 
                                          choices=["✘",
                                                   "🔌",
                                                   "🔌🔌",
                                                   "🔌🔌🔌",
                                                   "🔌🔌🔌🔌",
                                                   "🔌🔌🔌🔌🔌"],
                                          validators=[DataRequired()])
    submit = SubmitField("Submit")

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding="utf-8") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open_time.data},"
                           f"{form.close_time.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_strength.data},"
                           f"{form.power_sockets_available.data}")

        # My attempt. It worked, but always added an empty line. I was unable to 
        # figure out how to slve this issue.
        
        # new_data = form.data
        # new_row = [value for (key, value) in new_data.items() if not key in ['submit','csrf_token']]
        # with open('cafe-data.csv', mode="a+", newline='', encoding='utf-8') as csv_file:
        #     csv_data = csv.reader(csv_file, delimiter=",")
        #     csv_file.write("\n")
        #     wr = csv.writer(csv_file)
        #     wr.writerow(new_row)

        return redirect(url_for('cafes'))

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)



if __name__ == '__main__':
    app.run(debug=True)
