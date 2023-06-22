# ProjektDyplomowyNotino

Celem projektu jest przetestowanie obszaru wyszukiwania, filtrowania, sortowania, dodawania do koszyka oraz naliczania zniżek produktów dla sklepu internetowego  https://www.notino.pl/. W tym celu opracowano 5 przypadków testowych:
•	TC1: Dodanie produktów do koszyka
•	TC2: Filtrowanie produktów ze zniżką 20% oraz wprowadzanie kodu rabatowego w koszyku
•	TC3: Dodanie produktu do ulubionych
•	TC4: Wyszukanie produktu po nazwie i odświeżanie strony z wynikami wyszukiwania
•	TC5: Wyszukanie produktu po wybranej kategorii oraz sortowanie ceny według kolejności rosnącej
W niniejszej pracy zastosowano wzorzec projektowy Page Object. 
Dodatkowo, wygenerowano raport html z wykonanych testów przy użyciu platformy testowej Pytest.
  
## Instrukcja uruchamiania

1. Sklonuj repozytorium na swój lokalny komputer.
2. Przejdź do katalogu projektu.
3. Zainstaluj zależności za pomocą polecenia `npm install`.
4. Uruchom projekt za pomocą polecenia `npm start`.

## Technologie

Projekt został zrealizowany przy użyciu następujących technologii:

- Selenium WebDriver
- Unittest
- Pytest
- Page Object Pattern

