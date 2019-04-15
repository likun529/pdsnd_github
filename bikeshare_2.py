import time
import pandas as pd
import numpy as np

city_list = ["chicago", "new york city", "washington"] #add cities#

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    if answer == 'month':
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        popular_day = df['day_of_week'].mode()[0]
        print('Most Common day of week:', popular_day)
        df['hour'] = df['Start Time'].dt.hour
        popular_hour = df['hour'].mode()[0]
        print('Most Common Start Hour:', popular_hour)
    elif answer == 'day':
        df['month'] = df['Start Time'].dt.month
        popular_month = df['month'].mode()[0]
        print('Most Common Month:', popular_month)
        df['hour'] = df['Start Time'].dt.hour
        popular_hour = df['hour'].mode()[0]
        print('Most Common Start Hour:', popular_hour)
    elif answer == 'both':
        df['hour'] = df['Start Time'].dt.hour
        popular_hour = df['hour'].mode()[0]
        print('Most Common Start Hour:', popular_hour)
    elif answer == 'none':
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        popular_day = df['day_of_week'].mode()[0]
        print('Most Common day of week:', popular_day)
        df['hour'] = df['Start Time'].dt.hour
        popular_hour = df['hour'].mode()[0]
        print('Most Common Start Hour:', popular_hour)
        df['month'] = df['Start Time'].dt.month
        popular_month = df['month'].mode()[0]
        print('Most Common Month:', popular_month)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + df['End Station']
    popular_trip = df['trip'].mode()[0]
    print('Most Common End Station:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time is:',total_travel_time)

    # display mean travel time
    mean_travel_time = np.mean(df['Trip Duration'])
    print('Average travel time is:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if city == 'washington':
        print('No data for Washington')
    elif city == 'new york city' or 'chicago':
        gender = df['Gender'].value_counts()
        print(gender)

    # Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print('No data for Washington')
    elif city == 'new york city' or 'chicago':
        earliest = min(df['Birth Year'])
        print('The earlist year is:', earliest)
        most_recent = max(df['Birth Year'])
        print('The most recent year is:', most_recent)
        most_common = df['Birth Year'].mode()[0]
        print('The most common year of birth is:', most_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('do you want to see raw data? Enter Yes or No')
    answer_raw = input()
    answer_raw = str.lower(answer_raw)
    with open('{}.csv'.format(city)) as myfile:
        while answer_raw == 'yes':
            lines = []
            for i in range(5):
                lines.append(myfile.readline())
            print(lines)
            print('do you want to see raw data? Enter Yes or No')
            answer_raw = input()
            answer_raw = str.lower(answer_raw)

def main():
    df = pd.read_csv('{}.csv'.format(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if answer == 'month':
        print('Which month? January, February, March, April, May or June?')
        month = input()
        month_letter = ['January', 'February', 'March', 'April', 'May', 'June']
        month_number = month_letter.index(month) + 1
        df = df[df['month'] == month_number]
    elif answer == 'day':
        print('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday')
        day = input()
        df = df[df['day_of_week'] == day]
    elif answer == 'both':
        print('Which month? January, February, March, April, May or June?')
        month = input()
        month_letter = ['January', 'February', 'March', 'April', 'May', 'June']
        month_number = month_letter.index(month) + 1
        df = df[df['month'] == month_number]
        print('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday')
        day = input()
        df = df[df['day_of_week'] == day]
    elif answer == 'none':
        df = df
    else:
        print('Sorry, the answer you choose is not in the list, please enter again')
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)

print('Hello! Let\'s explore some US bikeshare data!')
print('Which city would you like to see data for? Chicago, New York City or Washington')
city = str.lower(input())
while city not in city_list:
    print('Sorry, the city you choose is not in the list, please enter again')
    city = input()
    # get user input for date
print('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter')
answer = input()
if __name__ == "__main__":
	main()
