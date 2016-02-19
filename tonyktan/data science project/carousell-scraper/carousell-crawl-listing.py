from bs4 import BeautifulSoup
import requests

r = requests.get("https://carousell.com/p/35934353")

soup = BeautifulSoup(r.text, "lxml")
# print type(soup)
# print soup.prettify()

def find_title():
  return soup.find("h1", class_="pdt-buy-box-title").get_text()

def find_attributes():
  attr = soup.find_all("p", class_="pdt-buy-box-attributes")
  s = attr[0].a.get_text()
  p = attr[1].span.get_text()
  l = attr[2].span.get_text()
  return s, p, l

def find_availability():
  return soup.find("button", class_="pdt-buy-box-chat").span.get_text()

def find_likes():
  return soup.find("span", class_="pdt-buy-box-likes-count").span.get_text()

def find_desc():
  return soup.find("p", class_="pdt-description-content").get_text()

def find_date():
  return soup.find("small", class_="pdt-description-time").time.find_all("span")[1].get_text()

def find_numcomments():
  return soup.find("div", class_="pdt-tabs").find("ul").find_all("li")[1].get_text()

product_title = find_title()
seller, price, location = find_attributes()
availability = find_availability()
likes = find_likes()
description = find_desc()
list_date = find_date()
num_comments = find_numcomments()

'''
#write to csv
import os, csv
os.chdir("/Users/franceszlotnick/Dropbox/TextAsData/Sections/tutorials/")

with open("lobbying.csv", "w") as toWrite:
    writer = csv.writer(toWrite, delimiter=",")
    writer.writerow(["name", "link", "date"])
    for a in lobbying.keys():
        writer.writerow([a.encode("utf-8"), lobbying[a]["link"], lobbying[a]["date"]])

#write to json
import json

with open("lobbying.json", "w") as writeJSON:
    json.dump(lobbying, writeJSON)

'''