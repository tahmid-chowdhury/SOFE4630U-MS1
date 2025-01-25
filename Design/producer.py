from google.cloud import pubsub_v1      # pip install google-cloud-pubsub  ##to install
import glob                             # for searching for json file 
import json
import os 
import csv

# Search the current directory for the JSON file (including the service account key) 
# to set the GOOGLE_APPLICATION_CREDENTIALS environment variable.
# files=glob.glob("*.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\tahmi\Documents\Cloud Computing\Project Milestone 1\SOFE4630U-MS1\Design\tahmids-project-95921-63961e4b0206.json";

# Set the project_id with your project ID
project_id="tahmids-project-95921";
topic_name = "design";   # change it for your topic name if needed

# create a publisher and get the topic path for the publisher
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)
print(f"Publishing messages to {topic_name} topic.")

csv_path = r"C:\Users\tahmi\Documents\Cloud Computing\Project Milestone 1\SOFE4630U-MS1\Design\Labels.csv"
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        message = json.dumps(row).encode('utf-8')
        future = publisher.publish(topic_path, message)
        future.result()
print("All records published.")
