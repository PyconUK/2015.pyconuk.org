type: session
title: "Instrument Your Python App with Metric Collection"
slug: "instrument-your-python-app-with-metric-collection"
url: "talks/instrument-your-python-app-with-metric-collection/index.html"
body_class_hack: talks
---

### Marek Mroz

Brief Description
-----
Metrics gathering and visualization is a standard practice for systems and operations engineers. While not as commonly used in the data science world, metric collection tools and techniques can be useful for scientific computing projects. In this talk I will show how to instrument an application to collect metrics, and create a dashboard view to monitor and explore the collected data.


Detailed description
-----
InfluxDB is an open-source distributed time series database that is easy to set up and to get started with. Grafana is a dashboarding tool that works with InfluxDB and other time series back-ends. In this talk I will use a practical example to present how to integrate a Python application with InfluxDB, explore the visualization capabilities that Grafana brings to the table, and show practical examples of insights that can be gained from instrumenting Python applications with metric collection.

"Log everything" is a great piece of advice for any project, whether doing exploratory research or deploying a system to production. Logs are invaluable for debugging and investigating specific issues. However, individual logs are only snapshots of application runs in time, and as the project grows and begins to incorporate multiple services, data processing pipelines, and compute resources, the value that can be immediately derived from bare logs diminishes. Logs also tend to be wordy, and the more you log, the harder it is to find the relevant information.

Traditionally time series databases were used to collect system metrics, but they can be equally useful in gathering application specific metrics. Logs can be complemented by metric gathering tools, which collect the data that you care about and expose it in an easy to query and to present manner. In conjunction with intuitive visualization and dashboarding provided by Grafana, InfluxDB can give great insight into inner workings of a system, and bring together all the disparate information into an interface that makes metric data exploration convenient. The two tools can help analyze performance bottlenecks, algorithm deficiencies, and resource constraints.