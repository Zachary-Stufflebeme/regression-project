 #                                             Zillow PROJECT:
                                           
  In this project I will be looking at the Zillow data in order to learn more about what drives home prices. It will be useful to  first identify the most relevant features in my data by exploring the data and running statistical tests on different attributes of my dataset. I will than use the most relevant features in order to create several models that I can tweak around until I find the parameters that most closely predict house prices.
                                           
#                                                     Pipeline:
Plan:
                                            
Aquire: acquire data through functions saved in my acquire.py along with my encrypted credentials.

Prepare: Prepare and clean my data in such a way that I can plug it in to my classification models without causing error and with the prepared data still holding true to its original meaning.

Explore: Ask statistical questions of my data and create visualizations of the results in order to improve comprehension by people reading the report without clarifications from my presentation.

Model:Create models that try to closely predict house price,  along with visuals that highlight important findings and help the audiance understand their significance. Validate that all of your models are accurate not just on your train data but on outside data as well.

Deliver: Put all of my findings together in a final report where I make things as easy to understand as possible.

#                                         QUESTIONS TO ANSWER:

1.  QUESTION 1: Is bedroom count correlated to house price?
    Hnull - bedroom count and house price are not correlated.
    Halt - bedroom count and house price are correlated

2. Are bathroom count and house price correlated?
   Hnull - bathroom count and house price are not correlated.
   Halt - bathroom count and house price are correlated

3. are square feet and house price correlated?
   Hnull - square feet and house price are not correlated
   Halt - square feet and house price are correlated
   
4. are house age and house price correlated?
   Hnull - house age and house price are not correlated
   Halt - house age and house price are correlated
#                                                     Data Library

 #   Column                        Non-Null Count  Dtype  
---  ------                        --------------  -----  
 0   taxvaluedollarcnt             51037 non-null  float64
 1   fips                          51037 non-null  float64
 2   yearbuilt                     50949 non-null  float64
 3   bedroomcnt                    51037 non-null  float64
 4   bathroomcnt                   51037 non-null  float64
 5   calculatedfinishedsquarefeet  50982 non-null  float64
 6   garagecarcnt                  17605 non-null  float64
 7   lotsizesquarefeet             50697 non-null  float64
 8   poolcnt                       10308 non-null  float64
 9   regionidzip                   51013 non-null  float64
 10  roomcnt                       51037 non-null  float64
 11  numberofstories               14327 non-null  float64

   
#                                                    Key Findings:
 
I found 4 important features to focus on in the name of predicting house price, and created a few good models that beat the baseline . In the future I would like a little more time to tamper with the features I include in my models as I believe doing do could garner further gains in accuracy.
 
#                                                  How To Reproduce:
In order to reproduce my report you will need:
- a personal env with your credentials to access the SQL database.
- you will need to download and move my aquire.py prepare.py into the same directory
-Than you will need to run my report from the same directory.

