from neo4j import ManagedTransaction

GET_LINE_WITH_STATION_NAME = """
  MATCH (station:Station {name:$station_name})
  RETURN station.lines AS line
"""

def transaction(tx:ManagedTransaction,name):
  result = tx.run(GET_LINE_WITH_STATION_NAME,{"station_name":name})
  data = result.data()
  if not data:
    raise Exception("There is no line associate with this station")
  return data[0]