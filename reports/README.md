# Proyecto de Automatización QA - Maria Chiribao

---

## Descripción

Proyecto de automatización de pruebas funcionales desarrollado con Python, Selenium WebDriver y Pytest.

El framework automatiza distintos escenarios de prueba sobre la aplicación SauceDemo utilizando buenas prácticas de automatización QA, estructura modular y generación automática de reportes.

---

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Pandas
- OpenPyXL
- WebDriver Manager
- Git

---

## Funcionalidades implementadas

- Ejecución automatizada de pruebas funcionales
- Soporte multi-browser:
  - Chrome
  - Edge
  - Firefox
- Login reutilizable mediante fixtures
- Captura automática de screenshots en fallos
- Generación automática de:
  - Reporte HTML
  - Reporte Excel
- Integración de Test Case IDs
- Organización modular del framework
- Manejo automático de drivers

---

## Instalación

### Clonar repositorio

```bash
git clone https://github.com/Maru2121/Pre-Entrega-Automation.git

Estructura del proyecto

```text
project/
│
├── documentation/
│   └── TestCases_SauceDemo.xlsx
│
├── reports/
│   ├── report.html
│   └── results.xlsx
│
├── screenshots/
│
├── test/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_sorting.py
│   ├── test_logout.py
│   ├── test_product_detail.py
│   └── test_special_users.py
│
├── utils/
│   ├── LoginPage.py
│   └── excel_reporter.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

---

Ingresar al proyecto
cd Pre-Entrega-Automation
---

## Instalar dependencias
- pip install -r requirements.txt
- Ejecución de pruebas
- Ejecutar toda la suite
- py -m pytest

---

## Ejecutar en navegador específico
- py -m pytest --browser=chrome
  py -m pytest --browser=edge
- py -m pytest --browser=firefox

---

##  Reportes automáticos

Al finalizar la ejecución se generan automáticamente:

- Reporte HTML → reports/
- Reporte Excel → reports/results_fecha.xlsx
- Screenshots de fallos → screenshots/

---

## Buenas prácticas implementadas

- Uso de fixtures reutilizables
- Separación de responsabilidades
- Automatización desacoplada
- Reportes automáticos
- Multi-browser support
- Código modular y escalable

---

Autor

Maria Chiribao

---

## Proyecto desarrollado con fines educativos y de práctica profesional QA Automation.
