from google.cloud import pubsub_v1      # pip install google-cloud-pubsub  ##to install
import glob                             # for searching for json file 
import json
import os 

# Search the current directory for the JSON file (including the service account key) 
# to set the GOOGLE_APPLICATION_CREDENTIALS environment variable.
files=glob.glob("*.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=files[0];

# Set the project_id with your project ID
project_id="";
topic_name = "testTopic";   # change it for your topic name if needed

# create a publisher and get the topic path for the publisher
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)
print(f"Published messages with ordering keys to {topic_path}.")

#iterate for 100 times 
for n in range(100):
    # get the value from the user
    print('Enter a value (String):',end='')
    record_value = input()
    # stop if empty value is entered
    if record_value=='':
        break;
    # convert the string to bytes (serialization)
    record_value=str(record_value).encode('utf-8')
    
    # send the value
    print("Producing a record: {}".format(record_value))    
    future = publisher.publish(topic_path, record_value);
    
    #ensure that the publishing has been completed successfully
    future.result()
 