import calendar

from datetime import datetime, timedelta
from util.constant import PDF

from dateutil.relativedelta import relativedelta

from logic.energy import Statistics
from util.util import diff_month, next_month, convert_date

from logic.pricematch import PriceMatch
from util.scanned_file import scanned_file

def get_diff(prop, start: datetime, end: datetime, pdf):
    start = start.replace( hour=0, minute=15)
    df = prop.get_clean_data(start, end)
    statistics = Statistics(df, start, end, pdf)
    price = PriceMatch(df, start, end, pdf, percent = 0.001)
    return (price.bill_ver())

def get_statistics(prop, start: datetime, end: datetime, pdf) -> dict:
    start = start.replace( hour=0, minute=15)
    df = prop.get_clean_data(start, end)
    statistics = Statistics(df, start, end, pdf=PDF)
    return statistics.get_data()

def get_total(prop, start: datetime, end: datetime, pdf) -> float:
    start = start.replace( minute=15)
    df = prop.get_clean_data(start, end)
    total_bill = Statistics(df, start, end, pdf=PDF)
    return total_bill.get_final_bill()



