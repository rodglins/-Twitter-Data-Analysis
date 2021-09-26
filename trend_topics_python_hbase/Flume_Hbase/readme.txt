Projeto: Análise twitter utilizando Hbase, Zookeper, Dataproc, Spark



#Criando um projeto:

projeto>>>> dataprocRodglins
Cluster>>>>cluster-rodglins

Criando um bucket:

Bucket: rodglinstwitter
https://console.cloud.google.com/storage/browser/rodglinstwitter
gs://rodglinstwitter

# Buckets:

gs://dataproc-temp-us-central1-642474987509-i7u3zqqe/
gs://gcs-bucket-service-8713-e1ea740b-7c5e-4423-b76e-3705b7114e0c/
gs://rodglinstwitter/

# arquivo para abrir no PySpark
gs://rodglinstwitter/trend_analysis_spark.py

gcloud dataproc jobs wait job-trend-spark --project dataprocrodglins --region us-central1


---

# Configurações:
ZooKeeper Base Path	/hbase
Cluster Key	cluster-rodglins-m:2181:/hbase
HBase Root Directory	/gateway/default/webhdfs/v1/hbase







---------

# criação um cluster em REST:
gcloud dataproc clusters create cluster-rodglins --enable-component-gateway --bucket rodglinstwitter --region us-central1 --zone us-central1-b --master-machine-type n1-standard-4 --master-boot-disk-size 500 --num-workers 3 --worker-machine-type n1-standard-4 --worker-boot-disk-size 500 --image-version 2.0-ubuntu18 --optional-components JUPYTER,ZEPPELIN,ZOOKEEPER,HBASE --project dataprocrodglins


# Criando um cluster Dataproc:
gcloud beta dataproc clusters create cluster-name \
    --optional-components=HBASE,ZOOKEEPER \
    --region=region \
    --image-version=1.5 \
    --enable-component-gateway \
    ... other flags

------

# Propriedades do cluster cluster-rodglins
capacity-scheduler:yarn.scheduler.capacity.root.default.ordering-policy
fair
core:fs.gs.block.size
134217728
core:fs.gs.metadata.cache.enable
false
core:hadoop.ssl.enabled.protocols
TLSv1,TLSv1.1,TLSv1.2
distcp:mapreduce.map.java.opts
-Xmx768m
distcp:mapreduce.map.memory.mb
1024
distcp:mapreduce.reduce.java.opts
-Xmx768m
distcp:mapreduce.reduce.memory.mb
1024
hadoop-env:HADOOP_DATANODE_OPTS
-Xmx512m
hbase-env:HBASE_HEAPSIZE
12624m
hdfs:dfs.datanode.address
0.0.0.0:9866
hdfs:dfs.datanode.http.address
0.0.0.0:9864
hdfs:dfs.datanode.https.address
0.0.0.0:9865
hdfs:dfs.datanode.ipc.address
0.0.0.0:9867
hdfs:dfs.namenode.handler.count
40
hdfs:dfs.namenode.http-address
0.0.0.0:9870
hdfs:dfs.namenode.https-address
0.0.0.0:9871
hdfs:dfs.namenode.lifeline.rpc-address
cluster-rodglins-m:8050
hdfs:dfs.namenode.secondary.http-address
0.0.0.0:9868
hdfs:dfs.namenode.secondary.https-address
0.0.0.0:9869
hdfs:dfs.namenode.service.handler.count
20
hdfs:dfs.namenode.servicerpc-address
cluster-rodglins-m:8051
hive:hive.fetch.task.conversion
none
mapred-env:HADOOP_JOB_HISTORYSERVER_HEAPSIZE
3840
mapred:mapreduce.job.maps
33
mapred:mapreduce.job.reduce.slowstart.completedmaps
0.95
mapred:mapreduce.job.reduces
11
mapred:mapreduce.jobhistory.recovery.store.class
org.apache.hadoop.mapreduce.v2.hs.HistoryServerLeveldbStateStoreService
mapred:mapreduce.map.cpu.vcores
1
mapred:mapreduce.map.java.opts
-Xmx2524m
mapred:mapreduce.map.memory.mb
3156
mapred:mapreduce.reduce.cpu.vcores
1
mapred:mapreduce.reduce.java.opts
-Xmx2524m
mapred:mapreduce.reduce.memory.mb
3156
mapred:mapreduce.task.io.sort.mb
256
mapred:yarn.app.mapreduce.am.command-opts
-Xmx2524m
mapred:yarn.app.mapreduce.am.resource.cpu-vcores
1
mapred:yarn.app.mapreduce.am.resource.mb
3156
spark-env:SPARK_DAEMON_MEMORY
3840m
spark:spark.driver.maxResultSize
1920m
spark:spark.driver.memory
3840m
spark:spark.executor.cores
2
spark:spark.executor.instances
2
spark:spark.executor.memory
5739m
spark:spark.executorEnv.OPENBLAS_NUM_THREADS
1
spark:spark.scheduler.mode
FAIR
spark:spark.sql.cbo.enabled
true
spark:spark.ui.port
0
spark:spark.yarn.am.memory
640m
yarn-env:YARN_NODEMANAGER_HEAPSIZE
1536
yarn-env:YARN_RESOURCEMANAGER_HEAPSIZE
3840
yarn-env:YARN_TIMELINESERVER_HEAPSIZE
3840
yarn:yarn.nodemanager.address
0.0.0.0:8026
yarn:yarn.nodemanager.resource.cpu-vcores
4
yarn:yarn.nodemanager.resource.memory-mb
12624
yarn:yarn.resourcemanager.nodemanager-graceful-decommission-timeout-secs
86400
yarn:yarn.scheduler.maximum-allocation-mb
12624
yarn:yarn.scheduler.minimum-allocation-mb
1

