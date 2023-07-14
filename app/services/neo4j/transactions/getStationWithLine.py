from neo4j import ManagedTransaction
GET_STATION_WITH_LINE_QUERY = """
  MATCH (station:Station)
  WHERE $line IN station.lines
  RETURN COLLECT(station)
"""

def transaction(tx:ManagedTransaction,line:int):
  result = tx.run(GET_STATION_WITH_LINE_QUERY,{"line":line})
  data = result.single()
  if not data:
    raise Exception("No station found with given line number")
  return data[0]