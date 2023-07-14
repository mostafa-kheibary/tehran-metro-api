from neo4j import ManagedTransaction  

GET_LINE_INTERSECTIO_QUERY ="""
  MATCH (station:Station)
  WHERE ALL(x IN $lines WHERE x IN station.lines) AND SIZE(station.lines) = SIZE($lines)
  RETURN station
"""

def transaction(tx:ManagedTransaction,lines):
  result = tx.run(GET_LINE_INTERSECTIO_QUERY,{"lines":lines})
  data = result.single()
  if not data:
    raise Exception("No stations found with these line intersect")
  return data