import calendar
from datetime import datetime, timedelta, date
from calendar import monthrange

import pandas as pd
from dateutil.relativedelta import *

from ga_mimic import GA


def next_month(start):
    end_of_month = start + relativedelta(months=1) - timedelta(seconds=1)
    return end_of_month


def scrape_total_ga(year: int, month: int, count=5) -> float:

    try:
        ga_value = GA.objects.get(date=date(year=year, month=month, day=1)).ga_value
    except:
        if not count:
            return
        ga_value = scrape_total_ga(year=year, month=month-1, count=count-1)
    return ga_value


def find_max(df: pd.DataFrame, column: str = 'value') -> float:
    """
    find max consumption in month
    :param df: desired dataframe with structure(index: datetime, value: float)
    :param column: value column (default is value in our API)
    :return: float or None for maximum consumption
    """
    return df.groupby([df.index.year, df.index.month]).max()[column]


def find_sum(df: pd.DataFrame, column: str = 'value') -> float:
    """
    find sum of consumptions in dataframe
    :param df: desired dataframe with structure(index: datetime, value: float)
    :param column: value column (default is value in our API)
    :return: float or None for summation of consumptions
    """
    return df.groupby([df.index.year, df.index.month]).sum()[column]


def get_month(df: pd.DataFrame) -> int:
    months = df.index.month.unique()
    return months


def get_year(df: pd.DataFrame) -> int:
    years = df.index.year.unique()
    return years


def convert_date(date: datetime):
    """
    for some modules we need to split a date to complete month, it means: start-end of that month
    :param date: desired date
    :return: start and end of its month
    """
    start_date = (date - timedelta(days=30)).replace(day=1)
    end_date = start_date.replace(day=calendar.monthrange(start_date.year, start_date.month)[1])

    return start_date, end_date


def diff_month(end, start) -> int:
    """
    get different month between two dates
    :param end:
    :param start:
    :return:
    """
    return (end.year - start.year) * 12 + end.month - start.month


def diff_days(start: datetime, end: datetime) -> int:
    """
    get the number of days between two dates
    :param end:
    :param start:
    :return:
    """
    return ((end - start).days)+1


def adjust_constant(start, end) -> float:
    """
    calculate a coefficient basd on number of days in a month to adjuste the constants
    :param get_month : get a month from get_month function
    :return :
    """
    return diff_days(start, end) / 30



