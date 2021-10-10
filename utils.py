import numpy as np
from datetime import datetime as dt
from datetime import timedelta, date
import holidays

date_fomat = '%Y-%m-%d'

def hsr_waiting_period_end_date(start_date, country='UnitedStates', n_days=30):
    """
    start_date: filing start date, string like '2021-01-20'
    country: country of filing, for holiday purposes
    n_days: the waiting period number of days
    """

    holiday_list = holidays.CountryHoliday(country)
    start_date_dt = dt.strptime(start_date, date_fomat)
    end_date = start_date_dt + timedelta(n_days)
    done = False
    candidates = []
    while not done:
        end_date_str = dt.strftime(end_date, date_fomat)
        if end_date.weekday() == 5:
            candidates.append((end_date_str, 'Saturday'))
            end_date += timedelta(1)
        elif end_date.weekday() == 6:
            candidates.append((end_date_str, 'Sunday'))
            end_date += timedelta(1)
        elif end_date in holiday_list:
            candidates.append((end_date_str, holiday_list.get(end_date_str)))
            end_date += timedelta(1)
        else:
            done = True
    return end_date_str, candidates
