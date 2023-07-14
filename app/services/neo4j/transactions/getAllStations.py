from neo4j import ManagedTransaction
GET_ALL_STATIONS_QUERY = """
  MATCH (n:Station) RETURN collect(n) AS stations
"""

def transaction(tx:ManagedTransaction):
  result = tx.run(GET_ALL_STATIONS_QUERY)
  data = result.single() or []
  return data[0]