import uvicorn
from dotenv import load_dotenv
from app.api.endpoints import stations, paths, lines
from fastapi.middleware.cors import CORSMiddleware
from app.services.neo4j.graph import db
from fastapi import FastAPI
import os 


def create_app():
    _app = FastAPI()
    
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(paths.router)
    _app.include_router(stations.router)
    _app.include_router(lines.router)
    return _app


# Create app
load_dotenv()
db.driver.verify_connectivity()
app = create_app()

if __name__ == '__main__':
    PORT = os.getenv("PORT")
    if not PORT:PORT = "8200"
    
    uvicorn.run("main:app", reload=True,host="0.0.0.0",port=int(PORT))
