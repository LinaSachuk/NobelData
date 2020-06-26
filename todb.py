import os
from pymongo import MongoClient
import urllib.parse
import json
import csv
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import re

# ===========================================
# Connect to MongoDB Atlas
username = urllib.parse.quote_plus('mongo')
password = urllib.parse.quote_plus('mongo')
client = MongoClient(
    'mongodb+srv://%s:%s@cluster0-8yire.mongodb.net/test?retryWrites=true&w=majority' % (username, password))


# Create local "nobel" database on the fly from API call
db = client["nobel"]

# nobel_data = {}


# def init_browser():
#     # @NOTE: Replace the path with your actual path to the chromedriver
#     executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
#     return Browser("chrome", **executable_path, headless=False)


# def scrape_info():
#     # =================================================================================
#     # getting Nobel facts
#     # =================================================================================

#     browser = init_browser()

#     url = 'https://www.nobelprize.org/prizes/facts/nobel-prize-facts/'
#     browser.visit(url)

#     # Scrape page into Soup
#     html = browser.html
#     soup = bs(html, "html.parser")
#     # print(soup)

#     title = soup.find('h1', class_='title').text
#     print(title)
#     p = soup.find('p', class_='ingress').text
#     print(p)

#     tables = pd.read_html(url)
#     print(tables[0])

#     table_df = tables[0]
#     nobel_facts_html = table_df.to_html(index=False, header=False)

#     nobel_data['facts'] = nobel_facts_html

#     nobel_data['title'] = title
#     nobel_data['p'] = p

#     print(nobel_data)
#     # Return results
#     return nobel_data


# nobel_data = scrape_info()
# # Create collections on the fly
# db["facts"].insert_one(nobel_data)

# for collection_name in ["prizes", "laureates"]:
#     # collect the data from the API
#     response = requests.get(
#         "http://api.nobelprize.org/v1/{}.json".
#         format(collection_name[:-1]))
#     # convert the data to json
#     documents = response.json()[collection_name]
#     # Create collections on the fly
#     db[collection_name].insert_many(documents)

# # ==========================================
# #  # Delete  many documents
# db.prizes.delete_many({})
# db.laureates.delete_many({})


# Connect to the "nobel" database
db = client.nobel

# Use empty document {} as a filter
filter = {}

# Count documents in a collection
n_prizes = db.prizes.count_documents(filter)
# print(n_prizes)  # 646
n_laureates = db.laureates.count_documents(filter)
# print(n_laureates)  # 943

# Save a list of names of the collections managed by the "nobel" database
nobel_coll_names = client.nobel.list_collection_names()
# print(nobel_coll_names) #['prizes', 'laureates']

# Retrieve sample prize and laureate documents
prize = db.prizes.find_one()
laureate = db.laureates.find_one()

# Get the fields present in each type of document
prize_fields = list(prize.keys())
# print(prize_fields) #['_id', 'year', 'category', 'laureates']

laureate_fields = list(laureate.keys())
# print(laureate_fields) #['_id', 'id', 'firstname', 'surname', 'born', 'died', 'bornCountry', 'bornCountryCode', 'bornCity', 'diedCountry', 'diedCountryCode', 'diedCity', 'gender', 'prizes']


# The number of distinct countries of laureate affiliation for prizes
count = len(db.laureates.distinct('prizes.affiliations.country'))
print(count)
