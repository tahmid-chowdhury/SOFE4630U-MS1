from google.cloud import pubsub_v1      # pip install google-cloud-pubsub  ##to install
import glob                             # for searching for json file 
import json
import random 

# Search the current directory for the JSON file (including the service account key) 
# to set the GOOGLE_APPLICATION_CREDENTIALS environment variable.
files=glob.glob("*.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=files[0];

# Set the project_id with your project ID
project_id="";
topic_name = " testTopic";   # change it for your topic name if needed

# create a publisher and get the topic path for the publisher
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

print(f"Published messages with ordering keys to {topic_path}.")

for n in range(100):
    print('Enter a key (String):',end='')
    record_key = input()
    print('Enter a value (String):',end='')
    record_value = input()
    if(record_key<=-1):
        break;
    
    print("Producing record: {}\t{}".format(record_key, record_value))    
    future = publisher.publish(topic_path, data=record_value,ordering_key=record_key);
    
    print(future.result())
 