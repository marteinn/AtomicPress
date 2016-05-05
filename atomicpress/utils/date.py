# -*- coding: utf-8 -*-

"""
atomicpress.utils.date
----------
Common date calculation helpers
"""


def get_months_apart(d1, d2):
    """
    Get amount of months between dates
    http://stackoverflow.com/a/4040338
    """

    return (d1.year - d2.year)*12 + d1.month - d2.month


def get_month_list(to_date, from_date):
    """
    Generate a list containing year+month between two dates.

    Returns:
        [(2013, 11), (2013, 12), (2014, 1)]
    """

    num_months = get_months_apart(to_date, from_date)
    month_offset = from_date.month
    month_list = []
    for month in range(month_offset-1, month_offset+num_months):
        year = from_date.year+(month/12)
        real_month = (month % 12) + 1
        month_list.append((year, real_month))

    return month_list
