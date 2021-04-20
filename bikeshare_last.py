import pandas as pd
import numpy as np
import time

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months= ['january' , 'february', 'march', 'april', 'may', 'june', 'all']
month = ' '
days= [ 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all' ]
day = ' '


def get_filters():


    print('Hello! Let\'s explore some US bikeshare data!')

    city = input('please choose a city from: chicago or new york city or washington? ').lower()
    while city not in CITY_DATA.keys():
            city = input('please choose a city from: chicago or new york city or washington? ').lower()

    month = input ('please choose a month from january, february, march, april, may or june or type all to not choose any. ').lower()
    while month not in months:
        month = input ('please choose a month from january, february, march, april, may or june or type all to not choose any. ').lower()

    day = input ( 'please choose a day from saturday, sunday, monday, tuesday, wednesday, thursday, friday, or type all to not choose any. ' ).lower()
    while day not in days:
         day = input ( 'please choose a day from saturday, sunday, monday, tuesday, wednesday, thursday, friday, or type all to not choose any. ' ).lower()





    print('-'*40)
    return city, month, day

def load_data(city, month, day):


    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    most_common_month = df['month'].value_counts().idxmax()
    print ( 'The most common month is:', most_common_month )


    most_common_day = df['day'].value_counts().idxmax()
    print ( 'The most common day is:', most_common_day )



    most_common_hour = df['hour'].mode()[0]
    print ( 'The most common hour is:', most_common_hour )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_common_start = df['Start Station'].value_counts().idxmax()
    print ( 'The most common starting station is:', most_common_start )

    most_common_end = df['End Station'].value_counts().idxmax()
    print ( 'The most common ending station is:', most_common_end )

    df['frequent_start_end'] = 'From ' + df['Start Station'] + ' to ' +  df['End Station']
    common = df['frequent_start_end'].value_counts().idxmax()
    print( 'The most frequent combination of starting station and ending station trip is:', common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_time_sec= df['Trip Duration'].sum()
    total_time_hours= total_time_sec / 3600
    print('Total travel time (in hours) is:', total_time_hours)


    mean_time_sec= df['Trip Duration'].mean()
    mean_time_mins= mean_time_sec / 60
    print('Mean travel time (in mins) is:', mean_time_mins)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types=df['User Type'].value_counts()
    print('Counts of different user types are:\n',user_types)

    #CITY_DATA = { 'chicago': 'chicago.csv',
    #          'new york city': 'new_york_city.csv',
    #          'washington': 'washington.csv' }
    #while city == ['washington']:
    #    break
    #    user_gender=df['Gender'].value_counts()
    #    print('Counts of different user genders are:\n',user_gender)
    #else:
    if 'Gender' in df:
        user_gender=df['Gender'].value_counts()
        print('Counts of different user genders are:\n',user_gender)
    else: print('No gender data available')

    if 'Birth Year' in df:
        common_user_birth=df['Birth Year'].value_counts().idxmax()
        print( 'Most common year of birth is:', common_user_birth)

        earliest_user_birth=df['Birth Year'].min()
        print( 'Earliest year of birth is:', earliest_user_birth)
        recent_user_birth=df['Birth Year'].max()
        print( 'Most recent year of birth is:', recent_user_birth)
    else: print('No Birth dates data available')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """The fuction takes the name of the city produced by the get_filters fuction as input and returns the raw data of that city as chunks of 5 rows based upon user input.
    """
    starting_row = 0
    raw_view = input ( 'Displaying raw data is available, would you like to check it?: Yes \n' ).lower()
    while raw_view not in ['yes', 'no']:
        raw_view = input ( 'Displaying raw data is available, would you like to check it?: Yes \n' ).lower()
    while raw_view == 'yes':
        print(df.iloc[starting_row:starting_row+5])
        starting_row += 5
        raw_view = input ( 'Displaying raw data is available, would you like to check it?: Yes \n' ).lower()
    if raw_view == 'no':
        print('\nExiting...')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)


        #print(city, month, day)
        #print(time_stats(df))
        #print(station_stats(df))
        #print(trip_duration_stats(df))
        #print(user_stats(df))
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
