import datetime
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city=input("Please input the name of the city of which you want to explore bikeshare data among Chicago,New York,Washington:").lower()
    if(city=='chicago'):
        return 'chicago.csv'
    elif(city=='new york'):
        return 'new_york_city.csv'
    elif(city=='washington'):
        return 'chicago.csv'
    else:
        print("You have not wriiten the appropriate spelling of the city or you have entered an invalid city name.Retry!!!!!!")
    return get_city()
    
def get_time_period():
    time_period=input("Would you like to filter the data by month,day or no filter at all,Type none for no filter?").lower()
    if (time_period=='month'):
        return['month',get_month()]
    elif (time_period=='day'):
        return['day',get_day()]
    elif (time_period=='none'):
        return['none','no filter']
    else:
        print("You have entered an inappropriate input..Please input again!!!!")
        return get_time_period()

def get_month():
    month=input("On which filter do you want to apply the filter,January,February,March,April,May,June\n'").lower()
    if(month=='January'):
       return('01')
    elif(month=='February'):
       return('02')
    elif(month=='March'):
       return('03')
    elif(month=='April'):
       return('04')
    elif(month=='May'):
       return('05')    
    elif(month=='June'):
       return('06')
    else:
       print("Sorry!!!but you have entered an invalid input so please recheck the spelling and input again correctly")
       return get_month()   
    

def get_day():
       day=input("On which day you want to apply the filter,Monday,Tuesday,Wednesday,Thursday,Fridday,Saturday?").lower()
       if(day=='Monday'):
           return(0)
       elif(day=='Tuesday'):
           return(1)
       elif(day=='Wednesday'):
           return(2)
       elif(day=='Thursday'):
           return(3)
       elif(day=='Friday'):
           return(4)
       elif(day=='Saturday'):
           return(5)
       elif(day=='Sunday'):
           return(6)
       else:
           print("You have inputted an wrong day.Try Again")
       return get_day()


    
def most_popular_month(df):
    most_trips_by_month=df.groupby('Month')['Start Time'].count()
    return ("Most popular month for the  start time: "+ calendar.month_name[int(most_trips_by_month.sort_values(ascending=False).index[0])])
def most_popular_day(df):
    most_trips_by_day=df.groupby('Day')['Start Time'].count()
    return ("Most popular day of week for start time: "+ calendar.day_name[int(most_trips_by_day.sort_values(ascending=False).index[0])])

def most_popular_hour(df):
    most_trips_by_hour=df.groupby('Hour')['Start Time'].count()
    most_popular_hour_int = most_trips_by_hour.sort_values(ascending=False).index[0]
    d = datetime.datetime.strptime(most_popular_hour_int, "%H")
    return ("Most popular hour of the day for start time: " + d.strftime("%I %p"))

def Duration_of_trip(df):
    total_trip_duration = df['Trip Duration'].sum()
    avg_trip_duration = df['Trip Duration'].mean()
    m, s = divmod(total_trip_duration, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)
    total_trip_duration = "\nTotal trip duration: %d years %02d days %02d hrs %02d min %02d sec" % (y, d, h, m, s)
    m, s = divmod(avg_trip_duration, 60)
    h, m = divmod(m, 60)
    avg_trip_duration = "Average trip duration: %d hrs %02d min %02d sec" % (h, m, s)
    return [total_trip_duration, avg_trip_duration]
def popular_stations(df):
    start_station_counts = df.groupby('Start Station')['Start Station'].count()
    end_station_counts = df.groupby('End Station')['End Station'].count()
    sorted_start_stations = start_station_counts.sort_values(ascending=False)
    sorted_end_stations = end_station_counts.sort_values(ascending=False)
    total_trips = df['Start Station'].count()
    most_popular_start_station = "\nMost popular start station: " + sorted_start_stations.index[0] + " (" +       str(sorted_start_stations[0]) + " trips, " + '{0:.2f}%'.format(((sorted_start_stations[0]/total_trips) * 100)) + " of trips)"
    most_popular_end_station = "Most popular end station: " + sorted_end_stations.index[0] + " (" + str(sorted_end_stations[0]) + " trips, " + '{0:.2f}%'.format(((sorted_end_stations[0]/total_trips) * 100)) + " of trips)"
    return [most_popular_start_station, most_popular_end_station]


def popular_trip(df):
    
    trip_counts = df.groupby(['Start Station', 'End Station'])['Start Time'].count()
    sorted_trip_stations = trip_counts.sort_values(ascending=False)
    total_trips = df['Start Station'].count()
    return "Most popular trip: " + "\n  Start station: " + str(sorted_trip_stations.index[0][0]) + "\n  End station: " + str(sorted_trip_stations.index[0][1]) + "\n  (" + str(sorted_trip_stations[0]) +  " trips, " + '{0:.2f}%'.format(((sorted_trip_stations[0]/total_trips) * 100)) + " of trips)"


