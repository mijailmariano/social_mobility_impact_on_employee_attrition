# importing dependencies
import os
import pandas as pd
import numpy as np

from skimpy import clean_columns
import random

# plotting libraries/modules
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = "darkgrid")

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# creating a function to randomly apply county based on the employee's distance from home
def get_county(x, lst_a, lst_b, lst_c, lst_d, lst_e):
        random.seed(548)
        '''where x = employees' work distance from home in miles. 
        function will iterate through all records and randomly assign a county based on distance from work.'''
        lst = []

        if x <= 5:
                county = random.choice(lst_a)
                lst.append(county)

        elif x > 5 and x <= 10:
                county = random.choice(lst_b)
                lst.append(county)

        elif x > 10 and x <= 21:
                county = random.choice(lst_c)
                lst.append(county)
        
        elif x > 27 and x <= 30:
                county = random.choice(lst_e)
                lst.append(county)

        else:
                county = lst_d[0]
                lst.append(county)

        # returning the list of counties
        return lst


def get_employee_df():
    random.seed(548)
    # check for a cached dataset
    filename = "emp_df.csv"
    if os.path.isfile(filename):
        df = pd.read_csv(filename)

    else:
        # importing the two (2) main dataframes (ibm attrition/opportunity atlas data)
        df1 = pd.read_csv("/Users/mijailmariano/Desktop/IBM_HR-Employee-Attrition.csv")
        df2 = pd.read_csv("/Users/mijailmariano/Desktop/equity_table.csv")

        df2["distance"] = df2["distance"].str.replace("miles", "").astype(int)
        
        # creating the county bins
        area_one = df2[df2["distance"] <= 5].county_name.tolist()
        area_two = df2[(df2["distance"] > 5) & (df2["distance"] <= 10)].county_name.tolist()
        area_three = df2[(df2["distance"] > 10) & (df2["distance"] <= 21)].county_name.tolist()
        area_four = df2[(df2["distance"] > 21) & (df2["distance"] <= 27)].county_name.tolist()
        area_five = df2[(df2["distance"] > 27) & (df2["distance"] <= 30)].county_name.tolist()

        # applying the 'get_county()' function to ibm employee df
        county_lst = df1["DistanceFromHome"].apply(get_county, args = (area_one, area_two, area_three, area_four, area_five))
        
        # let's flatten the county list
        county_lst = [val for sublist in county_lst for val in sublist]
        county_lst = pd.Series(county_lst)

        # assing the series to the ibm dataframe
        df1["county_name"] = county_lst

        # merging the two dataframes and dropping unneeded columns
        df = df1.merge(
                        df2,
                        how = "left",
                        left_on = "county_name",
                        right_on = "county_name"
                    ).drop(columns = "distance")

        # creating a cached file for future referencing
        df.to_csv("emp_df.csv")

    # let's print the shape too
    print(f'initial df shape: {df.shape}')

    return df


def clean_employee_df(df):
    # let's normalize the column names
    df = clean_columns(df)

    # setting employee number as the index for future referencing and attrition modeling/predictions
    df = df.set_index("employee_number").sort_index().rename_axis(None)
    
    # pulling needed variables for exploration/analysis
    df = df[[
            'attrition',
            'age',
            'monthly_income',
            'percent_salary_hike',
            'total_working_years',
            'training_times_last_year',
            'years_at_company',
            'household_income_at_35',
            'high_school_graduation_rate',
            'percentage_married_by_35',
            'incarceration_rate',
            'women_teenage_birthrate',
            'poverty_rate',
            'employment_rates_at_35',
            'single_parent_frac',
            'years_since_last_promotion',
            'county_name',
            'department',
            'education',
            'education_field',
            'environment_satisfaction',
            'gender',
            'job_involvement',
            'job_level',
            'job_role',
            'job_satisfaction',
            'marital_status',
            'performance_rating',
            'relationship_satisfaction',
            'state',
            'stock_option_level',
            'work_life_balance',
            'years_in_current_role',
            'years_with_curr_manager']]

    # renaming necessary columns for clarity
    df = df.rename(columns = {"age": "employee_age"})

    # renaming/classifying attrition as boolean value types
    df["attrition"] = df["attrition"].replace({"Yes": True, "No": False})

    # converting continuous variables to discrete type
    disc_lst = [
    'stock_option_level',
    'work_life_balance',
    'education',
    'job_involvement',
    'job_level',
    'job_satisfaction',
    'performance_rating',
    'relationship_satisfaction',
    'county_name',
    'state',
    'department',
    'education_field',
    'gender',
    'job_role',
    'marital_status',
    'environment_satisfaction']

    # setting the data types
    df[disc_lst] = df[disc_lst].astype(object)

    # printing the new df shape
    print(f'shape after cleaning: {df.shape}')

    # lastly, return the dataframe
    return df