--------

# Instalando o flume:

sudo wget http://archive.apache.org/dist/flume/1.9.0/apache-flume-1.9.0-bin.tar.gz
tar xzf apache-flume-1.9.0-bin.tar.gz
mv apache-flume-1.9.0-bin flume

Basta descompactar o arquivo e adicionar  .bashrc

Editando:
vi ~/.bashrc

Executando
source ~/.bashrc

source $HOME/.bashrc

# Adicionar:
# Flume
FLUME_CLASSPATH=/lib
export FLUME_HOME=~/flume
export PATH=$PATH:$FLUME_HOME/bin


---------

Criando pasta no hadoop:
sudo hadoop fs -mkdir /twitter_tweets
sudo hadoop fs -ls /twitter_tweets


#listando pasta HBase:
sudo hadoop fs -ls /hbase

@cluster-rodglins-m:/etc/hadoop/conf$ sudo hadoop fs -ls /hbase
Found 12 items
drwxr-xr-x   - root hadoop          0 2021-09-20 21:12 /hbase/.hbck
drwxr-xr-x   - root hadoop          0 2021-09-20 21:12 /hbase/.tmp
drwxr-xr-x   - root hadoop          0 2021-09-22 20:28 /hbase/MasterProcWALs
drwxr-xr-x   - root hadoop          0 2021-09-20 21:12 /hbase/WALs
drwxr-xr-x   - root hadoop          0 2021-09-20 21:12 /hbase/archive
drwxr-xr-x   - root hadoop          0 2021-09-20 21:12 /hbase/corrupt
drwxr-xr-x   - root hadoop          0 2021-09-20 21:13 /hbase/data
-rw-r--r--   2 root hadoop         42 2021-09-20 21:12 /hbase/hbase.id
-rw-r--r--   2 root hadoop          7 2021-09-20 21:12 /hbase/hbase.version
drwxr-xr-x   - root hadoop          0 2021-09-20 21:12 /hbase/mobdir
drwxr-xr-x   - root hadoop          0 2021-09-22 20:32 /hbase/oldWALs
drwx--x--x   - root hadoop          0 2021-09-20 21:12 /hbase/staging

-----

# Verificando versão do hadoop:

olindaglins@cluster-rodglins-m:/$ hadoop version
Hadoop 3.2.2
Source code repository https://bigdataoss-internal.googlesource.com/third_party/apache/hadoop -r 5dee0867618113e
dafb97f68d8aae96ff9e89bd1
Compiled by bigtop on 2021-08-26T20:35Z
Compiled with protoc 2.5.0
From source with checksum ba146be449aba4b4aae8987f1683cc
This command was run using /usr/lib/hadoop/hadoop-common-3.2.2.jar

-----

/etc/hadoop/conf/


