# Grabed Lab
![Resource group creation](./images/Screenshot%20(581).png)
!["raw" container creation](./images/Screenshot%20(582).png)
![Synapse creation](./images/Screenshot%20(583).png)
![SELECT TOP 100 * FROM OPENROWSET( BULK 'https://<storage-account>.dfs.core.windows.net/raw/*.parquet', FORMAT = 'PARQUET ) AS rows;](./images/Screenshot%20(584).png)
![Explore Data using Spark Notebook](./images/Screenshot%20(585).png)
![Explore Data using Spark Notebook](./images/Screenshot%20(586).png)
![Explore Data using Spark Notebook](./images/Screenshot%20(587).png)
![Data Transformation using Spark ](./images/Screenshot%20(589).png)
![Fix Data Types ](./images/Screenshot%20(590).png)
![Fix Data Types ](./images/Screenshot%20(591).png)
![Create Derived Columns ](./images/Screenshot%20(592).png)
![Write Transformed Data to Refined Zone](./images/Screenshot%20(594).png)
![Create External Table using SQL ](./images/Screenshot%20(595).png)
![Analyze & Visualize Data ](./images/Screenshot%20(596).png)
![Resource deletion](./images/Screenshot%20(596).png)


## findings
The "order_events.parquet" and "orders.parquet" files timestamps format were not supported by Synapse. I converted it using a python script.
