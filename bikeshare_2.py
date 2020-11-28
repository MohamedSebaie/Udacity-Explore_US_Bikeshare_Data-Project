import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv','new york city': 'new_york_city.csv','washington': 'washington.csv' }

MONTH_DATA = ['january','february','march','april','may','june']

DAYS_DATA = {'sunday':'1','monday':'2','tuesday':'3','wednesday':'4','thursday':'5','friday':'6','saturday':'7',"all":"all"}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which City You Would Like To Analyze? Chicago, New York City or Washington?').lower().strip()
    while city not in CITY_DATA:
        print('SORRY There Is a typo Mistake, Please Check Your Spelling Again!')
        city = input('Which City You Would Like To Analyze? Chicago, New York City or Washington?').lower().strip()
    
    print(city)
    

    # get user input for month (all, january, february, ... , june)
    month = input('Which Month You Would Like To Analyse? (All, January, February, ... , June)!!').lower().strip()
    while month not in MONTH_DATA:
        print('SORRY There Is a typo Mistake, Please Check Your Spelling Again!')
        month = input('Which Month You Would Like To Analyse? (All, January, February, ... , June)').lower().strip()

    print(month)
   

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which Day You Would Like To Analyse?(All,Sunday, Monday, ...,Saturday)!!Please Enter The Days As Integer(eg.Sunday=1)').strip()
    while day not in DAYS_DATA.values():
        print('SORRY There Is a Mistake, Please Check  Again!')
        day = input('Which Day You Would Like To Analyse? (All,Sunday, Monday, ...,Saturday)!!Please Enter The Days As Integer(eg.Sunday=1)').strip()

    print(day)

    return city, month, day
    print('-'*40)
    
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
    # load data file into a dataframe
    df= pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # convert the End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract month and day from the Start Time column to create a month and a day columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        
        # filter by day of week to create the new dataframe
        df = df[df['day'] == int(day)] 
    
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month_num = df['month'].mode()[0]
    popular_month = MONTH_DATA[popular_month_num-1].title()
    
    print('Most Common Month:', popular_month)

    # display the most common day of week
    popular_day_num = df['day'].mode()[0]
    popular_day = list(DAYS_DATA.keys())[list(DAYS_DATA.values()).index(str(popular_day_num))].title()  
    
    print('Most Common Day:', popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_used_Start_Station = df['Start Station'].mode()[0]

    print('Most Common Used Start Station Is:\n', common_used_Start_Station)

    # display most commonly used end station
    common_used_End_Station = df['Start Station'].mode()[0]

    print('Most Common Used End Station Is:\n', common_used_End_Station)


    # display most frequent combination of start station and end station trip
    common_used_trip = df[['Start Station','End Station']].mode()

    print('Most Common Used Trip Is:\n', common_used_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print("The Total Travel Time In Seconds Is:\n",total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print("The Mean Travel Time In Seconds Is:\n",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print("Counts of User Types Are :\n ",user_types)

    # Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()

        print("Counts of Gender Are :\n ",gender_counts)

    # Display earliest, most recent, and most common year of birth
        min_birth = df['Birth Year'].min()
        max_birth = df['Birth Year'].max()
        popular_birth = df['Birth Year'].mode()[0]
        print("The Most Recent Year Of Birth Is:\n ", max_birth)
        print("The Earliest Year Of Birth Is:\n ", min_birth)
        print('The Most Common Year Of Birth Is:\n', popular_birth)
        
    except Exception as error:
        print('_'*100)
        print('Couldn\'t Find The Gender And Birth Year Of Our Customers!!, as an Error occurred: {}'.format(error))
        print('_'*100)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_the_data(df):
    
    #Display contents of the CSV file as requested by the user.

    start_loc = 0
    end_loc = 5

    display = input("Do You Want To Display The Raw Data?: ").lower().strip()

    if display == 'yes':
        while end_loc <= df.shape[0] - 1:

            print(df[start_loc:end_loc])
            start_loc += 5
            end_loc += 5

            end_display = input("Would you like to continue?: ").lower().strip()
            if end_display == 'no':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_the_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
