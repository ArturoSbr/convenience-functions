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
