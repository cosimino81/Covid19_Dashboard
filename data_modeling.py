# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:31:51 2020

@author: curiacosi1
"""

import pandas as pd
import pycountry_convert as pc



# =============================================================================
# GEOCODER: Convert the country name to the belonging continent
# =============================================================================

# define function to convert country code to continent name
def country_to_continent(country_code):
    
    # japane
    if country_code == "JPG11668":
        country_code = "JP"
    # Greace   
    elif country_code == "EL":
        country_code = "GR"
    # Vatican city    
    elif country_code == "VA":
        country_code = "IT"
    # Island close to Haiti    
    elif country_code == "SX":
        country_code = "HT"
    # Timor East
    elif country_code == "TL":
        country_code = "JP"
    # Great Britan   
    elif country_code == "UK":
        country_code = "GB"
        
    country_continent_code = pc.country_alpha2_to_continent_code(country_code)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name


# Example
print(country_to_continent("IT"))


# =============================================================================
# Working on the dataset
# =============================================================================

# read the dataset
df_covid = pd.read_csv("https://opendata.ecdc.europa.eu/covid19/casedistribution/csv")

print(df_covid.shape)

# drop all nan values on the column "geoId"
df_covid.dropna(subset = ["geoId"], inplace=True)

print(df_covid.shape)

# create the column with continent names
df_covid["continent"] = df_covid["countryAndTerritories"].apply(country_to_continent(), axis=1,)






















