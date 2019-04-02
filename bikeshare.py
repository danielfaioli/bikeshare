import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        #check if input is correct
        city = str(input('Enter the city name: ')).lower()

        if city not in CITY_DATA:
            print('Sorry, We\'re not available is this city yet.')
            continue
        else:
            #exit the loop
            break
    #Month input
    month = str(input('Enter the desired month: ').lower())
    # Day input
    day = str(input('Enter the desired day of the week: '))
    # Dataset size
    dset_size = int(input('Type the desired dataset sample size to look at: '))

    print('-'*40)
    return city, month, day, dset_size


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Get data
    df = pd.read_csv(CITY_DATA[city])

    #Convert Star Time and End Time to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #Create columns Month, Day, Day of the Week, Start Hour
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['Week_day'] = df['Start Time'].dt.weekday_name

    #Filters data by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june',
                  'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    #Filters by day of the week
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Week_day'] == day.title()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Most common month
    month_mode = df.month.mode()
    print('Most frequent month:',month_mode)
    #Most common day of week
    day_mode = df.Week_day.mode()
    print('Most common day of the week:',day_mode)
    #Most common start hour
    hour_mode = df.hour.mode()
    print('Most frequent hour:',hour_mode)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Most commonly used start station
    DPstation_mode = df['Start Station'].mode()
    #Most commonly used end station
    ARVstation_mode = df['End Station'].mode()
    #Most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' - ' + df['End Station']
    trip_mode = df.trip.mode()

    #Saída
    print('Most common:\nStart Station:{}\nEnd Station:{}\nTrip:{}'.format(DPstation_mode,ARVstation_mode,trip_mode))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    #Convert column type
    df['Trip Duration'] = df['Trip Duration'].astype('float64')
    
    #Display total travel time
    trip_total = df['Trip Duration'].sum()
    #Display mean travel time
    trip_mean = df['Trip Duration'].mean()

    print('Total travel time: {}sec\nMean travel time:{}sec'.format(trip_total,trip_mean))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Counts of user types
    usr_types = df['User Type'].value_counts()
    usrdf = pd.DataFrame(usr_types)
    usrdf.rename(index=str, columns={"User Type": "Count"}, inplace=True)
    print('Counts of User Types:\n', usrdf)

    #Counts of gender - if City == NYC or CHICAGO
    if city == 'washington':
        pass
    else:
        gender = df['Gender'].value_counts()
        genderdf = pd.DataFrame(gender)
        genderdf.rename(index=str, columns={"Gender": "Count"}, inplace=True)
        print('\nCounts of User Gender:\n', genderdf)

    #Earliest, most recent, and most common year of birth - if city == NYC or CHICAGO
    if city == 'washington':
        pass
    else:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        year_mode = df['Birth Year'].mode()
        print('\nUser Birth Data:\nEarliest Year: {}\nMost Recent Year: {}\nMost Common Year of Birth: {}'.format(earliest,most_recent,year_mode))
    
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day, dset_size = get_filters()
        df = load_data(city, month, day)

        pd.set_option('display.max_rows', dset_size)
        pd.set_option('display.max_columns', 13)
        print(df)


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
