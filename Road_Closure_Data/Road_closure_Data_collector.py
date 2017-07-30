import bs4
import requests
import csv
import json

Closure = []
When = []
Event = []
Data = []
count = 0

url = "http://www.cityoforlando.net/roadclosure/"
hdr = {"user-agent" : "Mozilla/5.0"}
req = requests.get(url, hdr)
if (req.status_code == 200):
    print("Everything is ok!")
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    results = soup.find_all("strong")
    for item in results:
        if item.get_text() == "Closure":
            Closure.append(results[count+1].get_text())
        elif item.get_text() == "When":
            When.append(results[count+1].get_text())
        elif item.get_text() == "Event":
            Event.append(results[count+1].get_text())
        count += 1
    with open("Road_Closure_Data.csv",'w') as csv_file:
        csv_file.write('Closure,When,Event\n')

        for r,h,l in zip(Closure,When,Event):
            line = '"'+r+'"' + ',' + '"'+h +'"' + ',' + '"'+ l+'"'
            csv_file.write(line)
            csv_file.write('\n')

    csvfile = open('Road_Closure_Data.csv', 'r')
    jsonfile = open('Road_Closure_Data.json', 'w')

    fieldnames = ("Closure", "When", "Event")
    reader = csv.DictReader(csvfile, fieldnames)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')

    print(Closure,"\n")
    print(When,"\n")
    print(Event,"\n")