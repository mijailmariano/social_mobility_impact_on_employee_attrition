## **Machine Learning Classification: Predicting Employee Attrition Through Socioeconomic Equity**

### **Data Sources**
    
    Harvard University's Opportunity Atlas: Socioeconomic Data & IBM's Watson AI Human Resources Dataset

----

##### Created by: Mijail Q. Mariano
##### github.com/mijailmariano

<br>

### **<u>Project Description & Goals:</u>**

I use socioeconomic data at the state county level to understand social-mobility* measures and how these factors contribute to company-employee attrition.

The socioeconomic data for this analysis was acquired from Harvard University's "Opportunity Atlas" platform. In collaboration with the US Census Bureau and Internal Revenue Service (IRS) - the Opportunity Atlas tracks anonymized metrics of social-mobility at the local level for children born in the years from 1978 - 1983. 

The medium-sized business employee dataset used in the analysis was generated by IBM's AI "Watson" to help business practitioners investigate potential drivers of employee attrition.

*Though terms like 'social-mobility metric' and 'socioeconomic data' are traditionally distinct, for ease-of-readability I chose to use the two terms interchangeably throughout the analysis.* *

----

#### **<u>``In Brief:``</u>**

1. I first acquired the IBM Employee Dataset from Kaggle.com 
2. Since it was not provided in the data, I classify the geographical location for this mid-sized company to be New York, NY (midtown area) and inspected each employees' recorded commute "distance from work"
3. I filter and acquire socioeconomic data for counties within a 30-mile radius of the farthest employee commute in the IBM dataset

| ``County``                    | ``State ``    |
| ----                          | ----          |
| Fairfield County              | CT            |
| Bergen County                 | NJ            |
| Essex County                  | NJ            |
| Hudson County                 | NJ            |
| Middlesex County              | NJ            |
| Morris County                 | NJ            |
| Passaic County                | NJ            |
| Union County                  | NJ            |
| Bronx County                  | NY            |
| Kings County                  | NY            |
| Nassau County                 | NY            |
| New York County               | NY            |
| Queens County                 | NY            |
| Richmond County               | NY            |
| Rockland County               | NY            |
| Suffolk County                | NY            |
| Westchester County            | NY            |

4. I bin counties into five (5) distinct commute locations by range in miles from New York, NY (office location)
5. I then randomly assign each employee in the IBM dataset to a potential home-of-record county based on their commute distance
6. I then merge the two datasets (IBM & Opportunity Atlas) by county and assign each employee their respective county-level socioeconomic/social-mobility metric

| **``County-level Social-mobility Metrics:``** |
| ----                                          | 
| Household Income at Age 35                    |
| Highschool Graduation Rate                    |
| Percentage Married at Age 35                  |
| Incarceration Rate                            |
| Women Teenage Birth Rate                      |
| Poverty Rate                                  |
| Employment Rates at Age 35                    |
| Percentage of Single Parents                  |   

7. I use an “Inter-Quartile Range” (IQR) method to determine outliers in the dataset and filter out upper bound outliers found in employee records
8. I create and test statistical hypotheses to explore potential socioeconomic/mobility factors in company-employee attrition
9. I generate, deploy, and evaluate six (6) unique non-linear machine learning models to determine the predictability accuracy of employee attrition
10. I deploy the best performing model as measured by total accuracy and sensitivity on the test dataset
11. I conclude that commonly recorded employee data combined with county-level social-mobility metrics can contribute to predicting company-employee attrition better than a baseline mode prediction
11. Lastly, I summarize my findings and generate recommendations for follow-on analysis and implementation of these insights 

----

### **<u>Exploration Questions:</u>**

* How much does an employee's geographical background (where they live or grow-up) impact their decision to remain or leave their company?

* Are there socioeconomic/employee demographic differences between those employees who leave the company and those who remain?

* Can socioeconomic data help to model true employee turn-over (sensitivity) better than a baseline prediction model?

* How can organizations think about employee attrition in the context of local-counties social-mobility?

**<u>``Assumptions:``</u>**

I make several assumptions throughout the analysis that can potentially play a role in the interpretation of my findings. Here are some of the key underlying analysis assumptions:

**Employee Attrition**

    Employee attrition can typically be categorized into two (2) broad-ranging measures, which are "voluntary" and "involuntary" attrition. Though not recorded in the IBM dataset, I ultimately made the decision to classify "attrition" in the data as voluntary resignation. This means that any employee recorded as having left the company made this decision without any influence of the business.

**Geographical Assignment**

    I assume that the employee data is from a mid-sized business in the United States, specifically the New York City, NY area. I also assume that its employees live or are from counties within a 30-mile commute radius of this business. Due to random county assignment for all employees, the analysis does not determine the directionality of socioeconomic impact on attrition. This is due to the uncertainty around employees' exact home-of-record locations and how other variables such as an employee's age, company tenure, and ultimately their decision to remain or leave the company are directly impacted by their county's social-mobility metrics.

----

### **<u>``Key Findings:``</u>**

After deploying the final logistic regression model on the test dataset, we can conclude that the model is in fact better equipped to predict employee attrition than a baseline model prediction.

Model sensitivity or the *true-positive rate*, which represents all total instances when the model predicted an employee would turn-over or leave the company was ~14% greater than a baseline prediction.

Although model performance was a goal of this analysis, it's important to restate that any model created or used to predict employee turn-over should be handled and interpreted with a high-degree of responsibility and rigor. Since employee turn-over can represent an important decision to both employers and employees, it's also worth noting the many adverse effects that high degree of undue employee turn-over can have at the local and federal levels.

One of the primary objectives of this analysis was to explore a relatively different yet important approach to how organizations interpret, measure, and cultivate the employment life-cycle within their business. 

I believe that by researching and remaining attentive to local socioeconomic data from areas in which a business operates in, employers can help to understand important socioeconomic divides that can have a direct effect on their employees and whether they choose to remain at their company.

More importantly, by studying and leveraging social-mobility information - employers create opportunities to learn and measure how socially equitable and fair their businesses. By auditing current practices and potential cultural norms, employers can examine what, if any of these practices exacerbate unfair or misunderstood working environment, and thus - undue employee attrition.


----

### **<u>Statistical Analysis:</u>**

#### **<u>``Summary: 1-sample | 2 Tail T-test Results``</u>**

<br>

$H_0$ (Null Hypothesis): The variable mean of turn over employees is not statistically different than the population variable mean.

$H_a$ (Alternate Hypothesis): The variable mean for turn over employees is statistically different than the population variable mean.

* $alpha$: 1.0 - Confidence Interval (95% confidence level)
* $\alpha$ = 0.05

</br>

**``Statistically Significant Variables``**

1. Employee Age
2. Employment Rates At 35Yrs
3. High School Graduation Rate
4. Household Income At 35Yrs
5. Monthly Income
6. Percentage Married By 35Yrs
7. Poverty Rate
8. Total Years At Company (tenure)
9. Total Years in Current Role
10. Total Years with Current Manager
11. Total Working Years
12. Women Teenage Birthrate

-----

 #### **<u>``Summary: Chi_Squared Results``</u>**

<br>

$H_0$: "There is not a relationship between observed variable outcomes and expected employee turn over."

$H_a$: "There is a relationship between observed variable outcomes and expected employee turn over."

* $alpha$: 1 - Confidence Interval (95% confidence level)
* $\alpha$ = 0.05

</br>

**``Statistically Significant Variables``**

1. Job Level
2. Job Role
3. Marital Status
4. Stock Option Levels

<br>

### **<u>Model Selected Features: SKLearn Recursive Feature Elimination - using Cross Validation</u>**

|       | ``RFECV_features``                | 
| ----  | ----                              |
| 1     | employee age                      |
| 2     | employment rates at 35            |   
| 3     | high school graduation rate       |
| 4     | household income at 35            |
| 5     | job level 1                       |
| 6     | job level 2                       |
| 7     | job level 3                       |
| 8     | job role healthcare representative|
| 9     | job role human resources          |
| 10    | job role laboratory technician    |
| 11    | job role manufacturing director   |
| 12    | job role research scientist       |
| 13    | job role sales executive          |
| 14    | job role sales representative     |
| 15    | marital status divorced           |
| 16    | marital status married            |
| 17    | marital status single             |
| 18    | monthly income                    |
| 19    | percentage married at 35          |
| 20    | poverty rate                      |
| 21    | stock option level 0              |
| 22    | stock option level 1              |
| 23    | stock option level 2              |
| 24    | stock option level 3              |
| 25    | total working years               |
| 26    | women teenage birthrate           |
| 27    | years at company                  |
| 28    | years in current role             |
| 29    | years with current manager        |

