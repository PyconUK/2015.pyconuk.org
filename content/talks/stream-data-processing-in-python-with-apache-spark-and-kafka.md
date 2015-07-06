type: session
title: "Stream Data processing in Python with Apache Spark and Kafka"
slug: "stream-data-processing-in-python-with-apache-spark-and-kafka"
url: "talks/stream-data-processing-in-python-with-apache-spark-and-kafka/index.html"
body_class_hack: talks
---

### Peter Hoffmann

[Apache Spark][] is a computational engine for large-scale data processing. It
is responsible for scheduling, distribution and monitoring applications which
consist of many computational task across many worker machines on a computing
cluster. [Apache Kafka][]  is publish-subscribe messaging based on a
distributed, partitioned, replicated commit log service.


This talk will give an overview into Apache Spark with a focus on PySpark
Streaming, the API for real-time streaming data processing.  While Spark Core
itself is written in Scala and runs on the JVM, PySpark exposes the Spark
programming model to Python. The high-level abstraction to live input data
streams are so called discretized streams or DStreams. DStreams group input 
streams as a series of short batch jobs. Each item in a DStream
is a Resilient Distributed Dataset (RDD). RDDs are a distributed memory
abstraction that lets programmers perform in-memory computations. RDDs are
immutable, partitioned collections of objects. Transformations construct a new
RDD from a previous one. Actions compute a result based on an RDD. Multiple
computation steps are expressed as directed acyclic graph (DAG). The DAG
execution model is a generalization of the Hadoop MapReduce computation model.


Resources:

- [An Architecture for Fast and General Data Processing on Large Clusters] Matei Zaharia
- [Spark] Cluster Computing with Working Sets - Matei Zaharia et al.
- [Discretized Streams][] An Efficient and Fault-Tolerant Model for Stream Processing on Large Clusters - Matei Zaharia et al.
- [Learning Spark][] Lightning Fast Big Data Analysis - Oreilly
- [Advanced Analytics with Spark][] Patterns for Learning from Data at Scale - Oreilly


[An Architecture for Fast and General Data Processing on Large Clusters]: http://www.eecs.berkeley.edu/Pubs/TechRpts/2014/EECS-2014-12.pdf
[Learning Spark]: http://shop.oreilly.com/product/0636920028512.do
[Advanced Analytics with Spark]: http://shop.oreilly.com/product/0636920035091.do
[Resilient Distributed Datasets]: https://www.cs.berkeley.edu/~matei/papers/2012/nsdi_spark.pdf
[Discretized Streams]: https://www.cs.berkeley.edu/~matei/papers/2012/hotcloud_spark_streaming.pdf
[Spark]: http://www.cs.berkeley.edu/~matei/papers/2010/hotcloud_spark.pdf
[Apache Spark]: https://spark.apache.org
[Apache Kafka]: http://kafka.apache.org