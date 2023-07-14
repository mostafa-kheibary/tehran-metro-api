from fastapi import APIRouter, HTTPException
from app.services.neo4j.transactions import getAllStations,getStationWithLine,searchStation
from app.services.neo4j.graph import db

router = APIRouter(prefix="/stations", tags=["stations"])


@router.get('/')
async def get_all_stations():
    with db.driver.session() as session:
        try:
            return session.read_transaction(getAllStations.transaction)
        except Exception as err:
            return {"message":str(err)}


@router.get("/{line}")
async def get_station_with_line_number(line: int):
    if (line < 1 or line > 7):
        raise HTTPException(
            status_code=402, detail="Line number should be in range of 1,7")

    with db.driver.session() as session:
        try:
            result = session.read_transaction(getStationWithLine.transaction,line)
            return result
        except Exception as err:
            return {"message":str(err)}
        

@router.get('/search/{station_name}')
def get_searched_station(station_name):
    with db.driver.session() as session:
        try:
            return session.read_transaction(searchStation.transaction,station_name)
        except Exception as err:
            return {"message",str(err)}