|       | Non-selected Features             |
| ----  | ----                              |
| 1     | job role manager                  |
| 2     | job role research_director        |
| 3     | job level 4                       |

----

### **<u>Selected Model Performances</u>**

| Model                        | Hyperparameter(s)                 | Cross_Validation Accuracy    |
| ----                         | ----                              | ----              |
| Decision Tree                | depth: 7 / sample_leaf: 14        | 84%               |
| Decision Tree                | depth: 13 / sample_leaf: 13       | 84%               |
| K-nearest Neighbor (KNN)     | k: 4                              | 84%               |
| K-nearest Neighbor (KNN)     | k: 10                             | 84%               |
| Logistic Regression          | class_weight: 0.9                 | 84%               |
| Logistic Regression          | class_weight: 1.0                 | 84%               |
| Random Forest                | depth: 7 / sample_leaf: 14        | 84%               |

<br>

----

**<u>``Final Performance through Test Dataset: Logistic Regression w. class-weight: 1.0 ``</u>**

| Dataset                       | Accuracy      | Relative_Difference       |
| ----                          | ----          | ----                      |
| baseline (mode_outcome)       | 0.82          | 0.00                      |
| train                         | 0.84          | + 0.02                    |
| validate                      | 0.84          | 0.00                      |
| test (final)                  | 0.83          | - 0.01                    |

----

### **``Recommendations:``**

The following recommendations are based on the informed insights from this analysis and what I believe can help businesses better understand employee attrition and reduce continuity risks.

1. Leverage socioeconomic data/metrics at the local level to understand the communities in which the organization operates in. There are several free resources such as the Opportunity Atlas, America Inequality, and the US Federal Reserve System's Economic FRED platform that provide businesses with on-the-ground data on these metrics, to include social equity topics or ideas for employers to explore and potentially implement. 

2. Use this analysis to explore the casual relationship between employee attrition and the statistically identified county social-mobility metrics and employee recorded data. Employers can reproduce this analysis using their own organizational data. Consider also re-measuring statistical correlation or dependency to employee attrition when specific attrition data such as voluntary or involuntary attrition is included.

3. Leverage and iterate on the top performing machine learning models created through this analysis. Use models not to predict employee attrition, but rather as a measurement of employee sentiment and ways in which employers can help local communities and employees. 


### **Looking Ahead (next steps):**

- I want to test and measure the potential co-dependencies/collinearity of the social-mobility metrics and how this may impact my analysis.

- To better understand the independent-dependent relationship, I want to test the causal relationship of features to the target variable.

----

### **<u>Repository Roadmap:</u>**

Below is a GitHub repository roadmap and breakdown of the key files needed to navigate this analysis. All code, data synthesis, and models can be found here for future reproduction or improvement recommendations:

1. **final_report.ipynb**

   Data Science pipeline overview document. Project artifact of the hypothesis tests conducted, classification techniques used for machine learning models, key analysis takeaways, and recommendations.

2. **exploration_and_modeling.ipynb**

   Jupyter Notebook used as the data science pipeline which walks-through the process for acquiring, cleaning, and modeling with the IBM and Opportunity Atlas data.

3. **acquire.py** 
  
   Python module file that imports the necessary dataset. Once the dataset is pulled and loaded into a .ipynb file, it is then cached locally into a .csv file. All subsequent calling of this data will be referenced from the cached .csv.   
   
   **Note:** you must first import the initial Zillow dataset from MySQL. When passed in the "acquire.get_zillow_dataset()" function, the data is then stored locally as a .csv file - then referenced as a pd.Dataframe thereafter. 

4. **prepare.py**

     Python module file with created functions needed to clean, and manipulate the overall dataset used in this analysis.

5. **requirements.txt**

    This text file lays-out all the project dependencies that I have used throughout this project. Within the file you can find detailed information on the platforms, packages, version numbers, and libraries used to construct the working environment. 

***

### <center> **Data Dictionary** </center>

