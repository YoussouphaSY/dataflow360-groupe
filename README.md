
#  DataFlow360

##  Objectif du projet

**DataFlow360** est une plateforme modulaire de traitement de données en **temps réel** (streaming) et en **batch**, déployée dans un environnement conteneurisé via **Docker**.  
Ce projet vise à simuler un système de données professionnel, allant de la **génération** à la **valorisation** des données, en passant par leur **ingestion**, **transformation**, **stockage**, **monitoring** et **exploitation** via **BI** ou **Machine Learning**.

---

##  Architecture globale

```
graph TD
    A[Génération de données (generator)] --> B[Ingestion (stockage_data)]
    B --> C[Stockage dans le data lake (data_lake)]
    C --> D[Nettoyage & Transformation (ETL)]
    D --> E[Stockage dans data warehouse (data_warehouse)]
    E --> F[Analyse & Dashboard (BI)]
    B -->|Streaming (Kafka)
```

---

##  Structure du projet

```
DataFlow360/
├── generator/              # Scripts Python pour générer les données (batch & streaming)
├── kafka_streaming/        # Configuration Kafka, topics, producteurs/consommateurs
├── consumers/              # Consumers Kafka pour MongoDB, Redis, Elasticsearch
├── etl/                    # Pipelines ETL batch pour les traitements des données
├── data_warehouse/         # Scripts SQL et de chargement vers PostgreSQL
├── elk/                    # Stack ELK (Elasticsearch, Logstash, Kibana)
├── bi/                     # Tableau de bord BI 
├── docker/                 # Dockerfiles et docker-compose.yml
├── .env                    # Variables d’environnement
└── README.md
├── orchestration/          # Airflow....
├── stockage_data/          # stckage des donnes(comme sources)
```

---

##  Fonctionnalités principales

-  **Génération de données**
  - Données simulées (Agriculture) en **batch** ou **temps réel**
  - Formats multiples : CSV, JSON, YAML, Excel, XML

-  **Ingestion et transformation**
  - Kafka pour ingestion en continu (streaming)
  - Pipelines ETL codés en Python ou orchestrés avec **Airflow**

-  **Stockage des données**
  - Bases relationnelles : **PostgreSQL**, **MySQL**
  - NoSQL : **MongoDB**, **Cassandra**, **Neo4j**
  - Cache rapide : **Redis**
  - Stockage centralisé : **Data Warehouse PostgreSQL**

-  **Monitoring & Logs**
  - Stack **ELK** (Elasticsearch, Logstash, Kibana)
  - Suivi des événements Kafka, erreurs, indicateurs système

-  **Exploitation des données**
  - **BI** : Tableaux de bord interactifs (Power BI, Tableau)

---

##  Lancement rapide

