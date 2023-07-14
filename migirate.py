import json
from app.services.neo4j.graph import db


db.driver.execute_query('MATCH (n) DETACH DELETE n;')

with open('app/data/data.json',encoding="utf-8") as f:
    stations = json.load(f)

    for key, value in stations.items():
        property = value["property"]
        # creating nodes
        query = """
        CREATE (n:Station {name:$name,fa:$fa,lines:$lines,colors:$colors,disabled:$disabled})
        """
        db.driver.execute_query(query, property)

        # creating relationships
        for rel in value["relations"]:
            query = """
          MATCH (n:Station),(n1:Station)
          WHERE n.name = $from AND n1.name = $to
          CREATE (n)-[r:Line {disabled:$disabled}]->(n1),(n1)-[r2:Line {disabled:$disabled}]->(n)
          """
            db.driver.execute_query(query, {"from": key, "to": rel["name"], "disabled": property["disabled"] and rel["disabled"]})

db.driver.execute_query("""
MATCH (s:Station)-[rl:Line]-(t:Station)
WITH s, t, rl, [value IN s.lines WHERE value IN t.lines] AS commonValues
WHERE size(commonValues) > 0
SET rl.line = commonValues[0]
""")

# full text search indexs
db.driver.execute_query("""
CREATE FULLTEXT INDEX nameAndFa FOR (n:Station) ON EACH [n.name, n.fa]
""")

db.driver.execute_query("""
CREATE INDEX FOR (n:Station) ON (n.name)
""")

print("done")