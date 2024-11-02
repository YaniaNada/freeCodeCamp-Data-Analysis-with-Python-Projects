import pandas as pd
from collections import Counter

def calculate_demographic_data(print_data=True):
    # Read data from file
    dataframe = pd.read_csv('demographic-data-analyzer/adult_data.csv')
    df = pd.DataFrame(dataframe)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count_dict = Counter(df['race'])
    race_count = pd.Series(race_count_dict)

    # What is the average age of men?
    filtered_df = df[df['sex'] == 'Male']
    average_age_men = round(filtered_df['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(((df[df['education'] == 'Bachelors'].shape[0])/df['education'].shape[0])*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df['education'] == 'Bachelors') | (df['education'] == "Masters") | (df['education'] == "Doctorate")]
    lower_education = df[(df['education'] != 'Bachelors') & (df['education'] != "Masters") & (df['education'] != "Doctorate")]
    
    # percentage with salary >50K
    filtered_df = higher_education[(higher_education['salary']== '>50K')] 
    higher_education_rich = round((filtered_df.shape[0]/higher_education.shape[0])*100, 1)
    
    filtered_df = lower_education[(lower_education['salary']== '>50K')] 
    lower_education_rich =round((filtered_df.shape[0]/lower_education.shape[0])*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    filtered_df = df[(df['hours-per-week'] == 1) & (df['salary']== '>50K')]
    num_min_workers = filtered_df.shape[0]
    rich_percentage = (filtered_df.shape[0]/df[(df['hours-per-week'] == 1)].shape[0])*100

    # What country has the highest percentage of people that earn >50K?
    temp_df = df[(df['salary']== '>50K')]
    count_temp_df = temp_df['native-country'].value_counts()
    count_total = df['native-country'].value_counts()
    percentage_high_salary = (count_temp_df/count_total)*100
    highest_earning_country = percentage_high_salary.idxmax()
    highest_earning_country_percentage = round(percentage_high_salary.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    df_IN = temp_df[(temp_df['native-country'] == 'India')]
    top_occupation = df_IN['occupation'].value_counts()
    top_IN_occupation = top_occupation.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }