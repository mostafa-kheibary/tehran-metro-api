from fastapi import APIRouter
from app.utils.lineChangeLogger import line_change_logger
from app.utils.stationRanker import station_ranker
from app.services.neo4j.transactions import getShortestPaths
from app.services.neo4j.graph import db


router = APIRouter(prefix='/paths', tags=["paths"])

@router.get('/{from_station}/{to_station}')
async def find_shortest_path(from_station, to_station):

    with db.driver.session() as session:
        try:
            record = session.read_transaction(getShortestPaths.transaction,from_station,to_station)
            result = line_change_logger(station_ranker(record))
            return result
        except Exception as err:
            return {"message":str(err)}