capacity-scheduler.xml      hadoop-policy.xml           nodes_include
configuration.xsl           hdfs-site.xml               ssl-client.xml.example
container-executor.cfg      log4j.properties            ssl-server.xml.example
core-site.xml               mapred-env.sh               yarn-env.sh
distcp-default.xml          mapred-queues.xml.template  yarn-site.xml
hadoop-env.sh               mapred-site.xml             yarn-timelineserver.logging.properties
hadoop-metrics2.properties  nodes_exclude



-----




# Configurações do Hadoop:

hdfs-site.xml:

original:
<name>dfs.namenode.name.dir</name>
<value>file:/usr/local/hadoop-env/hadoop-2.7.0/yarn_data/hdfs/namenode</value>
usado:
   <name>dfs.namenode.name.dir</name>
    <value>/hadoop/dfs/name</value>

original:
<name>dfs.datanode.data.dir</name>
<value>file:/usr/local/hadoop-env/hadoop-2.7.0/yarn_data/hdfs/datanode</value>
usado:
    <name>dfs.datanode.data.dir</name>
    <value>/hadoop/dfs/data</value>


----


core-site:
    <name>fs.default.name</name>
    <value>hdfs://cluster-rodglins-m


----

# Configurações do cluster

    <name>dfs.datanode.data.dir</name>
    <value>/hadoop/dfs/data</value>

   <name>dfs.namenode.http-address</name>
    <value>0.0.0.0:9870</value>

    <name>dfs.namenode.http-address</name>
    <value>0.0.0.0:9870</value>
    <final>false</final>
    <source>Dataproc Cluster Properties</source>
  </property>
  <property>
    <name>dfs.permissions.supergroup</name>
    <value>hadoop</value>
    <description>The name of the group of super-users.</description>
  </property>
  <property>
    <name>dfs.hosts</name>
    <value>/etc/hadoop/conf/nodes_include</value>
  </property>
  <property>
    <name>dfs.namenode.datanode.registration.retry-hostname-dns-lookup</name>
    <value>true</value>
    <description>
      If true, then the namenode will retry reverse dns lookup for hostname of
      the       datanode. This helps in environments where DNS lookup can be
      flaky.
    </description>
  </property>
  <property>
    <name>dfs.namenode.secondary.http-address</name>
    <value>0.0.0.0:9868</value>
    <final>false</final>

----

    <name>dfs.namenode.name.dir</name>
    <value>/hadoop/dfs/name</value>
   <name>dfs.datanode.data.dir</name>
    <value>/hadoop/dfs/data</value>

# Inform. do cluster:
http://cluster-rodglins-m:8088/proxy/application_1632172312677_0001/
---


hdfs://localhost:54310/hbase



  <name>hbase.rootdir</name>
    <value>hdfs://cluster-rodglins-m/hbase

 <name>hbase.zookeeper.quorum</name>
    <value>cluster-rodglins-m:2181</value>


cluster-rodglins-m:8020


----
# Arquivos conf Hive:
olindaglins@cluster-rodglins-m:/etc/hive/conf$ ls
beeline-log4j2.properties.template  hive-site.xml
hive-default.xml.template           ivysettings.xml
hive-env.sh                         llap-cli-log4j2.properties.template
hive-exec-log4j2.properties         llap-daemon-log4j2.properties.template
hive-log4j2.properties              parquet-logging.properties

----


# Criando uma tabela no HBase:
# Antes de inserir os dados a tabela tem que existir


# iniciar
hbase shell

# Criar tabela
create 'twt_table', 'twt_cf'

# Acessando a tabela:
use 'twt_table'

# verificar conteúdo:
scan 'twt_table'

# limpar dados da tabela
truncate 'twt_table'

# iniciando o hbase
hbase master start


# Para exportar:

Take snapshot of the table
$ ./bin/hbase shell
hbase> snapshot 'myTable', 'myTableSnapshot-122112'

Export to the required file system
$ ./bin/hbase class org.apache.hadoop.hbase.snapshot.ExportSnapshot -snapshot MySnapshot -copy-to fs://path_to_your_directory

You can export it back from the local file system to hdfs:///srv2:8082/hbase and run the restore command from hbase shell to recover the table from the snapshot.
$ bin/hbase org.apache.hadoop.hbase.mapreduce.Export \
   <tablename> <outputdir> [<versions> [<starttime> [<endtime>]]]

