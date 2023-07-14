from fastapi import APIRouter
from pydantic import BaseModel
from app.services.neo4j.transactions import getLineWithStationName,getLineIntersection

from app.services.neo4j.graph import db
from typing import List


router = APIRouter(prefix="/line", tags=["lines"])

@router.get('/{stationName}')
def get_line_from_station_name(stationName: str):
    with db.driver.session() as session:
        try:
          result = session.read_transaction(getLineWithStationName.transaction, stationName)
          return result
        except Exception as err:
          return {"message":str(err)}

class Body(BaseModel):
    lines: List[int]

@router.post('/intersection')
def get_line_intersection(items: Body):
    with db.driver.session() as session:
      try:
        result = session.read_transaction(getLineIntersection.transaction,items.lines)
        return result
      except Exception as err:
        return {"message":str(err)}
