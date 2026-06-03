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

## ⚙️ Setup proiect

### 1. Clone repository

git clone https://github.com/potogoldmv/playwright-qa.git

cd playwright-qa

---

### 2. Creeaza virtual environment

python -m venv venv

---

### 3. Activeaza virtual environment

Windows PowerShell:
venv\Scripts\Activate.ps1

CMD:
venv\Scripts\activate.bat

---

### 4. Instaleaza dependintele

pip install -r requirements.txt

---

### 5. Instaleaza Playwright browsers

playwright install

---

## ▶️ Rulare teste

### Ruleaza toate testele

python -m pytest 

---

### Ruleaza testele cu output detaliat

python -m pytest -s

---

### Ruleaza un singur test

python -m pytest pytest tests/test_form.py -s

---

## 🤖 AI Integration

Unele teste folosesc OpenAI API pentru generare dinamica de date:
- nume si job titles
- date pentru formular
- valori pentru checkbox-uri

Daca AI nu functioneaza:
- verifica API key in utils/ai_data.py
- verifica conexiunea la internet
---

## Scopul proiectului

Acest proiect este creat pentru invatare si practica in QA automation:

- automatizare UI cu Playwright
- structura Page Object Model (POM)
- organizarea testelor cu Pytest
