# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 17:35:48 2018

@author: usert
"""

import pandas as pd

os.chdir('C:/Users/usert/Documents/GitHub/GitHub')

Raw_Data = pd.read_csv("listings.csv", error_bad_lines=False, warn_bad_lines=False)


# Remove the dollar sign from price variable and turn the characters as float
price_r = Raw_Data['price']

p = [0]*len(price_r)
price = [0]*len(price_r)
       
for i in range(0,len(price_r)):
    p[i] = price_r[i].replace(",","").replace("$","")
    price[i] = float(p[i])
    
price = pd.DataFrame(data = {'price': price})


# Define the minimum_nights variable
minimum_nights = pd.DataFrame(data = Raw_Data['minimum_nights'])


# Get the categories of the bed types
bed_type = Raw_Data['bed_type']
bed_type_u = []
for i in bed_type:
    if i not in bed_type_u:
        bed_type_u.append(i)
print (bed_type_u)

# Create 4 more variables to capture the categories of bed types
# Create a variable called "bed_type_Real_Bed" and set its value equals to 1 when the bed_type is "Real Bed", others follow this logic
bed_type_Real_Bed = [0]*len(price_r)
Raw_Data['bed_type_Real_Bed']= bed_type_Real_Bed
Raw_Data.loc[Raw_Data['bed_type'] == 'Real Bed', 'bed_type_Real_Bed'] = 1

# Need to modify the name "bed_type_Pull_out_Sofa" as Python does not read "-"
bed_type_Pull_out_Sofa = [0]*len(price_r)
Raw_Data['bed_type_Pull_out_Sofa']= bed_type_Pull_out_Sofa
Raw_Data.loc[Raw_Data['bed_type'] == 'Pull-out Sofa', 'bed_type_Pull_out_Sofa'] = 1

# Similar with 'Futon','Airbed' and 'Couch'
bed_type_Futon = [0]*len(price_r)
Raw_Data['bed_type_Futon']= bed_type_Futon
Raw_Data.loc[Raw_Data['bed_type'] == 'Futon', 'bed_type_Futon'] = 1

bed_type_Airbed = [0]*len(price_r)
Raw_Data['bed_type_Airbed']= bed_type_Airbed
Raw_Data.loc[Raw_Data['bed_type'] == 'Airbed', 'bed_type_Airbed'] = 1

bed_type_Couch = [0]*len(price_r)
Raw_Data['bed_type_Couch']= bed_type_Couch
Raw_Data.loc[Raw_Data['bed_type'] == 'Couch', 'bed_type_Couch'] = 1

Processed_Data = pd.concat([Processed_Data, price, minimum_nights, Raw_Data['bed_type_Real_Bed'], Raw_Data['bed_type_Pull_out_Sofa'], Raw_Data['bed_type_Futon'], Raw_Data['bed_type_Airbed'], Raw_Data['bed_type_Couch']], axis = 1)










