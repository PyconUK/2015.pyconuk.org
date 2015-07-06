type: session
title: "Exploring MicroServices for Cloud with Apache Thrift and Python"
slug: "exploring-microservices-for-cloud-with-apache-thrift-and-python"
url: "talks/exploring-microservices-for-cloud-with-apache-thrift-and-python/index.html"
body_class_hack: talks
---

### Chetan Giridhar

Many web applications start off as a monolithic code base, then move to a more distributed system. Large reports could take several minutes (and, sometimes, hours!) to complete, and users would become impatient waiting for their browser to finally display the result or the website would have already crossed limitations of how many requests it can handle.
Service Oriented Architecture or MicroServices present a cleaner alternative to make system more distributed and adapt to current needs of the cloud. Not only does this improve scalability & resiliency, but it makes services independent entities operating on their own - which essentially means freedom of language & deployment. However in this model - the contract (also called as interface) between services is well understood and maintained.
Apache Thrift, an open sourced framework demo Facebook, helps you in defining an Interface Definition Language file that help you:
	1.	Strict contract across services
	2.	Easy proof of concept with stubs
	3.	Freedom to still implement your own business logic
	4.	Minimise design level confusions

During the talk we would discuss about
	•	Issues with monolithic web architecture
	•	SOA and Microservices
	•	Apache thrift
	•	Example implementation with use case
	•	Discuss about performance of Apache Thrift 
