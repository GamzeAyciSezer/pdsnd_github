import time
# numpy and pandas used for numerical analysis. 
import pandas as pd

import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',

              'new york city': 'new_york_city.csv',

              'washington': 'washington.csv' }


# MONTHS and DAYS are global variables. These variables are used in functions when needed.

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']


# city, month, and day variables are not case-sensitive.

# TO DO: get user input for month (all, january, february, ... , june)

def find_month():

    while True:

        month = input("\nWhich month? January, February, March, April, May, or June? \n")

        month = month.lower() 


        if month in MONTHS: 

            break

        else:

            print("Sorry, the month value is " + str(month) + " so I didn't find the valid month. Please try again.")

            continue


    return month



# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

# I use numeric values described in demo video. The numbers between 1 and 7 refer to the weekdays by starting Sunday.

def find_day():

    while True:

        day = int(input("\nWhich day? Please type your response as an integer which is between 1 and 7 (e.g. 1=Sunday).\n"))


        if day in list(range(1,8,1)):

            day = DAYS[day-1]

            break

        else:

            print("Sorry, the value is " + str(day) + " so I didn't find the valid day. Please try again.")

            continue


    return day

    

    

def get_filters():

    """

    Asks user to specify a city, month, and day to analyze.


    Returns:

        (str) city - name of the city to analyze

        (str) month - name of the month to filter by, or "all" to apply no month filter

        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    """

    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:

        city = input("\nWould you like to see data for Chicago, New York City, or Washington?\n")

        city = city.lower()

          

        if city not in ("new york city", "chicago", "washington"):

            print("Sorry, the city value is " +str(city) + " so it is not defined. Please try again.")

            continue

        else:

            break

    

    # This checks the input type which is given from the user. Types of inputs can be "month", "day", "all" (which means both), or "None".

    while True:

        user_input = str(input("\nWould you like to filter the data by month, day, all, or not at all? Type 'None' for no filter \n"))


        if ((user_input == 'month') or (user_input == 'day') or (user_input == 'all') or (user_input == 'None')):

            if user_input == 'all':

                month = find_month()

                day = find_day()

                break

            elif user_input == 'month':

                month = find_month()

                day = 'all'

                break

            elif user_input == 'day':

                day = find_day()

                month = 'all'

                break

            else:

                month = 'all'

                day = 'all'

                break

        else:

            print("Be careful please. Type a valid input.")


    print('-'*40)

    return city, month, day



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

    

    df = pd.read_csv(CITY_DATA[city])

    

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['End Time'] = pd.to_datetime(df['End Time'])

    

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    df["day_of_month"] = df["Start Time"].dt.day

    df['month'] = df['Start Time'].dt.month


    # This part of code filters the dataframe based on preferences of the user.

    if month != 'all':

        month = MONTHS.index(month) + 1


        df = df[df['month'] == month]


    if day != 'all':        

        df = df[df['day_of_week'] == day.title()]


    return df



def time_stats(df):

    """Displays statistics on the most frequent times of travel."""


    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()


    # TO DO: display the most common month

    common_month = df['month'].mode()[0]

    print("The Most Common Month:", common_month)

    

    # TO DO: display the most common day of week

    common_day = df["day_of_week"].mode()[0]

    print("The Most Common day:", common_day)


    # TO DO: display the most common start hour

    df['hour'] = df["Start Time"].dt.hour

    common_hour = df['hour'].mode()[0]

    print("The Most Common Hour:", common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)



def station_stats(df):

    """Displays statistics on the most popular stations and trip."""
     #this code shows print. 

    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()


    # TO DO: display most commonly used start station

    commonly_start_station = df["Start Station"].value_counts().idxmax()

    print("Most Commonly used start station:", commonly_start_station)


    # TO DO: display most commonly used end station

    commonly_end_station = df["End Station"].value_counts().idxmax()

    print("Most Commonly used end station:", commonly_end_station)


    # TO DO: display most frequent combination of start station and end station trip

    commonly_combination_start_end_station = df.groupby(['Start Station','End Station']).size().idxmax()

    print('Most Commonly used combination of start station and end station trip:', commonly_combination_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)



def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    # This statistic average and total trip duration.

    print('\nCalculating Trip Duration...\n')

    start_time = time.time()


    # TO DO: display total travel time

    # You can find the result both in seconds, mins, and days format. 

    total_travel_time = df['Trip Duration'].sum()

    print("Total Travel Time:", total_travel_time, ' seconds,', total_travel_time/60, " minutes,", total_travel_time/60*60*24, " days.")


    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_travel_time, ' seconds,', mean_travel_time/60, " minutes,", mean_travel_time/60*60*24, " days.")


    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)



def user_stats(df):

    """Displays statistics on bikeshare users."""


    print('\nCalculating User Stats...\n')

    start_time = time.time()


    if 'Gender' not in df:

        print('There is no input for Gender and Birth Year')

    else:

        

        # TO DO: Display counts of user types

        user_types = df['User Type'].value_counts()

        print('User Types:\n', user_types)

        

        # TO DO: Display counts of gender

        gender_types = df["Gender"].value_counts()

        print("Gender Types:\n", gender_types)


        # TO DO: Display earliest, most recent, and most common year of birth

        birth_year = df['Birth Year'].dropna()


        earliest_year_birth = np.min(birth_year)

        print('Earliest Year of Birth:\n' , earliest_year_birth)


        most_recent_year_birth = np.max(birth_year)

        print('Most Recent Year of Birth:\n' , most_recent_year_birth)


        most_common_year_birth = birth_year.mode()[0]

        print('Most Common Year of Birth:\n', most_common_year_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

    
def display_raw_data(df):
    
    i = 0

    while True:

        raw_data_request = str(input('Would you like to see some raw data? Enter yes or no.\n'))

        raw_data_request = raw_data_request.lower()

        if raw_data_request == 'yes':

            print(df[i:i+5])

            i += 5

        else:

            break

            
def main():

    while True:

        city, month, day = get_filters()

        df = load_data(city, month, day)


        time_stats(df)

        station_stats(df)

        trip_duration_stats(df)

        user_stats(df)

        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')

        if restart.lower() != 'yes':

            break

      


if __name__ == "__main__":

    main()