# Twitter-Data-Analysis
Análise de dados do Twitter

## Projeto: Desafio Carrefour Análise Trend Topics

Twitter Nuvem de palavras

Twitter trend topics PySpark MongoDB

Twitter trend topics Flume HBase

Análise em Python / PowerBI

-------------

Por que MongoDB ou HBase?

São duas ótimas base de dados NoSQL e devem ser escolhidas conforme ambiente de trabalho e necessidade de uso. Enquanto a HBase é ótima em desempenho a MongoDB é excelente para aplicaões online. Abaixo uma comparação:

Both MongoDB vs HBase are popular choices in the market; let us discuss some of the major Differences: HBase vs MongoDB both being No SQL databases have significant differences. The query model of MongoDB provides different kinds of projections, filtering, and aggregate functions. Hbase, on the other hand, has a key-value pairing for data. For text search, MongoDB provides a native feature for text indexes and in HBase data is replicated for a search engine. MongoDB provides three nodes namely primary and secondary and one for replication. HBase has 10 nodes for masters, region servers, standby name nodes, data nodes, and zookeepers. In MongoDB partitioning can be done using a hash, range and zone sharding while HBase provides only hashing technique.In regards of backup and recovery, MongoDB has Ops manager and Atlas consistent which provides timely backups and sharded clusters. HBase takes snapshots of data every 60 seconds on each node of the cluster. Group by in MongoDB is performed by making use of aggregation pipeline and in HBase, it uses the Hadoop traditional map reduce. HBase is also an open source non-relational distributed database model. It was developed by Apache Foundation and runs on the Hadoop Distributed File System. It had begun by the company Powerset as they required large amounts of data. It is similar to Google’s big table and provides access to huge amounts of data. It is a part of the Hadoop ecosystem and data consumer can read and access the data using HBase. MongoDB is an open source document-oriented, NoSQL database program. It uses JSON documents with schemas. The development of MongoDB was started in 2007 by 10gen software. It is cross-platform and provides high availability and scalability. It works on collection and document concept. It mainly uses a database, collection, and document. 

Conclusion
HBase can be used when data is in the form of a key-value pair and has a high volume of data. MongoDB, on the other hand, can be used where the user wants to track the behavior of the user on an online application. HBase has high performance and scalability while MongoDB has a wide range of applications that it supports. It is the user who needs to decide if they would want better performance or want to support different applications

Referência:
https://www.educba.com/mongodb-vs-hbase/