$ bin/hadoop jar <path/to/hbase-{version}.jar> export \
     <tablename> <outputdir> [<versions> [<starttime> [<endtime>]]



----

Editando arquivo .conf na pasta conf

Flume:
vim flume.conf

#HBaseSink (org.apache.flume.sink.hbase.HBaseSink) supports secure HBase clusters and also the novel HBase IPC that was introduced in the version HBase 0.96.
#AsyncHBaseSink (org.apache.flume.sink.hbase.AsyncHBaseSink) has better performance than HBase sink as it can easily make non-blocking calls to HBase.

# ERRO: Versão incompatível, utilizar: HBase2Sink


HBase2Sink
HBase2Sink is the equivalent of HBaseSink for HBase version 2. The provided functionality and the configuration parameters are the same as in case of HBaseSink (except the hbase2 tag in the sink type and the package/class names).
a1.channels = c1
a1.sinks = k1
a1.sinks.k1.type = hbase2
a1.sinks.k1.table = foo_table
a1.sinks.k1.columnFamily = bar_cf
a1.sinks.k1.serializer = org.apache.flume.sink.hbase2.RegexHBase2EventSerializer
a1.sinks.k1.channel = c1

Twitter 1% firehose Source (experimental)
a1.sources = r1
a1.channels = c1
a1.sources.r1.type = org.apache.flume.source.twitter.TwitterSource
a1.sources.r1.channels = c1
a1.sources.r1.consumerKey = YOUR_TWITTER_CONSUMER_KEY
a1.sources.r1.consumerSecret = YOUR_TWITTER_CONSUMER_SECRET
a1.sources.r1.accessToken = YOUR_TWITTER_ACCESS_TOKEN
a1.sources.r1.accessTokenSecret = YOUR_TWITTER_ACCESS_TOKEN_SECRET
a1.sources.r1.maxBatchSize = 10
a1.sources.r1.maxBatchDurationMillis = 200

Flume Channels
a1.channels = c1
a1.channels.c1.type = memory
a1.channels.c1.capacity = 10000
a1.channels.c1.transactionCapacity = 10000
a1.channels.c1.byteCapacityBufferPercentage = 20
a1.channels.c1.byteCapacity = 800000


Modelos: https://flume.apache.org/FlumeUserGuide.html


twtagent.sinks.hbaseSink.table=twt_table
#twtagent.sinks.hbaseSink.serializer=org.apache.flume.sink.hbase.SplittingSerializer
twtagent.sinks.hbaseSink.serializer.columns=tweet:nothing
twtagent.sinks.hbaseSink.serializer.regex=(\\d+)\\s(\\S+)\\s(\\S+)\\s(\\d+)\\s(.+)
#twtagent.sinks.hbaseSink.serializer.colNames=id,first_name,last_name,age,gpa
twtagent.sinks.hbaseSink.serializer=org.apache.flume.sink.hbase.SimpleHbaseEventSerializer
twtagent.sinks.hbaseSink.serializer.payloadColumn=col1
twtagent.sinks.hbaseSink.serializer.incrementColumn=col1
#twtagent.sinks.hbaseSink.serializer.keyType=timestamp
twtagent.sinks.hbaseSink.serializer.rowPrefix=1+
twtagent.sinks.hbaseSink.serializer.suffix=timestamp

---------


Iniciando o agente Flume:

Testes:

./bin/flume-ng agent --conf ./conf --conf-file ./conf/twitter-flume-hdfs.conf --name twtagent -Dflume.root.logger=INFO,console

ERRO:
/usr/lib/hadoop/libexec//hadoop-functions.sh: line 2460: HADOOP_ORG.APACHE.HADOOP.HBASE.UTIL.GETJAVAPROP
ERTY_OPTS: bad substitution

./bin/flume-ng agent -f conf/twitter-flume-hdfs.conf -c conf -n twtagent


/bin/flume-ng agent -n twtagent -c conf -f conf/twitter-flume-hdfs.conf -Dflume.root.logger=INFO,console

./bin/flume-ng agent --conf-file ./conf/twitter-flume-hdfs.conf --name $twtagent -Dflume.root.logger=INFO,console

./bin/flume-ng agent $twtagent -c conf -f conf/twitter-flume-hdfs.conf -Dflume.root.logger=INFO,console

./bin/flume-ng agent --conf ./conf --conf-file ./conf/twitter-flume-hdfs.conf --name twtagent -Dflume.root.logger=INFO,console

~/flume/bin/flume-ng  agent -n twtagent -c conf -f ~/flume/conf/flume.conf -Dflume.root.looger=DEBUG,console

~/flume/bin/flume-ng agent --conf ~/flume/conf -f ~/flume/conf/flume.conf -Dflume.root.logger=DEBUG,console -n twtagent

~/flume/bin/flume-ng agent --conf ~/flume/conf --conf-file ~/flume/conf/flume.conf --name twtagent (não funciona)

~/flume/bin/flume-ng agent -n twtagent -c conf -f 

~/flume/bin/flume-ng agent --conf conf --conf-file flume.conf --name twtagent -Dflume.root.logger=INFO,console

~/flume/bin/flume-ng  agent -n twtagent -c conf -f ~/flume/conf/flume.conf -Dflume.root.looger=DEBUG,console

~/flume/bin/flume-ng agent --conf ~/flume/conf -f ~/flume/conf/flume.conf -Dflume.root.logger=DEBUG,console -n twtagent

# Erro na execução do flume, ajustar linha de comando
09-24 20:34:58,101 INFO client.RpcRetryingCallerImpl: Call exception, tries=12, retries=16, started=68495 m
s ago, cancelled=false, msg=java.io.IOException: org.apache.hadoop.hbase.shaded.org.apache.zookeeper.KeeperExcep
tion$NoNodeException: KeeperErrorCode = NoNode for /hbase/master, details=, see https://s.apache.org/timeout


# esse le mas nao grava
~/flume/bin/flume-ng agent --conf ~/flume/conf -f ~/flume/conf/flume.conf -Dflume.root.logger=DEBUG,console -n twtagent

# grava mas não le:
~/flume/bin/flume-ng agent --conf conf --conf-file flume.conf --name twtagent -Dflume.root.logger=INFO,console

teste1
~/flume/bin/flume-ng agent --conf ~/flume/conf -f ~/flume/conf/flume.conf --name twtagent -Dflume.root.logger=DEBUG,console
2
~/flume/bin/flume-ng agent --conf conf --conf-file flume.conf --name twtagent -Dflume.root.logger=DEBUG,console
3
~/flume/bin/flume-ng agent --conf ~/flume/conf --conf-file flume.conf --name twtagent -Dflume.root.logger=DEBUG,console
4

~/flume/bin/flume-ng agent –conf ~/flume/conf/flume.conf -z cluster-0910-m:2181,cluster-0910-m:2181 -p ~/flume –name a1 -Dflume.root.logger=INFO,console


------


# Erro duplicação: Estes arquivos não podem ser duplicados no sistema:
/home/olindaglins/flume/lib/slf4j-log4j12-1.7.25.jar

-- error:
SLF4J: Class path contains multiple SLF4J bindings.
:/usr/lib/zookeeper/contrib/rest$ sudo vim pom.xml

adicionando:
<exclusions>
    <exclusion>
        <groupId>org.slf4j</groupId>
        <artifactId>slf4j-log4j12</artifactId>
    </exclusion>
</exclusions>


LF4J: Found binding in [jar:file:/lib/slf4j-log4j12-1.6.1.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/lib/slf4j-log4j12-1.7.25.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/usr/lib/hadoop/lib/slf4j-log4j12-1.7.25.jar!/org/slf4j/impl/StaticLoggerBinde
r.class]
SLF4J: Found binding in [jar:file:/slf4j-log4j12-1.7.25.jar!/org/slf4j/impl/StaticLoggerBinder.class]

---


# erro: Flume Twitter: Could not configure channel MemChannel
Solução: 
erros no MemChannel, verificar existem e se estão corretos

------

# Erro de versão:
Solução:
wget http://files.cloudera.com/samples/flume-sources-1.0-SNAPSHOT.jar





-----



Erro: Flume agent failed because dependencies were not found in classpath
Resolvido

copied comon jar files from hadoop folder to the flume folder.

cp /usr/lib/hadoop/*.jar /lib
cp /usr/lib/hadoop/lib/*.jar /lib
Now the above error is rectified.
https://community.cloudera.com/t5/Support-Questions/Flume-agent-failed-because-dependencies-were-not-found-in/m-p/118423#M81206


---


[ERROR - org.apache.flume.lifecycle.LifecycleSupervisor$Monito
rRunnable.run(LifecycleSupervisor.java:253)] Unable to start EventDrivenSourceRunner:

erro no agent
./bin/flume-ng agent -n $twtagent -c conf -f conf/twitter-flume-hdfs.conf -Dflume.root.logger=INFO,console


---


/usr/bin/hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.separator=',' -Dimporttsv.columns='HBASE_ROW_KEY


https://community.cloudera.com/t5/Support-Questions/Flume-Exception-in-thread-quot-Twitter4J-Async-Dispatcher-0/td-p/163865
https://twittercommunity.com/t/exception-in-thread-twitter4j-async-dispatcher-0-while-fetching-tweets-using-flume/91895/5


# Resolvendo erros, adicionando:
export JAVA_HOME=/usr/lib/jvm/adoptopenjdk-8-hotspot-amd64
export JAVA_OPTS="-Xms100m -Xmx2000m -Dcom.sun.management.jmxremote"
FLUME_CLASSPATH="/lib/*"
export HIVE_HOME=/usr/lib/hive
export HCAT_HOME=/usr/lib/hive-hcatalog


# Testando flume
flume-ng agent -n twtagent --conf /conf -f /conf/flume.conf -Dflume.root.logger=DEBUG,console -Dtwitter4j.streamBaseURL=https://stream.twitter.com/1.1/

Erro:
Exception in thread "Twitter Stream consumer-1[Receiving stream]" java.lang.OutOfMemoryError: Java heap space

 (conf-file-poller-0) [DEBUG - org.apache.flume.node.PollingPropertiesFileConfigurationProvider$FileWatcherRunnabl
e.run(PollingPropertiesFileConfigurationProvider.java:126)] Checking file:/conf/twitter-flume-hdfs.conf for changes

https://stackoverflow.com/questions/50349540/getting-java-lang-outofmemoryerror-java-heap-space-while-running-twitter-connec


------

# Atualizando versão Python de 2.2 para 3.8

Miniconda3-py38_4.10.3-Linux-x86_64.sh
/opt/conda/miniconda3/bin/python

sudo ln -sf /opt/conda/default/bin/python /opt/conda/default/bin/python3

/opt/conda/default/bin/python3


------



# Erro versão incompatível, substituindo arquivos:
sudo gsutil mv gs://rodglinstwitter/flume-sources-1.0-SNAPSHOT.jar /lib
sudo gsutil mv gs://rodglinstwitter/twitter4j-core-2.2.6.jar /lib
sudo gsutil mv gs://rodglinstwitter/twitter4j-media-support-2.2.6.jar /lib
sudo gsutil mv gs://rodglinstwitter/twitter4j-stream-2.2.6.jar /lib



# Duplicidade:

SLF4J

HADOOP_ORG.APACHE.HADOOP.HBASE.UTIL.GETJAVAPROPERTY_USER

SLF4J: Found binding in [jar:file:/usr/lib/hadoop/lib/slf4j-log4j12-1.7.25.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/usr/lib/hbase/lib/client-facing-thirdparty/slf4j-log4j12-1.7.25.jar!/org/slf4j/impl/StaticLoggerBinder.class]

(base) olindaglins@cluster-rodglins-m:/usr/lib/hbase/lib/client-facing-thirdparty$ 
sudo mv slf4j-api-1.7.25.jar 
 slf4j-api-1.7.25.jar.RENOMEADO
(base) olindaglins@cluster-rodglins-m:/usr/lib/hbase/lib/client-facing-thirdparty$ 
sudo mv slf4j-log4j12-1.7.25.jar slf4j-log4j12-1.7.25.jar.RENOMEADO


/usr/lib/hbase/lib/client-facing-thirdparty/slf4j-log4j12-1.7.25.jar




----
ERRO:

Page up
        at java.lang.StringBuilder.append(StringBuilder.java:190)
        at java.io.BufferedReader.readLine(BufferedReader.java:358)
        at java.io.BufferedReader.readLine(BufferedReader.java:389)
        at twitter4j.StatusStreamBase.handleNextElement(StatusStreamBase.java:85)
        at twitter4j.StatusStreamImpl.next(StatusStreamImpl.java:57)
        at twitter4j.TwitterStreamImpl$TwitterStreamConsumer.run(TwitterStreamImpl.java:478)
2021-09-24 14:16:26,789 ERROR twitter.TwitterSource: Exception while streaming tweets
org.apache.flume.ChannelException: Cannot commit transaction. Byte capacity allocated to store event body 552970
0.0reached. Please increase heap space/byte capacity allocated to the channel as the sinks may not be keeping up
 with the sources
        at org.apache.flume.channel.MemoryChannel$MemoryTransaction.doCommit(MemoryChannel.java:123)
        at org.apache.flume.channel.BasicTransactionSemantics.commit(BasicTransactionSemantics.java:151)
        at org.apache.flume.channel.ChannelProcessor.processEvent(ChannelProcessor.java:270)
        at org.apache.flume.source.twitter.TwitterSource.onStatus(TwitterSource.java:168)
        at twitter4j.StatusStreamImpl.onStatus(StatusStreamImpl.java:75)
        at twitter4j.StatusStreamBase$1.run(StatusStreamBase.java:114)
        at twitter4j.internal.async.ExecuteThread.run(DispatcherImpl.java:116)
2021-09-24 14:16:30,012 ERROR twitter.TwitterSource: Exception while streaming tweets
org.apache.flume.ChannelException: Cannot commit transaction. Byte capacity allocated to store event body 552970
0.0reached. Please increase heap space/byte capacity allocated to the channel as the sinks may not be keeping up
 with the sources


Info: Including Hadoop libraries found via (/usr/bin/hadoop) for HDFS access
/usr/lib/hadoop/libexec//hadoop-functions.sh: line 2365: HADOOP_ORG.APACHE.FLUME.TOOLS.GETJAVAPROPERTY_USER: bad
 substitution
/usr/lib/hadoop/libexec//hadoop-functions.sh: line 2460: HADOOP_ORG.APACHE.FLUME.TOOLS.GETJAVAPROPERTY_OPTS: bad
 substitution
Info: Including HBASE libraries found via (/usr/bin/hbase) for HBASE access
/usr/lib/hadoop/libexec//hadoop-functions.sh: line 2365: HADOOP_ORG.APACHE.HADOOP.HBASE.UTIL.GETJAVAPROPERTY_USE
R: bad substitution
/usr/lib/hadoop/libexec//hadoop-functions.sh: line 2460: HADOOP_ORG.APACHE.HADOOP.HBASE.UTIL.GETJAVAPROPERTY_OPT
S: bad substitution
/usr/lib/hadoop/libexec//hadoop-functions.sh: line 2365: HADOOP_ORG.APACHE.HADOOP.HBASE.UTIL.GETJAVAPROPERTY_USE
R: bad substitution
/usr/lib/hadoop/libexec//hadoop-functions.sh: line 2460: HADOOP_ORG.APACHE.HADOOP.HBASE.UTIL.GETJAVAPROPERTY_OPT
S: bad substitution

# Resolvido

---

# Verificando status do cluster:
gcloud dataproc clusters diagnose cluster-0910 --region=us-central1

# Iniciando o cluster:
gcloud dataproc clusters start cluster-0910 --region=us-central1


---



References:

https://iq.opengenus.org/trends-api-twitter/

https://www.cloudsigma.com/realtime-twitter-data-ingestion-using-flume/

http://ahikmat.blogspot.com/2014/08/streaming-twitter-tweets-to-hbase-with.html

https://www.cloudsigma.com/realtime-twitter-data-ingestion-using-flume/

https://qastack.com.br/ubuntu/127056/where-is-bashrc

https://community.cloudera.com/t5/Support-Questions/Can-Flume-be-used-with-HBase-How/td-p/123517

https://docs.cloudera.com/HDPDocuments/HDP3/HDP-3.1.4/hbase-data-access/hdag-Using-HBase-to-store-and-access-data.pdf

https://gist.github.com/jarrettmeyer/26b3e1fcd423071a7a6d

https://happybase.readthedocs.io/en/latest/user.html

https://data-flair.training/blogs/apache-flume-installation-tutorial/

https://prwatech.in/blog/hadoop/hadoop-flume-tutorial/

https://towardsdatascience.com/google-trends-api-for-python-a84bc25db88f