pip install poetry
poetry init

# adicionando dependencias
#dependencias dev
# após configurar e gerar o arquivo toml:
poetry install

--
# verifica vesões ocrretas:
poetry.lock 

# flake8 configuração de visualização de colunas de código
setup.cfg

# especificações para o editor de código:
.editorconfig



---



instalar mongo na maquina ou 

mongo express:

# conexão com o mongo
docker-compose.yml


--

#Primeiramente, atualize a lista de pacotes para ter a versão mais recente dos registros:
sudo apt update

#Agora, instale o pacote MongoDB:
sudo apt install -y mongodb


#verifique o estado do serviço:
sudo systemctl status mongodb

# resultado:

● mongodb.service - An object/document-oriented database
   Loaded: loaded (/lib/systemd/system/mongodb.service; enabled; vendor preset: enabled)
   Active: active (running) since Thu 2021-09-23 16:12:17 UTC; 1min 4s ago
     Docs: man:mongod(1)
 Main PID: 30078 (mongod)
    Tasks: 23 (limit: 4915)
   CGroup: /system.slice/mongodb.service
           └─30078 /usr/bin/mongod --unixSocketPrefix=/run/mongodb --config /etc/mongodb.conf
Sep 23 16:12:17 cluster-rodglins-m systemd[1]: Started An object/document-oriented database.

---

# Isso mostrará a versão atual do banco de dados, o endereço e a porta do servidor, e o resultado do comando de estado:
mongo --eval 'db.runCommand({ connectionStatus: 1 })'

Resultado:

MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
{
        "authInfo" : {
                "authenticatedUsers" : [ ],
                "authenticatedUserRoles" : [ ]
        },
        "ok" : 1
}



---

Docker:

olindaglins@cluster-rodglins-m:~$ sudo systemctl status docker
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
   Active: active (running) since Thu 2021-09-23 16:43:15 UTC; 11s ago
     Docs: https://docs.docker.com
 Main PID: 12481 (dockerd)
    Tasks: 13
   CGroup: /system.slice/docker.service
           └─12481 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
Sep 23 16:43:15 cluster-rodglins-m dockerd[12481]: time="2021-09-23T16:43:15.217949369Z" level=warning msg="Your ker
Sep 23 16:43:15 cluster-rodglins-m dockerd[12481]: time="2021-09-23T16:43:15.217956709Z" level=warning msg="Your ker
Sep 23 16:43:15 cluster-rodglins-m dockerd[12481]: time="2021-09-23T16:43:15.217963262Z" level=warning msg="Your ker
Sep 23 16:43:15 cluster-rodglins-m dockerd[12481]: time="2021-09-23T16:43:15.218259508Z" level=info msg="Loading con
Sep 23 16:43:15 cluster-rodglins-m dockerd[12481]: time="2021-09-23T16:43:15.318098905Z" level=info msg="Default bri
Sep 23 16:43:15 cluster-rodglins-m dockerd[12481]: time="2021-09-23T16:43:15.382796944Z" level=info msg="Loading con
Sep 23 16:43:15 cluster-rodglins-m dockerd[12481]: time="2021-09-23T16:43:15.420942135Z" level=info msg="Docker daem
Sep 23 16:43:15 cluster-rodglins-m dockerd[12481]: time="2021-09-23T16:43:15.421169650Z" level=info msg="Daemon has 
Sep 23 16:43:15 cluster-rodglins-m dockerd[12481]: time="2021-09-23T16:43:15.459709133Z" level=info msg="API listen 
Sep 23 16:43:15 cluster-rodglins-m systemd[1]: Started Docker Application Container Engine.

---


sudo docker network ls 

sudo docker run -it --rm \
    --network 127.0.0.1 \
    --name mongo-express \
    -p 8081:8081 \
    -e ME_CONFIG_OPTIONS_EDITORTHEME="ambiance" \
    -e ME_CONFIG_MONGODB_SERVER="web_db_1" \
    -e ME_CONFIG_BASICAUTH_USERNAME="" \
    -e ME_CONFIG_BASICAUTH_PASSWORD="" \
    mongo-express


--

/home/olindaglins/twitter/src

