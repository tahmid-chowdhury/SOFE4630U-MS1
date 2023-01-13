# Lab 1: Data Ingestion System (Apache Kafka)

## What’s Kafka?
1.	Watch the following video about [Event Driven Architecture (EDA)](https://www.youtube.com/watch?v=o2HJCGcYwoU)
2.	The core component of an EDA is the Data Ingestion System also known as Publisher/subscriber (pub/sup). 
Kafka is one of the most frequent used pub/sub. Watch the following video to get a good understanding of [Kafka and its terminologies](https://www.youtube.com/watch?v=Ch5VhJzaoaI).
3.	You can set up Kafka cluster on a set of locally connected computers, 
deploy it as a set of docker images over Kubernetes cluster, or use already exists cloud-native service. 
In this section, we will use Kafka confluent Cloud as a cloud-native service. It’s a tool that can integrate with any cloud platform 
like Google Cloud Platform (GCP) to create a Kafka cluster. Thus, we will start by creating a GCP account.  

## Creating GCP account
1.	It’s recommended to create a new Gmail account, but you can use an already existing account.
2.	Go to [GCP official site](https://cloud.google.com/gcp). Be sure that you are using the correct account. Then, click on **Get Started for free** button  
![a1](images/a1.jpg)  
3.	Fill the account information and accept the terms of services  
![a2](images/a2.jpg)  
4.	In the next step, you will fill in your personal information and a credit card information. That information is to ensure that you are a real person. This will create a free account for 90 days and give you 300+ $ free credits. **No charges are made unless you upgrade to a paid Cloud Billing account**. Please read [the GCP billing verification](https://cloud.google.com/free/docs/free-cloud-features#billing_verification) for more information.  
![a3](images/a3.jpg)  
5.	Fill in the final survey. Then, click **Done**. You can safely skip any given offers.  
![a4](images/a4.jpg)  
6.	Get yourself familiar with
* Dashboard: allows you to search and select available cloud services
* project(s): a project usually named **My First Project** will be created but we can create, edit, and delete projects.
* The console: By clicking the console icon, the console will be opened to you. The console is a Linux terminal that can be used to configure the cloud. Any commands that affect the console local OS will be temporary and lost whenever the session is closed while any change made to any cloud services will be permanent.  
![a5](images/a5.jpg)  
The console will be opened at the bottom of the page as shown in the following figure and from it we can exchange files and folders with your local computer by downloading or uploading them. You can also click **Open Editor** button to open the editor.  
 ![a6](images/a6.jpg)  
* Editor: It’s a text editor that allows you to edit plain text file as shown in the following figure. You can switch back to the console by clicking **Open Terminal** button  
 ![a7](images/a7.jpg)  
# Create a Confluent Kafka Cluster
1.	Open [the Confluent Cloud-native Service for Apache Kafka](https://www.confluent.io/confluent-cloud/). Then click **TRY FREE**.  
![b1](images/b1.jpg)  
2.	Sign in with the same Google account  
![b2](images/b2.jpg)  
3.	Enter your personal Information. Then, click **Submit**  
![b3](images/b3.jpg)  
4.	Finish the final survey and click **Continue**.  
5.	The first step in creating the Kafka cluster is to choose the free Basic configuration. Then, Choose Google Cloud as the service provider, Toronto as a **Region**, and the A single zone as the **Availability**. Then press **Continue**.   
![b4](images/b4.jpg)  
6.	Don’t enter the payment info.   
![b5](images/b5.jpg)  
7.	Finally, choose the cluster name and press **Launch cluster**  
![b6](images/b6.jpg)  
## Create a topic, producer and consumer using the GUI
1.	Go to [the Confluent Kafka home page](https://confluent.cloud/home).
2.	Click **View environments**.  
![c1](images/c1.jpg)  
3.	Select the default environment.  
![c2](images/c2.jpg)  
4.	Select the cluster according to its name.  
![c3](images/c3.jpg)  
5.	Create a topic by selecting **topics**. Then click on **Create topic**.  
![c4](images/c4.jpg)  
6.	Choose the topic name as **testTopic** and you can leave the number of partitions to the default value of 6. Also, by clicking on **Show advanced settings**. Thus, you can change the **Cleanup policy**, **Retention time**, **Retention size**, and **maximum message size**. For now, you clean leave them with the default values. Finally, click **create with defaults** to create the topic.  
![c5](images/c5.jpg)  
7.	In the **testTopic** page, create **messages** tap which allows you to produce and consume messages.  
![c6](images/c6.jpg)  
8.	Click on **+ Producer a new message to this topic** shown in the previous figure. A default value/key message will be generated for you. 
The value is in a JSON format, but we can change it to a plain string. The key also is a number, but it can also be a string.  
Change the **value** to **“Hello Kafka”** and the **key** to **1**. Then click **Produce**.  
![c7](images/c7.jpg)   
9.	It will be automatically consumed in the consumer region. The partition will be determined by hashing the key value.  
![c8](images/c8.jpg)   
10.	Produce more messages. The consumer part should look like  
![c9](images/c9.jpg)   
11.	If you refreshed the page, the consumption area will be empty because all messages were consumed before.  
## Create a Topic, Producer and Consumer Using Python Code
1.	To create a Kafka client, either a producer or a consumer using a language of your choice. Click Dashboard. Then, at the Set up client area, click Get started. Click Set up a new client to get a template of a given language.
 
2.	Inspired by the given template, this section will guide you to write a python script for a consumer and a producer. The first step is to get an API key for a credential that enables you to create to the Kafka cluster. Start by clicking API keys. Then, click Create key.
 
3.	To make your life easier, choose Global access. Then, click next.
 
4.	Click Download and continue. A text file will be downloaded containing the values of the API key, the API secret, and the address of the Bootstrap server.
5.	Once created, API keys will show a list of already created keys to redownload.
Note: The following steps should run on your local computer to act as a data source that is located outside the cloud. The following set of python codes will create a topic named “testTopic2” to produce and consume messages from
6.	Install the python library
pip install confluent-kafka[avro,json,protobuf]
7.	Copy the file from folder v1 from the GitHub repository to a certain folder in your computer.
8.	Edit the cred.json and replace <Bootstrap servers>, <CLUSTER_API_KEY>, and  <CLUSTER_API_SECRET> by the values of Bootstrap server, API key, and API secret you got in step 4 in this section. Save the file to be used of a credential for the three python scripts.
 
9.	createTopic.py is the script used to create a topic. Edit the file and change the topic name in line 8th from “<topicname>” to “testTopic2”. You can change the default values of the number of partitions and the replication factor at lines 9 and 10. The credential will be read from the cred.json file according to the python statement in line 7. The cred.json and createTopic.py should be in the same folder. In line 12, an admin client has the privileged to create topics. The statement in lines 14 to 16 creates an array of new topics that contains only a single topic. The array is passed to a createTopics function to create the topics. The loop starting from line 18 goes through the results of createTopics and prints a summary of the creation results.
 
Save the file and run it, the output should look like
 
10.	producer.py is a python script that produces messages to a topic. Following the same technique change the topic name in line 8 to “testTopic2”. The second marked box in the following figure is a call back function that prints the output of each produce function that sends a message to the Kafka. The code in the third rectangle reads two strings and an integer that represents the key, value and the partition number from the user. Entering any integer less than -1 will stop the loop. The fourth box sends the message via produce function and invokes the call back function using the poll function. The last box flushes the producer internal buffer to ensure that all messages are already sent before ending the program.

 
11.	The final script is consumer.py. As usual, change the topic name in line 6 to “testTopic2”. The group id is given in the 11th line. Consumers of the same group id will cooperate to read messages from the topic. The group id can be any string. The third rectangle marked in the following figure creates a consumer and subscribes it to the topic. Note, the consumer can subscribe to a set of topics. The poll function at the 23rd line reads messages from the topic. The fifth rectangle marks the code that prints the status and output of the consume function. The last box will end the consumer once Ctrl-C is pressed by the user that will trigger the KeyboardInterrupt.
 