'''creating a function to clean outliers at upperbounds'''
def df_outliers(df):

    # monthly income / leadership or seniority
    df = df[df["monthly_income"] <= 16581.00]
    
    # length of working tenure
    df = df[df["total_working_years"] <= 28.00]

    # length of tenure at current company
    df = df[df["years_at_company"] <= 18.00]

    # number of years since last promotion
    df = df[df["years_since_last_promotion"] <= 7.50]

    # number of years in current role 
    df = df[df["years_in_current_role"] <= 14.50]

    # number of year with current manager
    df = df[df["years_with_curr_manager"] <= 14.50]

    # returning the cleaned dataset
    print(f'shape after outliers: {df.shape}')

    return df


'''Function created to split the initial dataset into train, validate, and test datsets'''
def train_validate_test_split(df):
    train_and_validate, test = train_test_split(
    df, test_size = 0.2, random_state = 548)
    
    train, validate = train_test_split(
        train_and_validate,
        test_size = 0.3,
        random_state = 548)

    print(f'train shape: {train.shape}')
    print(f'validate shape: {validate.shape}')
    print(f'test shape: {test.shape}')

    return train, validate, test

'''Function created to scale continuous data for modeling'''
def scaled_data(df):
    # selecting features to scale
    scale_lst = df.select_dtypes(exclude = ["object", "uint8", "bool"]).columns.tolist()

    # creating a copy of the original zillow/dataframe
    df_scaled = df.copy()

    # created the standard scaler
    scaler = StandardScaler()

    # fit/learn from the selected columns
    scaler.fit(df_scaled[scale_lst])

    # apply/transform the data
    df_scaled[scale_lst] = scaler.transform(df_scaled[scale_lst])
    
    print(f'scaled df shape: {df_scaled.shape}')

    # returning newly created dataframe with scaled data
    return df_scaled

'''function to create dummy variables for discrete variables/feature'''
def get_dummy_dataframes(train_df, val_df, test_df):

    # train dataset
    train_dummy = pd.get_dummies(
        data = train_df, 
        columns = [
                'job_level', 
                'job_role', 
                'marital_status', 
                'stock_option_level'],
        drop_first = False, 
        dtype = bool)

    # validate dataset
    validate_dummy = pd.get_dummies(
        data = val_df, 
        columns = [
                'job_level', 
                'job_role', 
                'marital_status', 
                'stock_option_level'],
        drop_first = False, 
        dtype = bool)

    # test dataset
    test_dummy = pd.get_dummies(
        data = test_df, 
        columns = [
                'job_level', 
                'job_role', 
                'marital_status', 
                'stock_option_level'],
        drop_first = False, 
        dtype = bool)

    # cleaning column names after dummy transformation
    train_dummy = clean_columns(train_dummy)
    validate_dummy = clean_columns(validate_dummy)
    test_dummy = clean_columns(test_dummy)

    # returning dummy datasets
    return train_dummy, validate_dummy, test_dummy


'''Function to create a dummy variable dataframe'''
def get_dummy_df(df):
    dummy_df = pd.get_dummies(
                    data = df, 
                    columns = [
                            'job_level', 
                            'job_role', 
                            'marital_status', 
                            'stock_option_level'],
                            drop_first = False, 
                            dtype = bool)

    print(f'dummy df shape: {dummy_df.shape}')

    return dummy_df


'''Function to return originally selected RFECV features w/random forest classifier: needed for reproduceability'''
def retrieve_rfecv_feature_lst():

    feature_lst = [
                'employee_age',
                'employment_rates_at_35',
                'high_school_graduation_rate',
                'household_income_at_35',
                'job_level_1',
                'job_level_2',
                'job_level_3',
                'job_role_healthcare_representative',
                'job_role_human_resources',
                'job_role_laboratory_technician',
                'job_role_manufacturing_director',
                'job_role_research_scientist',
                'job_role_sales_executive',
                'job_role_sales_representative',
                'marital_status_divorced',
                'marital_status_married',
                'marital_status_single',
                'monthly_income',
                'percentage_married_by_35',
                'poverty_rate',
                'stock_option_level_0',
                'stock_option_level_1',
                'stock_option_level_2',
                'stock_option_level_3',
                'total_working_years',
                'women_teenage_birthrate',
                'years_at_company',
                'years_in_current_role',
                'years_with_curr_manager']


    return feature_lst