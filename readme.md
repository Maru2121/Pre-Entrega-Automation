# Proyecto de Automatización QA - Maria Chiribao

## Descripción

Proyecto de automatización de pruebas funcionales desarrollado con Python, Selenium WebDriver y Pytest.

El framework automatiza distintos escenarios de prueba sobre la aplicación SauceDemo utilizando buenas prácticas de automatización QA, estructura modular y generación automática de reportes.

---

# Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Pandas
- OpenPyXL
- WebDriver Manager
- Git

---

# Funcionalidades implementadas

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

# Estructura del proyecto

```plaintext
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

