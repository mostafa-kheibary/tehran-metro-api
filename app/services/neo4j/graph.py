import os
from neo4j import GraphDatabase
from dotenv import load_dotenv


class GraphDB():
    def __init__(self):
        load_dotenv()
        URI = os.getenv('NEO4J_URI')
        USERNAME = os.getenv('NEO4J_USERNAME')
        PASSWORD = os.getenv('NEO4J_PASSWORD')

        if not URI or not USERNAME or not PASSWORD:
            raise Exception("Include .env with the esential database creadentials")

        self.URI = URI
        self.username = USERNAME
        self.password = PASSWORD
    def connect(self):
        with GraphDatabase.driver(self.URI, auth=(self.username, self.password)) as driver:
            driver.verify_connectivity()
            self.driver = driver


db = GraphDB()
db.connect()
