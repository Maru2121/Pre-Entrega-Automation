# Proyecto Final de Automation Testing - Maria Chiribao

## Propósito del Proyecto
Framework de automatización de pruebas End-to-End (E2E) para la plataforma **Swag Labs (UI)** y pruebas de regresión e integración para la API pública **ReqRes (Backend)**. El objetivo de este ecosistema es garantizar la consistencia funcional de los flujos de negocio mediante aserciones robustas, inyección de datos dinámicos y generación automática de reportes de auditoría.

---

## Tecnologías Utilizadas
* **Python 3.13** (Lenguaje principal)
* **Pytest** & **Pytest HTML** (Framework de pruebas y reportes visuales)
* **Selenium WebDriver** (Automatización de interfaz de usuario)
* **Requests** (Validación e integración de servicios API)
* **Faker** (Generación de datos aleatorios para testing funcional)
* **Pandas** & **OpenPyXL** (Consolidación de matrices de datos en Excel)

---

## Estructura del Proyecto
```text
Entrega-Final-Automation/
│
├── documentation/
│   ├── TestCases_SauceDemo.xlsx
│   └── TESTING_METHODOLOGY.md
│
├── logs/
│   └── automation.log          # Historial de trazabilidad y ejecución paso a paso
│
├── pages/                      # Clases bajo el patrón Page Object Model (POM)
│   ├── LoginPage.py
│   └── [Componentes de la UI]...
│
├── reports/                    # Reportes generados automáticamente
│   ├── report_*.html           # Reporte interactivo con marcas de tiempo
│   └── results_*.xlsx          # Matriz de cobertura de Test Cases
│
├── screenshots/                # Capturas automáticas en caso de fallas de UI
│
├── test/
│   ├── api/                    # Pruebas automatizadas del Backend (ReqRes)
│   │   ├── test_delete_user.py
│   │   ├── test_get_users.py
│   │   └── test_post_user.py
│   ├── test_cart.py            # Pruebas funcionales de UI (Flujos de Carrito)
│   ├── test_checkout.py
│   ├── test_inventory.py
│   ├── test_login.py           # Login parametrizado multi-usuario
│   ├── test_logout.py
│   ├── test_product_detail.py
│   └── test_special_users.py
│
├── utils/                      # Herramientas de soporte y reportería externa
│   └── excel_reporter.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Colección de Validaciones y Snippets de API (Postman Assertions)
Detalle de los scripts de control aplicados en la sección de "Tests" de Postman para asegurar los contratos del backend:

### 1. Validación de Código de Estado (Status 200 OK)
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
```

### 2. Validación de Contrato JSON Estructurado
```javascript
pm.test("Estructura de usuario correcta", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.data).to.be.an('array');
    pm.expect(jsonData.data[0]).to.have.property('id');
    pm.expect(jsonData.data[0]).to.have.property('email');
});
```

---

## Cobertura de la Suite de Pruebas (Pytest Execution Summary)
La última ejecución global arrojó un resultado de **`29 passed in 256.54s`**, distribuidos de la siguiente manera:

| Archivo / Módulo | Caso de Prueba (TC) | Capa | Estado |
| :--- | :--- | :--- | :--- |
| `test/api/test_delete_user.py` | `test_delete_user` (API-003) | API | **PASSED** |
| `test/api/test_get_users.py` | `test_get_users_list` (API-001) | API | **PASSED** |
| `test/api/test_post_user.py` | `test_create_user` (API-002) | API | **PASSED** |
| `test/test_cart.py` | `test_add_product_cart` | UI | **PASSED** |
| `test/test_cart.py` | `test_view_cart` | UI | **PASSED** |
| `test/test_cart.py` | `test_remove_product` | UI | **PASSED** |
| `test/test_checkout.py` | `test_checkout_complete` | UI | **PASSED** |
| `test/test_inventory.py` | `test_inventory_title` | UI | **PASSED** |
| `test/test_inventory.py` | `test_productos_visibles` | UI | **PASSED** |
| `test/test_inventory.py` | `test_ui_elements` | UI | **PASSED** |
| `test/test_inventory.py` | `test_footer_redes` | UI | **PASSED** |
| `test/test_inventory.py` | `test_imagenes_productos` | UI | **PASSED** |
| `test/test_inventory.py` | `test_detalle_producto` | UI | **PASSED** |
| `test/test_login.py` | `test_login_multiples_usuarios[standard_user]` | UI | **PASSED** |
| `test/test_login.py` | `test_login_multiples_usuarios[locked_out_user]`| UI | **PASSED** |
| `test/test_login.py` | `test_login_multiples_usuarios[problem_user]` | UI | **PASSED** |
| `test/test_login.py` | `test_login_multiples_usuarios[performance_glitch]`| UI | **PASSED** |
| `test/test_login.py` | `test_login_multiples_usuarios[error_user]` | UI | **PASSED** |
| `test/test_login.py` | `test_login_multiples_usuarios[visual_user]` | UI | **PASSED** |
| `test/test_logout.py` | `test_logout` | UI | **PASSED** |
| `test/test_product_detail.py`| `test_product_detail` | UI | **PASSED** |
| `test/test_sorting.py` | `test_sort_az` | UI | **PASSED** |
| `test/test_sorting.py` | `test_sort_za` | UI | **PASSED** |
| `test/test_sorting.py` | `test_sort_low_high` | UI | **PASSED** |
| `test/test_sorting.py` | `test_sort_high_low` | UI | **PASSED** |
| `test/test_special_users.py` | `test_performance_user` | UI | **PASSED** |
| `test/test_special_users.py` | `test_visual_user` | UI | **PASSED** |
| `test/test_special_users.py` | `test_error_user` | UI | **PASSED** |
| `test/test_special_users.py` | `test_problem_user` | UI | **PASSED** |

---

## Instalación de Dependencias

### 1. Clonar el repositorio
```bash
git clone [https://github.com/Maru2121/Entrega-Final-Automation.git](https://github.com/Maru2121/Entrega-Final-Automation.git)
cd Entrega-Final-Automation
```

### 2. Instalar requerimientos
```bash
pip install -r requirements.txt
```

---

## Ejecución de Pruebas

### Ejecutar toda la suite (UI + API) con reporte HTML embebido
```bash
pytest --html=reports/reporte_final.html --self-contained-html
```

### Ejecutar únicamente las pruebas de integración API
```bash
pytest test/api/
```

### Ejecutar pruebas de UI forzando un navegador específico
```bash
pytest --browser=chrome
pytest --browser=edge
pytest --browser=firefox
```

---

## Reportes y Evidencias Generadas
Las salidas de cada suite quedan registradas de manera automática en las siguientes rutas locales:
* 📊 **Reporte Interactivo Completo:** `reports/report_20260704_003251.html`
* 📈 **Matriz de Cobertura Comercial:** `reports/results_20260704_003703.xlsx`
* 📝 **Logs y Trazabilidad Técnica:** `logs/automation.log`

---
*Desarrollado por Maria Chiribao con fines académicos y de práctica profesional en QA Automation.*