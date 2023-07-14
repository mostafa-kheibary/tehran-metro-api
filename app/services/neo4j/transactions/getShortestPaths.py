import re

GET_LENGTH_SHORTEST_PATH_QUERY = """
    MATCH p = shortestPath((hby:Station {name:$from,disabled:FALSE})-[:Line*]-(cnm:Station {name:$to,disabled:FALSE}))
    WHERE all(link in relationships(p) WHERE link.disabled = false)
    return length(p)
"""

GET_ALL_SHORTEST_PATH_POSSIBLE_QUERY = """
    MATCH p = (from:Station {name: $from_station, disabled: false})-[r:Line*..depth {disabled: false}]->(to:Station {name: $to_station, disabled: false})
    WHERE ALL(node IN nodes(p) WHERE single(other_node IN nodes(p) WHERE id(other_node) = id(node)))
    WITH p AS path, size([node IN nodes(p) WHERE node.disabled = false]) AS path_size
    ORDER BY path_size ASC
    WITH nodes(path) AS nodes, path_size, [rel IN relationships(path) | rel.line] AS lines
    RETURN nodes as paths, path_size, lines
    LIMIT 3
"""


def transaction(tx,from_station,to_station):
    
    # Indicate how many of more node calculate to finds the shortest paths
    CHANGES_DELTA = 3

    result = tx.run(GET_LENGTH_SHORTEST_PATH_QUERY, {"from": from_station, "to": to_station})
    data = result.single()
    if not data:
        raise Exception("No path found with this station names")

    minimumPath = data[0]
    replacedQuery = re.sub("depth",str(minimumPath+CHANGES_DELTA),GET_ALL_SHORTEST_PATH_POSSIBLE_QUERY)
    result = tx.run(replacedQuery, from_station=from_station, to_station=to_station)
    if not data:
        raise Exception("No path found with this station names")

    return result.data()



