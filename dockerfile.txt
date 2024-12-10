# Wähle ein Basis-Image
FROM python:3.9-slim

# Arbeitsverzeichnis im Container erstellen
WORKDIR /app

# Kopiere die requirements.txt und installiere Abhängigkeiten
COPY requirements.txt .
RUN pip install -r requirements.txt

# Kopiere den gesamten Rest des Projekts
COPY . .

# Exponiere den Port, den deine App verwendet
EXPOSE 8080

# Standardbefehl, um die Flask-App zu starten
CMD ["python", "app.py"]
