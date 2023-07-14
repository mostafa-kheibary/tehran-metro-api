# Metro Navigation App: Setup and Installation Guide

##### This project use the [metro-graph-data](https://github.com/mostafa-kheibary/tehran-metro-graph) repository for the metro stations data

##

##

##

Metro-App is a Python-based project that uses the FastAPI framework.and it used for :

- Find the shortest time to trvel from on station to another
- FullText search across the tehran metro stations
- and other metro related api's

The guide will provide instructions on how to setup and run the Metro-App project. Please follow each step closely to ensure the successful setup of the project.

## Prerequisites

You can run this project as Docker container with

```bash
docker-compose up --build
```

or just run it localy:
Before getting started, make sure you have the following software installed on your system:

- Python 3.7 or later
- Neo4j Database

### Step 1: Install Neo4j Database

The Metro-App project uses the Neo4j graph database. If you do not have it installed, you can download and install it from [here](https://neo4j.com/download/).

After installation, make sure the Neo4j service is running.

### Step 2: Setting Up a Virtual Environment

To keep your project's dependencies isolated from your other Python projects, it is good practice to use a virtual environment.

To create a virtual environment for this project, navigate to the project directory in your terminal and run the following command:

```bash
python -m venv env
```

### Step 3: Setting Up Environment Variables

Next, create a `.env` file in the root directory of the project. This file will hold all the necessary environment variables. Add the following content to the `.env` file:

```
NEO4J_URI="neo4j://localhost:7687"
NEO4J_USERNAME="neo4j"
NEO4J_PASSWORD="neo4j"
```

Please replace `"neo4j"` in `NEO4J_USERNAME` and `NEO4J_PASSWORD` with your actual Neo4j username and password.

### Step 4: Install Required Python Packages

First, activate the virtual environment you created:

For Linux or macOS:

```bash
source env/bin/activate
```

For Windows:

```bash
.\env\Scripts\activate
```

Then install the necessary Python packages for the project by running:

```bash
pip install -r requirements.txt
```

### Step 5: Migrate the Database

After setting up the database and environment, you need to migrate your data. Run the following command:

```bash
python3 app/services/neo4j/migrate.py
```

### Step 6: Run the Project

Finally, you can run the project using the following command:

```bash
python3 main.py
```

After this step, your application should be running, and you can access it through your web browser.

Please feel free to reach out if you encounter any problems during the setup process. Happy coding!

### Step 7: Navigate to

```bash
http://localhost:8000/docs
```
