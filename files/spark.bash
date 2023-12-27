docker network ls

docker network create pouria-network

docker run -dit --rm -p 2442:8080 
 --name pouria-master --network pouria-network
  bitnami/spark   /opt/bitnami/spark/sbin/start-master.sh


docker run  -dit --rm --name pouria-worker1
  --network pouria-network
  -e SPARK_WORKER_MEMORY=2g   
  -e SPARK_WORKER_CORES=2  
  bitnami/spark 
  /opt/bitnami/spark/sbin/start-worker.sh spark://pouria-master:7077

docker ps
http://141.98.210.151:2442