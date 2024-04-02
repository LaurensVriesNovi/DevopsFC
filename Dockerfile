# Gebruik de officiële Python beeld
FROM python:3.12-slim

# Stel de werkdirectory in
WORKDIR /app

# Kopieer het huidige directory inhoud naar de container op /app
COPY . /app

COPY requirements.txt .
# Installeer de benodigde Python-pakketten
RUN pip install -r requirements.txt

# Start de FastAPI-applicaties
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
