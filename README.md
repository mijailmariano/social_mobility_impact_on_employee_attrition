## **``Machine Learning Classification: Predicting Employee Attrition Through Socioeconomic Equity``**

### **<u>``Data Sources``</u>**
    
    Harvard University's Opportunity Atlas: Socioeconomic Data & IBM's Watson AI Human Resources Dataset

----

##### Created by: Mijail Q. Mariano
##### github.com/mijailmariano

<br>

### **<u>Project Description & Goals:</u>**



add text...



----

#### **<u>``In Brief:``</u>**


add text...


----

### **<u>Exploration Questions & Hypotheses:</u>**

add text...


----

### **<u>Key Findings:</u>**

add text...



----

### **<u>Statistical Analysis:</u>**

<br>

#### **<u>``Summary: 1-sample | 2 Tail T-test Results``</u>**

</br>

$H_0$ (Null Hypothesis): The variable mean of turn over employees is not statistically different than the population mean.

$H_a$ (Alternate Hypothesis): The variable mean for turn over employees is statistically different than the population variable mean.

* $alpha$: 1.0 - Confidence Interval (95% confidence level)
* $\alpha$ = 0.05

<br>

**``Statistically Signifcant Variables``**

1. Employee Age
2. Employment Rates At 35Yrs
3. High School Graduation Rate
4. Household Income At 35Yrs
5. Monthly Income
6. Percentage Married By 35Yrs
7. Poverty Rate
8. Total Years At Company (tenure)
9. Total Years In Current Role
10. Total Years With Current Manager
11. Total Working Years
12. Women Teenage Birthrate

-----
<br>

 #### **<u>``Summary: Chi_Squared Results``</u>**

</br>

$H_0$: "There is not a relationship between observed variable outcomes and expected employee turn over."

$H_a$: "There is a relationship between observed variable outcomes and expected employee turn over."

* $alpha$: 1 - Confidence Interval (95% confidence level)
* $\alpha$ = 0.05

<br>

**``Statistically Signifcant Variables``**


1. Job Level
2. Job Role
3. Marital Status
4. Stock Option Levels


<br>

### **<u>Model Selected Features: SKLearn Recursive Feature Elimination - using Cross Validation</u>**

|       | RFECV_features    | 
| ----  | ----              |
| 1     | employee age
| 2     | employment rates at 35yrs         |   
| 3	    | high school graduation rate       |
| 4	    | household income at 35Yrs         |
| 5	    | job level 1                       |
| 6	    | job level 2                       |
| 7	    | job level 3                       |
| 8	    | job role healthcare representative|
| 9	    | job role human resources          |
| 10	| job role laboratory technician    |
| 11	| job role manufacturing director   |
| 12	| job role research scientist       |
| 13	| job role sales executive          |
| 14	| job role sales representative     |
| 15	| marital status divorced           |
| 16	| marital status married            |
| 17	| marital status single             |
| 18	| monthly income                    |
| 19	| percentage married by 35Yrs       |
| 20	| poverty rate                      |
| 21	| stock option level 0              |
| 22	| stock option level 1              |
| 23	| stock option level 2              |
| 24	| stock option level 3              |
| 25	| total working years               |
| 26	| women teenage birthrate           |
| 27	| years at company                  |
| 28	| years in current role             |
| 29	| years with current manager        |


|       | Non-selected Features             |
| ----  | ----                              |
| 1     | job role manager                  |
| 2     | job role research_director        |
| 3     | job level 4                       |

----

### **<u>Selected Model Performances</u>**

| Model                        | Hyperparemeter(s)                 | Cross_Validation Accuracy          |
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
| baseline (mode_outcome)	    | 0.82	        | 0.00                      |
| train                         | 0.84	        | + 0.02                    |
| validate                      | 0.84          | 0.00                      |
| test (final)                  | 0.83          | - 0.01                    |


----

### **``Recommendations:``**


add text...



### **Looking Ahead (next steps):**

add text...


----

### **<u>Repository Roadmap:</u>**

Below is a GitHub repository roadmap and breakdown of the key files needed to navigate this anlysis. All code, data synthesis, and models can be found here for future reproduction or improvement recommendations:

1. **final_report.ipynb**

   Data Science pipeline overview document. Project artifact of the hypothesis tests conducted, regression techniques used for machine learning models, key analysis takeaways, and recommendations.

2. **exploration_and_modeling.ipynb**

   Jupyter Notebook used as the data science pipeline file which walks-through the process for creating the necessary data acquisition and cleaning functions.

3. **acquire.py** 
  
   Python module file that imports the neccessary Zillow real-estate dataset and subsequent feature for modeling phase in the analysis. If just using or running the final_report.ipynb file, then this corresponding acquire.py file should suffice and the prepare.py file will not be needed.
   
   **Note:** you must first import the initial Zillow dataset from MySQL. When passed in the "acquire.get_zillow_dataset()" function, the data is then stored locally as a .csv file - then referenced as a pd.Dataframe thereafter. 

4. **prepare.py**

     Python module file with created functions needed to clean, and manipulate the Zillow dataset used in this analysis.

5. **requirements.txt**

    add text...

----

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

    Fraction of households with children in this area whose head of household was single in 2012-16  (Source: American Community Survey.)
    
    Population Density in 2010	Number of residents per square mile in this area in 2010. (Source: 2010 Census Gazetteer and 2010 Decennial Census.)


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

    Freqeuncy of employees' travel for work related purposes


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
