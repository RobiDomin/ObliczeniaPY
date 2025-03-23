import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Pobranie katalogu 'maszyna'
SQLITE_DB_PATH = os.path.join(BASE_DIR, "..", "data", "dane.db")  # Pełna ścieżka do bazy danych
CSV_FILE_PATH = os.path.join(BASE_DIR, "..", "data", "dane_w.csv")  # Pełna ścieżka do pliku CSV

TABLE_NAME = 'dane'
DELIMITER = ';'
ENCODING = 'utf-8'