def users(df):
    
    user_type_counts = df.groupby('User Type')['User Type'].count()
    return user_type_counts


def gender(df):
    
    gender_counts = df.groupby('Gender')['Gender'].count()
    return gender_counts


def birth_years(df):
    
    earliest_birth_year = "Earliest birth year: " + str(int(df['Birth Year'].min()))
    most_recent_birth_year = "Most recent birth year: " + str(int(df['Birth Year'].max()))
    birth_year_counts = df.groupby('Birth Year')['Birth Year'].count()
    sorted_birth_years = birth_year_counts.sort_values(ascending=False)
    total_trips = df['Birth Year'].count()
    most_common_birth_year = "Most common birth year: " + str(int(sorted_birth_years.index[0])) + " (" + str(sorted_birth_years.iloc[0]) + " trips, " + '{0:.2f}%'.format(((sorted_birth_years.iloc[0]/total_trips) * 100)) + " of trips)"
    return [earliest_birth_year, most_recent_birth_year, most_common_birth_year]


def display_data(df, current_line):
    
    display = input('\nWould you like to view individual trip data?'
                    ' Type \'yes\' or \'no\'.\n')
    display = display.lower()
    if display == 'yes' or display == 'y':
        print(df.iloc[current_line:current_line+5])
        current_line += 5
        return display_data(df, current_line)
    if display == 'no' or display == 'n':
        return
    else:
        print("\nI'm sorry, I'm not sure if you wanted to see more data or not!!! Let's try again.")
        return display_data(df, current_line)


def statistics():
    city = get_city()
    city_df = pd.read_csv(city)

    def get_day_of_week(str_date):
        date_obj = datetime.date(int(str_date[0:4]), int(str_date[5:7]), int(str_date[8:10]))
        return date_obj.weekday() 
    city_df['Day'] = city_df['Start Time'].apply(get_day_of_week)
    city_df['Month'] = city_df['Start Time'].str[5:7]
    city_df['Hour'] = city_df['Start Time'].str[11:13]

    
    time_period = get_time_period()
    filter_period = time_period[0]
    filter_period_value = time_period[1]
    filter_period_label = 'No filter'

    if filter_period == 'none':
        filtered_df = city_df
    elif filter_period == 'month':
        filtered_df = city_df.loc[city_df['Month'] == filter_period_value]
        filter_period_label = calendar.month_name[int(filter_period_value)]
    elif filter_period == 'day':
        filtered_df = city_df.loc[city_df['Day'] == filter_period_value]
        filter_period_label = calendar.day_name[int(filter_period_value)]


    print('\n')
    print(city[:-4].upper().replace("_", " ") + ' -- ' + filter_period_label.upper())
    print('-------------------------------------')

    #To give some context, print the total number of trips for this city and filter
    print('Total trips: ' + "{:,}".format(filtered_df['Start Time'].count()))

    # What is the most popular month for start time?
    if filter_period == 'none' or filter_period == 'day':
        print(most_popular_month(filtered_df))

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if filter_period == 'none' or filter_period == 'month':
        print(most_popular_day(filtered_df))

    # What is the most popular hour of day for start time?
    print(most_popular_hour(filtered_df))

    # What is the total trip duration and average trip duration?
    trip_duration_stats = Duration_of_trip(filtered_df)
    print(trip_duration_stats[0])
    print(trip_duration_stats[1])

    # What is the most popular start station and most popular end station?
    most_popular_stations = popular_stations(filtered_df)
    print(most_popular_stations[0])
    print(most_popular_stations[1])

    # What is the most popular trip?
    print(popular_trip(filtered_df))

    # What are the counts of each user type?
    print('')
    print(users(filtered_df))

    if city == 'chicago.csv' or city == 'new_york_city.csv': #only those two files have this data
        # What are the counts of gender?
        print('')
        print(gender(filtered_df))
        # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
        # most popular birth years?
        birth_years_data = birth_years(filtered_df)
        print('')
        print(birth_years_data[0])
        print(birth_years_data[1])
        print(birth_years_data[2])

    # Display five lines of data at a time if user specifies that they would like to
    display_data(filtered_df, 0)

    # Restart?
    def restart_question():
        '''Conditionally restarts the program based on the user's input
        Args:
            none.
        Returns:
        '''
        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'. (If you say no it will end the program.)\n')
        if restart.lower() == 'yes' or restart.lower() == 'y':
            statistics()
        elif restart.lower() == 'no' or restart.lower() == 'n':
            return
        else:
            print("\nI'm not sure if you wanted to restart or not. Let's try again.")
            return restart_question()

    restart_question()


if __name__ == "__main__":
    statistics()
