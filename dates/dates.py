# Imports
from datetime import datetime, timedelta


# Function to rewind current date to last day `m` months ago
def get_last_day(months_ago=1, format='%Y-%m-%d'):
    """
    This function rewinds the date back to the last day of the month from
    `months_ago` months ago.
    """

    # Rewind current date `months_ago` times
    ret = datetime.now()
    for i in range(months_ago):
        ret = ret - timedelta(days=ret.day)

    # Return
    return ret.strftime(format)


# Function to rewind current date back to first day from `n` months ago
def get_first_day(months_ago=1, format='%Y-%m-%d'):
    """
    This function rewinds the date back to the first day of the month from
    `months_ago` months ago.
    """

    # Use get_last_day and replace day to 1
    ret = datetime.strptime(
        get_last_day(months_ago=months_ago, format=format),
        format
    ).replace(day=1)

    # Return
    return ret.strftime(format)
