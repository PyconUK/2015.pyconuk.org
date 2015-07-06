type: session
title: "With flexibility comes responsibilty: Getting schemas around semi-structured data using Avro and Python !!"
slug: "with-flexibility-comes-responsibilty-getting-schemas-around-semi-structured-data-using-avro-and-python-"
url: "talks/with-flexibility-comes-responsibilty-getting-schemas-around-semi-structured-data-using-avro-and-python-/index.html"
body_class_hack: talks
---

### Konark Modi

In this world of big-data where we are producing data of enormous variety, velocity, volume and the nature being semi-structured we need to put some rules around data being collected which are not rigid yet allow efficient management of it right from collection layer.

My talk is based on first-hand experience that me and my team had while writing frameworks and data pipelines , we like anyone else started with collecting data in JSON format. But soon started to run into problems because of systems which were writing the data were abusing the flexibility.

More importantly how we can leverage Python with this and makes it interoperable with various Big Data techologies.

Schemas  / Serialization is a layer not many people talk about , but in my experience it is very useful and one can benefit from it in many many ways.


The agenda of the talk is as follows :

1. Need of a schema / serialization.
2. Avro and why is it so awesome.
3. Demo of creating some schemas and showcasing the features.
4. How Avro serialized data can be used across different layers / tools in the BigData pipeline. Be it Realtime processing system like Kafka with Storm or Batch processing system like Hadoop, Hive etc.
5. Setting up your AVRO schema repository to help people create, distrubute and manage schemas. A pure Django based implementation.
6.  Do's and Don'ts .


Who should Attend :

I plan to keep it beginner friendly, any one who has been or is doing data collection at any level can benefit from this talk. 