**``Opportunity Atlas Data:``**

**source:**  https://www.opportunityatlas.org/

**High School Graduation Rate**

    Fraction of children who grew up in this area with a high school degree or a GED. Estimates have a margin of error; for example, standard error at county level for children with parents at 25th percentile is 1% pooling race and gender groups and 3% for black men. This outcome is available only at the county (not tract) level due to small sample sizes. (Source: American Community Survey)

**Household Income at Age 35**

    Average annual household income in 2014-15 for children (now in their mid-30s) who grew up in this area. Estimates have a margin of error; for example, standard error at tract level for children with parents at 25th percentile is $1,917 pooling race and gender groups and $2,721 for black men. (Source: Federal income tax records)

**Incarceration Rate**

    Fraction of children who grew up in this area who were in prison or jail on April 1, 2010. Estimates have a margin of error; for example, standard error at tract level for children with parents at 25th percentile is 1% pooling race and gender groups and 4% for black men. (Source: 2010 Decennial Census)

**Poverty Rate in 2012-16**

    Fraction of all residents of this area with household incomes below the federal poverty line in 2012-16. (Source: American Community Survey.)

**Fraction Single Parents in 2012-16**

    Fraction of households with children in this area whose head of household was single in 2012-16 (Source: American Community Survey.)
    
    Population Density in 2010 Number of residents per square mile in this area in 2010. (Source: 2010 Census Gazetteer and 2010 Decennial Census.)

**Teenage Birth Rate (women only)**

    Fraction of women who grew up in this area who claimed ever a child who was born when the women were between the ages of 13 and 19 as a dependent when filing taxes. Estimates have a margin of error; for example, standard error at tract level for children with parents at 25th percentile is 4% pooling race groups and 6% for black women. (Source: Income Tax Records)

**Fraction Married at Age 35**

    Fraction of children who grew up in this area who are married in 2015 (in their mid-30s). Estimates have a margin of error; for example, standard error at tract level for children with parents at 25th percentile is 3% pooling race and gender groups and 4% for black men. (Source: Income Tax Records)

<br>

**``IBM Watson AI HR Dataset:``**

**source:**  https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

**Employee Age**

    Total years lived by the employee

**Total Working Years**

    Total number of years the employee has worked

**Attrition**

    Turn over of current employee or if employee is still employed with the company

**Average Tenure**

    Average length of time at the job

**Business Travel**

    Frequency of employees' travel for work related purposes

**Department**

    The department that the employee currently works in or has previously worked for

**Distance From Home**

    Distance between the employee’s home and the company, measured in miles

**Education**

    Highest level of education attainment

**Education Field**

    The employee’s main field of academic study

**Employee Count**

    Total number of employees in the company

**Employee Number**

    Unique employee identifier/credentials 

**Gender**

    Employees' recorded gender preference

**Job Role**

    Employee's role at the company

**Marital Status**

    Employees' recorded relationship status

**Total Number of Companies**

    Total number of companies the employee has worked for prior to their current job

**Total Working Years**

    Total years the employee has worked

**Training Times Last Year**

    Number of work-related trainings attended by the employee in the previous year

**Years at Company (tenure)**

    Total years the employee has worked for the company

**Years In Current Role**

    Total years the employee has stayed in their current role in the company

**Years Since Last Promotion**

    Total years since the employee was last promoted

**Years With Current Manager**

    Total years working under the same manager

**Daily Rate**

    Gross rate of pay per day

**Hourly Rate**

    Gross rate of pay per hour

**Monthly Income**

    Employees' monthly salary 

**Monthly Rate**

    Gross rate of pay per month

**Over Time**

    Indication of whether the employee has worked after their standard working hours

**Percent Salary Hike**

    Percentage increase in the employee’s salary compared to the prior year

**Standard Hours**

    Number of hours stipulated in the employee contract

**Stock Option Level**

    add text...

**Environment Satisfaction**

    Degree to which the employee is satisfied with their work area/space

**Job Involvement**

    Degree to which the employee identifies with their current role

**Job Satisfaction**

    Degree to which the employee is satisfied with their job

**Relationship Satisfaction**

    Degree to which the employee is satisfied with their relationships at work

**Work Life Balance**

    Degree to which the employee agrees that there is work-life balance


