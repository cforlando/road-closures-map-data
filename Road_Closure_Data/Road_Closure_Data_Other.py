import bs4
import requests
import csv
import json

Closure_Other = []
When_Other = []
Event_Other = []

Event_I4U = []
Closure_I4U = []
I4 = False

count = 0

url = "http://www.cityoforlando.net/roadclosure/other-road-closures/"
hdr = {"user-agent" : "Mozilla/5.0"}
req = requests.get(url, hdr)
if (req.status_code == 200):
    print("Everything is ok!")
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    results = soup.find_all("strong")
    for item in results:
        if item.get_text() == "Closure" and I4 == False:
            Closure_Other.append(results[count+1].get_text())
        elif item.get_text() == "Closure" and I4 == True:
            Closure_I4U.append(results[count+1].get_text())
        elif item.get_text() == "When" and I4 == False:
            When_Other.append(results[count+1].get_text())
        elif item.get_text() == "Event" and I4 == False:
            Event_Other.append(results[count+1].get_text())
        elif item.get_text() == "Event" and I4 == True:
            Event_I4U.append(results[count+1].get_text())
        elif item.get_text() == "I-4 Ultimate Improvements Project":
            I4 = True
        count += 1

#Storing Data "Others" Releated

    with open("Road_Closure_Data_Other.csv",'w') as csv_file:
        csv_file.write('Closure,When,Event\n')

        for r,h,l in zip(Closure_Other,When_Other,Event_Other):
            line = '"'+r+'"' + ',' + '"'+h +'"' + ',' + '"'+ l+'"'
            csv_file.write(line)
            csv_file.write('\n')

    csvfile = open('Road_Closure_Data_Other.csv', 'r')
    jsonfile = open('Road_Closure_Data_Other.json', 'w')

    fieldnames = ("Closure", "When", "Event")
    reader = csv.DictReader(csvfile, fieldnames)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')

#Storing data I-4 Ultimate Releated

    with open("Road_Closure_Data_I4_Ultimate.csv", 'w') as csv_file:
        csv_file.write('Closure,Event\n')
        for r, l in zip(Closure_I4U, Event_I4U):
            line = '"' + r + '"' + ',' + '"' + l + '"'
            csv_file.write(line)
            csv_file.write('\n')
    csvfile = open('Road_Closure_Data_I4_Ultimate.csv', 'r')
    jsonfile = open('Road_Closure_Data_I4_Ultimate.json', 'w')
    fieldnames = ("Closure", "Event")
    reader = csv.DictReader(csvfile, fieldnames)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')


    print(Closure_Other,"\n")
    print(When_Other,"\n")
    print(Event_Other,"\n")
    print(Closure_I4U, "\n")
    print(Event_I4U, "\n")