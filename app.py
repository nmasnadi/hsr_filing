from flask import Flask, render_template, request
from utils import hsr_waiting_period_end_date
from datetime import datetime as dt

app = Flask(__name__)

def change_date_format(input_date):
    return dt.strftime(dt.strptime(input_date, '%Y-%m-%d'), '%m/%d/%Y')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date_zero = request.form['hsr']
        end_date, candidates = hsr_waiting_period_end_date(date_zero)

        conflicts = ["{} is {}".format(change_date_format(x[0]), x[1]) for x in candidates]
        shift_days=len(candidates)
        if shift_days == 0:
            shift_days_str=""
        elif shift_days == 1:
            shift_days_str="{} day".format(str(shift_days))
        else:
            shift_days_str="{} days".format(str(shift_days))

        return render_template("index.html",
            show_messages=True,
            start_date=change_date_format(date_zero),
            end_date=change_date_format(end_date),
            shift_days=shift_days,
            shift_days_str=shift_days_str,
            conflicts=conflicts)
    else:
        return render_template("index.html", show_messages=False)

if __name__ == '__main__':
    app.run(port=5000)
