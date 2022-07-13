======
ETL - Extract, Transform, Load
======
**IBM Data Enginering Certification - Exercise.**

DISCLAIMER - This is still in progress.

**Scenario**

For this project, you will assume the role of data engineer working for an international financial analysis company. Your company tracks stock prices, commodities, forex rates, inflation rates.  Your job is to extract financial data from various sources like websites, APIs and files provided by various financial analysis firms. After you collect the data, you extract the data of interest to your company and transform it based on the requirements given to you. Once the transformation is complete you load that data into a database.

-----
Project Tasks
-----

In this project you will:

* Collect data using APIs

* Collect data using webscraping.

* Download files to process.

* Read csv, xml and json file types.

* Extract data from the above file types.

* Transform data.

* Use the built in logging module.

* Save the transformed data in a ready-to-load format which data engineers can use to load the data.

-----
Exercise 1 - Extract data from Webpage by webscraping
-----

Get the bank information using webscraping from this Wikipedia link https://en.wikipedia.org/wiki/List_of_largest_banks?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0221ENSkillsNetwork23455645-2022-01-01
Scrape the data from the table "By market capitalization" and store it in a JSON file.

etl_webscraping.py

-----
Exercise 2 - Extract data from API
-----
In this part we will:

* Collect exchange rate data using an API
* Store the data as a CSV

We will use https://apilayer.com/marketplace/exchangerates_data-api, just get the free subscription to get your api key