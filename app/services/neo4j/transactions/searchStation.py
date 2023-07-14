from neo4j import ManagedTransaction
import re
FULL_TEXT_SEARCH_QUERY = """
        MATCH (n:Station) 
        WHERE n.fa =~ '.*searched_char_token.*' OR toLower(n.name) =~ '.*searched_char_token.*' 
        RETURN collect(n)
      """

def transaction(tx:ManagedTransaction,station_name:str):
  replcaed = re.sub('searched_char_token',station_name,FULL_TEXT_SEARCH_QUERY)
  result = tx.run(replcaed) # type: ignore
  data = result.single()
  if data == None:
    raise Exception({f"message":"Noting found with {station_name}"}) 
  return data[0]