## Spark command
### Object 1 
To submit spark applications

[Details_submitting_applications](https://spark.apache.org/docs/latest/submitting-applications.html)

-  --verbose
>spark-submit --verbose spark/jobs/pipeline.py

If you are ever unclear where configuration options are coming from, you can print out fine-grained debugging information by running spark-submit with the --verbose option.

- --deploy-mode
> spark-submit --deploy-mode cluster 

Whether to deploy your driver on the worker nodes (cluster) or locally as an external client (client) (default: client)

- --master
> spark-submit --master local[k]  
Run Spark locally with K worker threads (ideally, set this to the number of cores on your machine). 

> spark-submit --master spark://HOST:PORT
Connect to the given Spark standalone cluster master. The port must be whichever one your master is configured to use, which is 7077 by default. 

> spark-submit --master YARN
Connect to a  YARN  cluster in client or cluster mode depending on the value of --deploy-mode. The cluster location will be found based on the HADOOP_CONF_DIR or YARN_CONF_DIR variable.

Run Spark locally or connect to given master

### Object 2  
To monitor Spark applications: web UIs  
- access to Web UI
> http://<driver-node>:4040 