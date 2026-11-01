import dlt

@dlt.table
def bronze():
  return spark.range(10)