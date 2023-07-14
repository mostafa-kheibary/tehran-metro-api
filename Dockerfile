FROM python:3.8-alpine
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENV NEO4J_URI="neo4j://database:7687"
ENV NEO4J_USERNAME="neo4j"
ENV NEO4J_PASSWORD="neo4j"

EXPOSE 8200
CMD python migirate.py;python main.py