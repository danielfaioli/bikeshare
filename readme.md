THIS IS DANIEL THEREZA FAIOLI's PROJECT
STATS OF BIKESHARE DATA

References:
Pandas documentation: https://pandas.pydata.org/pandas-docs/stable/#
Datetime module documentation: https://docs.python.org/3/library/datetime.html#module-datetime
General posts on Stackoverflow

For the washington dataset is important to take notice that the columns Birth Year and Gender DO NOT EXIST.
In order to deal with this the code has Control Flow statements in the user_stats function.

Docs

# Functions:

## def get_filters () :
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter


##def load_data(city, month, day):
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day

## def station_stats():
## def trip_duration_stats:
## def user_stats():

The three functions above calculate the statistics for station, trip durations and users data. The results are displayed as program output. 

**THX FOR COLABORATING, HOPEFULY THIS WILL HELP SOMEONE LEARN A LITTLE BIT OF PYTHON AS IT HELPED ME.
PEACE!!**