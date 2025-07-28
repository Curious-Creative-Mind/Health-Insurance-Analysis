# Health-Insurance-Analysis

## Project Overview:

### Business Problem Statement:

Rising healthcare costs and inefficient claims processing are placing significant financial strain on both patients and insurance providers. To ensure sustainable healthcare delivery, it is critical to identify the key drivers of billing amounts, analyze the impact of insurance coverage, and optimize claims management practices. 

The objective is to uncover actionable insights that help reduce unnecessary medical expenses, streamline insurance workflows, and improve transparency between hospitals, patients, and insurance providers.

### Data Structure and Initial Checks:

The Healthcare_db database consists of a table healthcare_data with a total row count of 55,500 records.

Prior to beginning the analysis, a variety of checks were conducted for quality control and familiarization with the datasets using Python and SQL.

### Data Quality Check:

-	Check Null values
-	Check Duplicates
-	Deleting irrelevant columns
-	Creating custom columns
-	Formatting and changing data type

## Executive Summary:

### Overview of Findings:

The healthcare data covers details of medical expenses and related insurance claims of patients between the time period of May 2019 - May 2024. The total billed amount is $ 1.42 Billion across the span of 5 years with the average billing amount being $ 25.54 K. The total medical claims made were 55.5 K in count. The average hospital stay was 15 days and the average patient age was 51.5 years. There were no factors found that were significantly impacting Insurance bills.

![Dashboard Pg1](https://github.com/Curious-Creative-Mind/Health-Insurance-Analysis/blob/main/Dashboard%20Pg-1.PNG?raw=true)

![Dashboard Pg2](https://github.com/Curious-Creative-Mind/Health-Insurance-Analysis/blob/main/Dashboard%20Pg-2.PNG?raw=true)

Below are few observations made based on the detailed analysis:-

1. Medical bills  of children are higher for most diseases compared to the other age groups for same medical condition. This phenomenon can be attributed to specialized treatment and care needed for children as these are generally life style diseases commonly occuring in senior and elderly age group.

![Bill_agewise](https://github.com/Curious-Creative-Mind/Health-Insurance-Analysis/blob/main/bill_medicalcon_agewise.png?raw=true)

2. The Average Billing Amount reduces with increase in Length of Stay in hospital.

3. The highest average bills claimed were from Medicare ($ 25,615) while the lowest average bills were claimed from UnitedHealthcare ($ 25,389). There's not much difference in the amount.

4. By Medication, highest average billed amount is for Ibuprofen ($ 25,735) and least in the case of Lipitor ($ 25,342).

5. The average billed amount of all chronic conditions are almost same with almost uniform age wise distribution.

6. There is no impact of admission type (Urgent/Emergency/Elective) on the average billed amount for similar medical conditions.

![Bill_admissiontype](https://github.com/Curious-Creative-Mind/Health-Insurance-Analysis/blob/main/bill_admissiontype_medconwise.png?raw=true)

7. The Elderly population contributes maximum to the claimed insurance amount ($ 0.4 bn) as well as they comprise the highest chunk of total patient count (29%).

8. For male patients, the highest average claims were made from Blue Cross and Aetna and the least from Cigna.

9. The highest average billing amount by medication in females is for Aspirin and the lowest for Lipitor. In case of males, the highest is for Ibuprofen and the lowest for Aspirin. 

10. Maximum Female patients are insuranced from Cigna and least from Aetna. In case of male patients, most have bought insurance from Cigna and the least from Blue Cross.

11. The month of February sees a dip in patient count every year while August sees a spike in patient count almost every year. Further investigation needs to be made to find any reason behind such trend.

12. The total distinct patient count was 40.24 K with an average age of 51.5 years.

13. The insurance company has no impact on the average hospital stay.

14. There seems to be no significant relationship between particular blood group and any chronic disease.

15. Elderly population make up the highest patient count (15 K) while children make up the least count (888).

16. In case of children, there is high risk of cancer in O(-ve) blood group, obesity in A(+ve) blood group and hypertension in B(-ve) blood group.

## Recommendations:

Based on the uncovered insights, the following recommendations have been provided :

- For Insurance Buyers :

1. Buying insurance for children having chronic diseases can be beneficial in long term and help in managing medical expenses.
2. Most of the patients belong to the Elderly Age Group as these chronic diseases are common in old age so having medical insurance would be helpful to reduce the burden of medical expenses for senior and elderly population.

- For Insurance Companies :

1. Can design custom Insurance plans specially for children covering long hospital stays, diagnostics and medical checkups.
2. Adjust age stratified premium pricing models to increase coverage proportion for children.
3. Provide preventive health programs and offer discounts and rewards for wellness program participation and regular health checkups.
4. Partner with pedriatric hospitals and clinics and negotiate pre-packaged pricing for frequent treatments.
5. Having the Insurance buyer go through a basic medical checkup/diagnosis for common chronic diseases to screen out and propose premium plans accordingly. This would create transparency and build trust.

### Data Source:

- Kaggle 

### Tools used:

- **Python** - scripting for data ingestion in database
- **SQL** - extracting relevant table from database
- **Python-(NumPy, Pandas)** – for Data Cleaning, Data Transformation and EDA
- **Python-(Matplotlib, Seaborn)** – for Data Visualization and Data Analysis
- **Power BI** - dashboard creation

### Skills applied and learned:

- SQL 
- Python (Scripting, Numpy, Pandas, Matplotlib, Seaborn)
- Data Analysis and insights generation
- Power BI - Dashboard creation
- Data Storytelling
- Project Documentation
- AI (Copilot and ChatGPT) 

