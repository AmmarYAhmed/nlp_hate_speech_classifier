import bz2
import json
import csv

with open('post-elon-tweets.csv', 'w', newline='') as f1:
    csv_writer = csv.writer(f1)
    csv_writer.writerow(['text', 'created_at'])

    with open('31.json', 'r') as f:
        for line in f:
            try:
                data_line = json.loads(line)  
                if "data" in data_line and "text" in data_line["data"] and "created_at" in data_line["data"]:
                    tweet = data_line["data"]["text"]
                    time_stamp = data_line["data"]["created_at"]
                    if "2023" not in time_stamp:  
                        continue
                    if "lang" in data_line["data"] and data_line["data"]["lang"] != "en":
                        continue
                    csv_writer.writerow([tweet, time_stamp]) 
            except json.JSONDecodeError:
                continue 
            
# 20210930113400.json has some tweets from 2021
with open('pre-elon-tweets.csv', 'w', newline='') as f2:
    csv_writer = csv.writer(f2)
    csv_writer.writerow(['text', 'created_at'])

    with open('20210930113400.json', 'r') as f:
        for line in f:
            try:
                data_line = json.loads(line)  
                if "text" in data_line and "created_at" in data_line:
                    tweet = data_line["text"]
                    time_stamp = data_line["created_at"]
                    if "lang" in data_line and data_line["lang"] != "en":
                        continue 
                    csv_writer.writerow([tweet, time_stamp]) 
            except json.JSONDecodeError:
                continue
