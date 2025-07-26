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

Below are few observations made based on the the detailed analysis:-

1. Medical bills  of children are higher for most diseases compared to the other age groups for same medical condition. This phenomenon can be attributed to specialized treatment and care needed for children as these are generally life style diseases commonly occuring in senior and elderly age group.

2. The Average Billing Amount reduces with increase in Length of Stay in hospital.

3. The highest average bills claimed were from Medicare ($ 25,615) while the lowest average bills were claimed from UnitedHealthcare ($ 25,389). There's not much difference in the amount.

4. By Medication, highest average billed amount is for Ibuprofen ($ 25,735) and least in the case of Lipitor ($ 25,342).

5. The average billed amount of all chronic conditions are almost same with almost uniform age wise distribution.

6. There is no impact of admission type (Urgent/Emergency/Elective) on the average billed amount for similar medical conditions.

7. The Elderly population contributes maximum to the claimed insurance amount ($ 0.4 bn) as well as they comprise the highest chunk of total patient count (29%).

8. For male patients, the highest average claims were made from Blue Cross and Aetna and the least from Cigna.

9. The highest average billing amount by medication in females is for Aspirin and the lowest for Lipitor. In case of males, the highest is for Ibuprofen and the lowest for Aspirin.

10. Maximum Female patients are insuranced from Cigna and least from Aetna. In case of male patients, most have bought insurance from Cigna and the least from Blue Cross.

11. The month of February sees a dip in patient count every year while August sees a spike in patient count almost every year. Further investigation needs to be made to find any reason behind such trend.

12.  
