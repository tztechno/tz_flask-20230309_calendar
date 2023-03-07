import calendar
from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            year = int(request.form['year'])
            month = int(request.form['month'])
            cal = calendar.HTMLCalendar(calendar.MONDAY)
            html_cal = cal.formatmonth(year, month)

            return render_template('index.html', html_cal=html_cal)

        except ValueError:
            result = "Error: Please enter a valid number."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



