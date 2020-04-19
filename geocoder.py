# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:21:52 2020

@author: curiacosi1
"""

import pycountry_convert as pc

def country_to_continent(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name

# Example
country_name = 'Germany'

print(country_to_continent(country_name))