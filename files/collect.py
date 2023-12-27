from pyspark.sql import SparkSession

# Create a SparkSession
spark = (
    SparkSession.builder.appName("CollectExample")
    .master("spark://141.98.210.151:7077")
    .getOrCreate()
)

# Create a DataFrame
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Show the DataFrame content
df.show()

# Collect all the data from the DataFrame
collected_data = df.collect()

# Print the collected data (This is feasible for small datasets)
for row in collected_data:
    print(row)

# Stop the SparkSession
spark.stop()
