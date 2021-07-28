
import time
import pandas as pd


city_data = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
city_range = {'chicago', 'new york city', 'washington'}
month_range = {'january', 'february', 'march', 'april', 'may', 'june'}
time_range = {'month', 'day', 'both', 'none'}
day_range = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
answer_range = {'yes', 'no'}


def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bike share data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please tell me your city name: Chicago, New York City, Washington?").lower()
        if city not in city_range:
            print("That is not correct!\n")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        filter_input = input("How should we filter the results: month, day, both or none.").lower()
        if filter_input.lower() not in time_range:
            print("That is not correct!\n")
            continue
        if filter_input == 'month':
            month = input("Please tell me which month: January, February, March, April, May or June.").lower()
            if month.lower() not in month_range:
                print("That is not correct!\n")
                continue
            day = 'all'
            break

        elif filter_input == 'day':
            month = 'all'
            day = input(
                "Please tell me which day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday.").lower()
            if day.lower() not in day_range:
                print("That is not correct!\n")
                continue
            break

        elif filter_input == 'both':
            month = input("Please tell me which month: January, February, March, April, May or June.").lower()
            if month.lower() not in month_range:
                print("That is not correct!\n")
                continue
            day = input(
                "Please tell me which day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday.").lower()
            if day.lower() not in day_range:
                print("That is not correct!\n")
                continue
            break
        elif filter_input == 'none':
            month = 'all'
            day = 'all'
            break
        else:
            input("That is not correct. Please enter: month, day, all or none.")
            break

    print(city)
    print(month)
    print(day)
    print('-' * 40)
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

    df = pd.read_csv(city_data[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
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
    print("The most common month is:", common_month)
    month_count = df['month'].value_counts()
    print("Providing mount counts:\n", month_count)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of the week is:", common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("The most common hour is:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("The most common start station is:", common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("The most common end station is:", common_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print("The most common combination is:", common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("The total travel time is:", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("The mean travel time is:", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bike share users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The counts of user type are:\n", user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print("The gender counts are:\n", gender)
    else:
        print("No gender information available for your selection.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        common_birth = df['Birth_Year'].mode()[0]
        print("The most common birth year is:", common_birth)
        earliest = df['Birth_Year'].min()
        print("The earliest birth year is:", earliest)
        recent = df['Birth_Year'].max()
        print("The latest birth year is:", recent)

    else:
        print("No birth information available for your selection.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def raw_data(df):
    rd_input = 0
    while True:
        first_attempt = input("Provide the raw data? Yes or No").lower()
        if first_attempt not in answer_range:
            input("Incorrect entry. Type Yes or No.").lower()
        elif first_attempt == 'yes':
            rd_input += 5
            print(df.iloc[rd_input: rd_input + 5])
            second_attempt = input("Provide more raw data? Yes or No").lower()
            if second_attempt not in answer_range:
                second_attempt = input("Incorrect entry. Type Yes or No.").lower()
            elif second_attempt == 'yes':
                rd_input += 5
                print(df.iloc[rd_input: rd_input + 5])
            if second_attempt == 'no':
                break
        elif first_attempt == 'no':
            return


def main():
    city = ""
    month = ""
    day = ""
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()


import time
import pandas as pd


city_data = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
city_range = {'chicago', 'new york city', 'washington'}
month_range = {'january', 'february', 'march', 'april', 'may', 'june'}
time_range = {'month', 'day', 'both', 'none'}
day_range = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
answer_range = {'yes', 'no'}


def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bike share data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please tell me your city name: Chicago, New York City, Washington?").lower()
        if city not in city_range:
            print("That is not correct!\n")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        filter_input = input("How should we filter the results: month, day, both or none.").lower()
        if filter_input.lower() not in time_range:
            print("That is not correct!\n")
            continue
        if filter_input == 'month':
            month = input("Please tell me which month: January, February, March, April, May or June.").lower()
            if month.lower() not in month_range:
                print("That is not correct!\n")
                continue
            day = 'all'
            break

        elif filter_input == 'day':
            month = 'all'
            day = input(
                "Please tell me which day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday.").lower()
            if day.lower() not in day_range:
                print("That is not correct!\n")
                continue
            break

        elif filter_input == 'both':
            month = input("Please tell me which month: January, February, March, April, May or June.").lower()
            if month.lower() not in month_range:
                print("That is not correct!\n")
                continue
            day = input(
                "Please tell me which day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday.").lower()
            if day.lower() not in day_range:
                print("That is not correct!\n")
                continue
            break
        elif filter_input == 'none':
            month = 'all'
            day = 'all'
            break
        else:
            input("That is not correct. Please enter: month, day, all or none.")
            break

    print(city)
    print(month)
    print(day)
    print('-' * 40)
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

    df = pd.read_csv(city_data[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
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
    print("The most common month is:", common_month)
    month_count = df['month'].value_counts()
    print("Providing mount counts:\n", month_count)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of the week is:", common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("The most common hour is:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("The most common start station is:", common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("The most common end station is:", common_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print("The most common combination is:", common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("The total travel time is:", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("The mean travel time is:", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bike share users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The counts of user type are:\n", user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print("The gender counts are:\n", gender)
    else:
        print("No gender information available for your selection.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        common_birth = df['Birth_Year'].mode()[0]
        print("The most common birth year is:", common_birth)
        earliest = df['Birth_Year'].min()
        print("The earliest birth year is:", earliest)
        recent = df['Birth_Year'].max()
        print("The latest birth year is:", recent)

    else:
        print("No birth information available for your selection.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def raw_data(df):
    rd_input = 0
    while True:
        first_attempt = input("Provide the raw data? Yes or No").lower()
        if first_attempt not in answer_range:
            input("Incorrect entry. Type Yes or No.").lower()
        elif first_attempt == 'yes':
            rd_input += 5
            print(df.iloc[rd_input: rd_input + 5])
            second_attempt = input("Provide more raw data? Yes or No").lower()
            if second_attempt not in answer_range:
                second_attempt = input("Incorrect entry. Type Yes or No.").lower()
            elif second_attempt == 'yes':
                rd_input += 5
                print(df.iloc[rd_input: rd_input + 5])
            if second_attempt == 'no':
                break
        elif first_attempt == 'no':
            return


def main():
    city = ""
    month = ""
    day = ""
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()


### Making some changes per step 3.B. in Git Lesson


import time
import pandas as pd


city_data = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
city_range = {'chicago', 'new york city', 'washington'}
month_range = {'january', 'february', 'march', 'april', 'may', 'june'}
time_range = {'month', 'day', 'both', 'none'}
day_range = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
answer_range = {'yes', 'no'}


def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bike share data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please tell me your city name: Chicago, New York City, Washington?").lower()
        if city not in city_range:
            print("That is not correct!\n")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        filter_input = input("How should we filter the results: month, day, both or none.").lower()
        if filter_input.lower() not in time_range:
            print("That is not correct!\n")
            continue
        if filter_input == 'month':
            month = input("Please tell me which month: January, February, March, April, May or June.").lower()
            if month.lower() not in month_range:
                print("That is not correct!\n")
                continue
            day = 'all'
            break

        elif filter_input == 'day':
            month = 'all'
            day = input(
                "Please tell me which day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday.").lower()
            if day.lower() not in day_range:
                print("That is not correct!\n")
                continue
            break

        elif filter_input == 'both':
            month = input("Please tell me which month: January, February, March, April, May or June.").lower()
            if month.lower() not in month_range:
                print("That is not correct!\n")
                continue
            day = input(
                "Please tell me which day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday.").lower()
            if day.lower() not in day_range:
                print("That is not correct!\n")
                continue
            break
        elif filter_input == 'none':
            month = 'all'
            day = 'all'
            break
        else:
            input("That is not correct. Please enter: month, day, all or none.")
            break

    print(city)
    print(month)
    print(day)
    print('-' * 40)
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

    df = pd.read_csv(city_data[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
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
    print("The most common month is:", common_month)
    month_count = df['month'].value_counts()
    print("Providing mount counts:\n", month_count)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of the week is:", common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("The most common hour is:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("The most common start station is:", common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("The most common end station is:", common_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print("The most common combination is:", common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("The total travel time is:", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("The mean travel time is:", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bike share users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The counts of user type are:\n", user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print("The gender counts are:\n", gender)
    else:
        print("No gender information available for your selection.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        common_birth = df['Birth_Year'].mode()[0]
        print("The most common birth year is:", common_birth)
        earliest = df['Birth_Year'].min()
        print("The earliest birth year is:", earliest)
        recent = df['Birth_Year'].max()
        print("The latest birth year is:", recent)

    else:
        print("No birth information available for your selection.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def raw_data(df):
    rd_input = 0
    while True:
        first_attempt = input("Provide the raw data? Yes or No").lower()
        if first_attempt not in answer_range:
            input("Incorrect entry. Type Yes or No.").lower()
        elif first_attempt == 'yes':
            rd_input += 5
            print(df.iloc[rd_input: rd_input + 5])
            second_attempt = input("Provide more raw data? Yes or No").lower()
            if second_attempt not in answer_range:
                second_attempt = input("Incorrect entry. Type Yes or No.").lower()
            elif second_attempt == 'yes':
                rd_input += 5
                print(df.iloc[rd_input: rd_input + 5])
            if second_attempt == 'no':
                break
        elif first_attempt == 'no':
            return


def main():
    city = ""
    month = ""
    day = ""
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