cp -r ~/twitter/* ~/miniconda3/lib/python3.8/twitter
cp ~/miniconda3/lib/python3.8/twitter/src/* ~/miniconda3/lib/python3.8/
twitter



pip install uvicorn
pip install fastapi
pip install pymongo
pip install tweepy


---


> show dbs
> admin     0.000GB
> config    0.000GB
> local     0.000GB
> rodglins  0.000GB
> show users
> use rodglins
> switched to db rodglins
> show collections
> trends
>

se
sudo systemctl status mongodb
sudo systemctl start mongodb

 Memory usage: 62%                IP address for ens4:    10.128.0.6
  Swap usage:   0%                 IP address for docker0: 172.17.0.1


----


id" : ObjectId("614ceed8b2cdc12d4917cdc3"), "name" : "#Transcendendo", "url" : "http://twitter.com/search?q=
%23Transcendendo", "promoted_content" : null, "query" : "%23Transcendendo", "tweet_volume" : null }
{ "_id" : ObjectId("614ceed8b2cdc12d4917cdc4"), "name" : "Bolsa de Valores", "url" : "http://twitter.com/search?
q=%22Bolsa+de+Valores%22", "promoted_content" : null, "query" : "%22Bolsa+de+Valores%22", "tweet_volume" : 21864
 }
{ "_id" : ObjectId("614ceed8b2cdc12d4917cdc5"), "name" : "#VerdadesSecretas2", "url" : "http://twitter.com/searc
h?q=%23VerdadesSecretas2", "promoted_content" : null, "query" : "%23VerdadesSecretas2", "tweet_volume" : null }
{ "_id" : ObjectId("614ceed8b2cdc12d4917cdc6"), "name" : "LA RAFA EST BELLE", "url" : "http://twitter.com/search
?q=%22LA+RAFA+EST+BELLE%22", "promoted_content" : null, "query" : "%22LA+RAFA+EST+BELLE%22", "tweet_volume" : nu
ll }
{ "_id" : ObjectId("614ceed8b2cdc12d4917cdc7"), "name" : "Boulos", "url" : "http://twitter.com/search?q=Boulos",
 "promoted_content" : null, "query" : "Boulos", "tweet_volume" : null }
{ "_id" : ObjectId("614ceed8b2cdc12d4917cdc8"), "name" : "Las Vegas", "url" : "http://twitter.com/search?q=%22La
s+Vegas%22", "promoted_content" : null, "query" : "%22Las+Vegas%22", "tweet_volume" : 22197 }
{ "_id" : ObjectId("614ceed8b2cdc12d4917cdc9"), "name" : "#LaLigaNaESPN", "url" : "http://twitter.com/search?q=%
23LaLigaNaESPN", "promoted_content" : null, "query" : "%23LaLigaNaESPN", "tweet_volume" : null }
{ "_id" : ObjectId("614ceed8b2cdc12d4917cdca"), "name" : "#VisibilidadeBi", "url" : "http://twitter.com/search?q
=%23VisibilidadeBi", "promoted_content" : null, "query" : "%23VisibilidadeBi", "tweet_volume" : null }
{ "_id" : ObjectId("614ceed8b2cdc12d4917cdcb"), "name" : "Girão", "url" : "http://twitter.com/search?q=Gir%C3%A3
o", "promoted_content" : null, "query" : "Gir%C3%A3o", "tweet_volume" : null }
{ "_id" : ObjectId("614ceed8b2cdc12d4917cdcc"), "name" : "POLIETTE NO TVZ", "url" : "http://twitter.com/search?q
=%22POLIETTE+NO+TVZ%22", "promoted_content" : null, "query" : "%22POLIETTE+NO+TVZ%22", "tweet_volume" : null }
{ "_id" : ObjectId("614ceed8b2cdc12d4917cdcd"), "name" : "Depay", "url" : "http://twitter.com/search?q=Depay", "
promoted_content" : null, "query" : "Depay", "tweet_volume" : null }
{ "_id" : ObjectId("614ceed8b2cdc12d4917cdce"), "name" : "Bovespa", "url" : "http://twitter.com/search?q=Bovespa
", "promoted_content" : null, "query" : "Bovespa", "tweet_volume" : null }
{ "_id" : ObjectId("614ceed8b2cdc12d4917cdcf"), "name" : "Koeman", "url" : "http://twitter.com/search?q=Koeman",
 "promoted_content" : null, "query" : "Koeman", "tweet_volume" : 39831 }
{ "_id" : ObjectId("614ceed8b2cdc12d4917cdd0"), "name" : "Zico", "url" : "http://twitter.com/search?q=Zico", "pr
omoted_content" : null, "query" : "Zico", "tweet_volume" : null }
{ "_id" : ObjectId("614ceed8b2cdc12d4917cdd1"), "name" : "Rolex", "url" : "http://twitter.com/search?q=Rolex", "
promoted_content" : null, "query" : "Rolex", "tweet_volume" : 15334 }
{ "_id" : ObjectId("614ceed8b2cdc12d4917cdd2"), "name" : "Flávio Bolsonaro", "url" : "http://twitter.com/search?
q=%22Fl%C3%A1vio+Bolsonaro%22", "promoted_content" : null, "query" : "%22Fl%C3%A1vio+Bolsonaro%22", "tweet_volum
e" : 10194 }
{ "_id" : ObjectId("614ceed8b2cdc12d4917cdd3"), "name" : "Luuk De Jong", "url" : "http://twitter.com/search?q=%2
2Luuk+De+Jong%22", "promoted_content" : null, "query" : "%22Luuk+De+Jong%22", "tweet_volume" : null }


----


(base) olindaglins@cluster-rodglins-m:~/miniconda3/lib/python3.8/twitter$



gsutil mv ~/twitter/* gs://rodglinstwitter

(base) olindaglins@cluster-rodglins-m:~/twitter/src$ gsutil mv ~/twitter/* gs://rodglinstwitter/twitter


gsutil cp -r  ~/miniconda3/lib/python3.8/twitter/* gs://
rodglinstwitter/twitter




gsutil -m cp -r \
  "gs://rodglinstwitter/twitter/" \
  .
