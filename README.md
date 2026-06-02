# Automatizare QA cu Playwright

## Descriere

Acest proiect este un framework simplu de automatizare QA construit cu Python, Playwright si Pytest.  
Acopera scenarii de testare UI web folosind Page Object Model (POM).

---

## Tipuri de teste

Proiectul contine 5 tipuri principale de teste:

- Form - completarea formularelor web
- Checkbox-uri - selectarea optiunilor
- Date Picker - selectarea datelor din calendar
- Switch Window - gestionarea tab-urilor noi si a alertelor
- Buttons - interactiuni simple UI (click, hover)

---

## Tehnologii folosite

- Python
- Playwright
- Pytest

---

## Structura proiectului

- Branch Master

Base Version

- Branch Ai Pom Upgrade

Proiectul refactorizat in POM cu Integrare AI pt Forms si Checkboxes

---

## Cum rulam proiectul

### Instalare dependinte

pip install pytest playwright  
python -m playwright install

---

### Rulare teste

Rulare toate testele  
python -m pytest

Rulare cu log-uri (debug)  
python -m pytest -s

Rulare folder tests  
python -m pytest tests

Rulare un singur test  
python -m pytest tests/test_form.py

---

## Scopul proiectului

Acest proiect este creat pentru invatare si practica in QA automation:

- automatizare UI cu Playwright
- structura Page Object Model (POM)
- organizarea testelor cu Pytest