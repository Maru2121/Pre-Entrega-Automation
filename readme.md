# Proyecto Final — Automation Testing

### María Chiribao | QA Tester Funcional | QA Analyst | QA Automation

Framework de automatización de pruebas **End-to-End (E2E)** para la plataforma web **Swag Labs (SauceDemo)**, complementado con pruebas de integración de la API pública **ReqRes**.

El proyecto integra **Testing Funcional, E2E Testing, API Testing y Automation Testing**, junto con generación de datos dinámicos, validaciones automatizadas, evidencias de ejecución, logging y generación automática de reportes.

El objetivo es validar la consistencia funcional de los principales flujos de negocio mediante una estrategia de pruebas automatizadas basada en casos de prueba previamente definidos y criterios de validación.

---

## Propósito del Proyecto

Desarrollar un framework de automatización capaz de validar diferentes capas de una aplicación y cubrir escenarios funcionales relevantes mediante pruebas automatizadas.

La suite contempla:

- Autenticación y validación de diferentes perfiles de usuario.
- Gestión del carrito de compras.
- Inventario y productos.
- Detalle de productos.
- Ordenamiento de productos.
- Flujo completo de Checkout.
- Logout.
- Usuarios con comportamientos especiales.
- Pruebas de integración de API.
- Generación automática de reportes.
- Consolidación de resultados en Excel.
- Logging y trazabilidad de las ejecuciones.
- Captura automática de evidencias ante fallos de UI.

El proyecto busca demostrar cómo una estrategia de **QA funcional puede evolucionar hacia un proceso automatizado**, manteniendo como eje el análisis del comportamiento esperado del sistema.

---

# Enfoque de QA

La automatización fue desarrollada a partir de una perspectiva funcional y end-to-end.

Antes de automatizar los escenarios se consideraron:

- Flujos funcionales de la aplicación.
- Reglas de negocio.
- Casos de prueba definidos.
- Datos de prueba.
- Resultados esperados.
- Escenarios positivos y negativos.
- Diferentes perfiles de usuario.
- Validaciones de interfaz.
- Validaciones de navegación.
- Validaciones de datos.
- Integración con servicios API.
- Evidencias necesarias para la trazabilidad.

La automatización se utilizó como mecanismo para aumentar la repetibilidad, cobertura y trazabilidad de las pruebas, sin reemplazar el análisis funcional ni el criterio de QA.

---

# 🛠️ Tecnologías Utilizadas

| Tecnología | Utilización |
|---|---|
| **Python 3.13** | Lenguaje principal |
| **PyTest** | Framework de ejecución y organización de pruebas |
| **Pytest-HTML** | Generación de reportes HTML |
| **Selenium WebDriver** | Automatización de interfaz web |
| **Requests** | Consumo y validación de servicios API |
| **Faker** | Generación de datos dinámicos para testing |
| **Pandas** | Procesamiento y consolidación de resultados |
| **OpenPyXL** | Generación y manipulación de matrices Excel |
| **WebDriver Manager** | Gestión automática de drivers de navegador |
| **Postman** | Pruebas y validaciones de API |
| **Swagger** | Consulta y documentación de servicios API |
| **JSON** | Intercambio y procesamiento de datos |

---

# Inteligencia Artificial como herramienta de desarrollo

La **Inteligencia Artificial fue utilizada de forma transversal durante el desarrollo del proyecto como herramienta de asistencia para la implementación de la automatización**, incluyendo generación, estructuración, revisión y refactorización de código.

La IA participó en diferentes etapas del desarrollo, especialmente como asistente técnico para transformar requerimientos y escenarios de prueba en implementaciones automatizadas.

Su utilización incluyó:

- Generación y estructuración de código.
- Implementación y refactorización de componentes.
- Asistencia en la construcción de Page Objects.
- Apoyo en la creación y modificación de casos automatizados.
- Análisis y resolución de errores.
- Revisión de alternativas técnicas.
- Optimización de soluciones.
- Asistencia en la documentación.
- Apoyo en la generación de datos y escenarios.
- Consulta técnica sobre Python, PyTest, Selenium, Requests y patrones de automatización.

## Supervisión y criterio humano de QA

La utilización de IA **no reemplazó el análisis funcional ni el criterio profesional de QA**.

El proceso de automatización fue supervisado y validado considerando el conocimiento del flujo funcional de la aplicación, sus reglas de negocio, los casos de prueba definidos y los resultados esperados.

La responsabilidad sobre las decisiones de testing permaneció bajo criterio de QA, incluyendo:

- Definición de los escenarios a automatizar.
- Interpretación de los requerimientos.
- Identificación de reglas de negocio.
- Selección de casos de prueba.
- Definición de resultados esperados.
- Revisión del código generado o asistido por IA.
- Verificación de locators e interacciones.
- Revisión de assertions.
- Análisis de errores.
- Ejecución de la suite.
- Validación de resultados.
- Revisión de evidencias.
- Evaluación de cobertura.
- Corrección y refactorización.
- Validación final del comportamiento esperado.

### 🔍 Proceso de validación

El código generado o asistido mediante IA **no fue considerado válido automáticamente**.

Cada implementación fue revisada y ejecutada dentro del framework para comprobar su correspondencia con el comportamiento esperado.

```text
Análisis QA
     ↓
Definición del escenario
     ↓
IA como herramienta de asistencia
     ↓
Generación / implementación de código
     ↓
Revisión humana
     ↓
Ejecución
     ↓
Análisis de resultados
     ↓
Corrección / refactorización
     ↓
Validación QA
```

De esta manera, la IA fue utilizada como **herramienta de productividad y asistencia técnica**, mientras que el análisis funcional, el criterio de testing, la supervisión del proceso y la decisión final sobre la validez de las pruebas permanecieron bajo responsabilidad de QA.

> **La IA asistió en la implementación; el criterio de QA definió qué debía probarse, verificó cómo se implementó y determinó si el resultado era correcto.**

---

# Arquitectura del Framework

El framework utiliza una estructura modular orientada a facilitar la reutilización y el mantenimiento de los componentes.

La automatización UI utiliza el patrón:

### Page Object Model — POM

Los Page Objects encapsulan los elementos y acciones correspondientes a cada página de la aplicación.

```text
Tests
  │
  ▼
Page Objects
  │
  ▼
Selenium WebDriver
  │
  ▼
Swag Labs
```

Esta separación permite:

- Reutilización de componentes.
- Centralización de locators.
- Separación entre lógica de prueba e interacción con la UI.
- Mayor mantenibilidad.
- Mejor legibilidad de los tests.
- Facilidad para modificar elementos de la interfaz.

---

# Fixtures y configuración centralizada

El archivo `conftest.py` centraliza diferentes aspectos de la ejecución mediante fixtures y hooks de PyTest.

Entre sus responsabilidades se encuentran:

- Configuración de navegadores.
- Inicialización del WebDriver.
- Cierre del WebDriver.
- Selección de navegador mediante `--browser`.
- Login reutilizable.
- Creación de directorios de reportes.
- Creación de directorios de screenshots.
- Configuración del reporte HTML.
- Registro de resultados.
- Captura automática de screenshots ante fallos.
- Generación final de la matriz Excel.

### 🌐 Navegadores soportados

```text
Chrome
Edge
Firefox
```

Ejemplos:

```bash
pytest --browser=chrome
pytest --browser=edge
pytest --browser=firefox
```

---

# 📸 Evidencias y Hooks de PyTest

Se implementó el hook:

```python
pytest_runtest_makereport
```

para interceptar el resultado de cada prueba.

Cuando una prueba de UI falla, el framework:

```text
Test FAILED
     ↓
Registro del resultado
     ↓
Captura automática de screenshot
     ↓
Almacenamiento de evidencia
```

Los resultados son posteriormente consolidados mediante:

```python
pytest_sessionfinish
```

que dispara la generación del reporte Excel al finalizar la ejecución.

---

# 📂 Estructura del Proyecto

```text
Entrega-Final-Automation/
│
├── data/
│   └── users.py
│
├── documentation/
│   ├── TestCases_SauceDemo.xlsx
│   ├── BUG_REPORT_TEMPLATE.md
│   ├── POSTMAN_ASSERTIONS.md
│   ├── POSTMAN_COLLECTION_GUIDE.md
│   ├── QA-STRATEGY.md
│   ├── QA_TEST_PLAN.md
│   ├── TESTING_METHODOLOGY.md
│   └── TEST_EXECUTION.md
│
├── evidence-entrega-final/
│   ├── report_20260704_003251.html
│   └── results_20260704_003703.xlsx
│
├── evidence-pre-entrega-clase8/
│   ├── Pre-Entrega-Automation_20260512_213614.html
│   ├── ejecucion de todos los tests.png
│   └── report_20260513_003552.html
│
├── logs/
│   └── automation.log
│
├── pages/
│   ├── cart_page.py
│   ├── checkout_information_page.py
│   ├── checkout_overview_page.py
│   ├── checkout_page.py
│   ├── complete_page.py
│   ├── inventory_page.py
│   └── login_page.py
│
├── reports/
│   ├── reportes HTML
│   └── matrices XLSX
│
├── screenshots/
│   └── evidencias de ejecución
│
├── test/
│   ├── api/
│   │   ├── test_delete_user.py
│   │   ├── test_get_users.py
│   │   └── test_post_user.py
│   │
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_inventory.py
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_product_detail.py
│   ├── test_sorting.py
│   └── test_special_users.py
│
├── utils/
│   ├── csv_reader.py
│   ├── excel_reporter.py
│   ├── faker_data.py
│   ├── json_reader.py
│   ├── logger.py
│   └── screenshot.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Cobertura de UI — Swag Labs

La suite de pruebas UI contempla diferentes funcionalidades y perfiles de usuario.

## 🔐 Login

Se implementó parametrización de usuarios mediante una fuente externa de datos:

```text
data/users.py
```

La suite contempla diferentes comportamientos:

- `standard_user`
- `locked_out_user`
- `problem_user`
- `performance_glitch_user`
- `error_user`
- `visual_user`

Se incluye tanto un escenario negativo como escenarios de acceso exitoso.

---

## Inventory

Las validaciones incluyen:

- Título de la aplicación.
- URL esperada.
- Cantidad de productos visibles.
- Elementos principales de la interfaz.
- Menú.
- Filtro de productos.
- Footer.
- Redes sociales.
- Imágenes de productos.
- Detalle de producto.

---

## 🛒 Carrito

Se automatizaron escenarios relacionados con:

- Agregado de productos.
- Visualización del carrito.
- Navegación al carrito.
- Gestión de productos.

---

## 🔄 Sorting

Se validan diferentes criterios de ordenamiento:

- A → Z.
- Z → A.
- Precio menor → mayor.
- Precio mayor → menor.

Las validaciones comparan los resultados obtenidos en la interfaz con los valores esperados mediante operaciones de ordenamiento.

---

## Checkout End-to-End

Se automatizó un flujo completo desde el inventario hasta la confirmación de compra.

```text
Login
  ↓
Inventory
  ↓
Agregar producto
  ↓
Cart
  ↓
Checkout Information
  ↓
Datos dinámicos con Faker
  ↓
Checkout Overview
  ↓
Finalizar compra
  ↓
Complete
  ↓
Validación del mensaje de éxito
```

El flujo valida el resultado final mediante:

```text
"Thank you for your order!"
```

---

## Logout

Se valida el cierre de sesión mediante:

- Apertura del menú.
- Selección de Logout.
- Verificación de retorno a la pantalla de Login.

---

# 👤 Usuarios especiales

Se automatizaron escenarios para diferentes perfiles disponibles en Swag Labs:

| Usuario | Escenario |
|---|---|
| `standard_user` | Login exitoso |
| `locked_out_user` | Login bloqueado |
| `problem_user` | Comportamiento especial |
| `performance_glitch_user` | Comportamiento con demora |
| `error_user` | Comportamiento especial |
| `visual_user` | Validación visual / funcional |

---

# 🔌 API Testing

El proyecto incorpora pruebas automatizadas de integración utilizando:

```text
Python
Requests
PyTest
```

La suite contempla:

- `GET` — consulta de usuarios.
- `POST` — creación de usuario.
- `DELETE` — eliminación de usuario.

### Casos implementados

```text
API-001 → GET Users
API-002 → POST User
API-003 → DELETE User
```

Las pruebas incluyen manejo controlado de excepciones y validación de códigos de respuesta esperados dentro del contexto de una API pública utilizada como entorno de práctica.

---

# 📮 Postman

También se desarrollaron validaciones mediante Postman para complementar las pruebas automatizadas de API.

Entre las validaciones se incluyen:

- Código de estado.
- Estructura de respuesta JSON.
- Existencia de propiedades esperadas.
- Validación de datos de respuesta.

Ejemplo:

```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
```

Validación estructural:

```javascript
pm.test("Estructura de usuario correcta", function () {
    var jsonData = pm.response.json();

    pm.expect(jsonData.data).to.be.an('array');
    pm.expect(jsonData.data[0]).to.have.property('id');
    pm.expect(jsonData.data[0]).to.have.property('email');
});
```

---

# Data-Driven Testing

El proyecto utiliza diferentes fuentes y mecanismos para gestionar datos de prueba.

### Usuarios

Los usuarios de login se encuentran centralizados en:

```text
data/users.py
```

y son utilizados mediante parametrización de PyTest.

```python
@pytest.mark.parametrize("usuario, password", lista_usuarios)
```

### Datos dinámicos

El flujo de Checkout utiliza `Faker` para generar información dinámica:

```text
Nombre
Apellido
Código postal
```

Esto permite evitar depender exclusivamente de datos estáticos y facilita la reutilización de los escenarios.

---

# Reportería

El framework genera diferentes tipos de evidencias y reportes.

### Reporte HTML

Se genera mediante:

```text
pytest-html
```

y contiene información visual de la ejecución.

Ejemplo:

```text
reports/report_YYYYMMDD_HHMMSS.html
```

### Matriz Excel

Los resultados de las pruebas se consolidan mediante:

```text
Pandas
OpenPyXL
excel_reporter.py
```

El resultado contiene información relacionada con:

- Test Case.
- Estado.
- Errores.
- Resultados de ejecución.

### Logs

La trazabilidad técnica de la ejecución se registra mediante:

```text
logs/automation.log
```

### Screenshots

Ante determinados fallos de UI se generan capturas automáticas:

```text
screenshots/
```

---

# 📈 Resultado de la Ejecución

La última ejecución global registrada obtuvo:

```text
29 PASSED
Tiempo total: 256.54 segundos
```

La cobertura incluye:

### API

```text
API-001 → GET Users
API-002 → POST User
API-003 → DELETE User
```

### UI

```text
Login
Inventory
Cart
Checkout
Logout
Product Detail
Sorting
Special Users
```

---

# Documentación QA

El proyecto no se limita al código de automatización.

Se incorporó documentación orientada a diferentes etapas del proceso de QA:

```text
BUG_REPORT_TEMPLATE.md
POSTMAN_ASSERTIONS.md
POSTMAN_COLLECTION_GUIDE.md
QA-STRATEGY.md
QA_TEST_PLAN.md
TESTING_METHODOLOGY.md
TEST_EXECUTION.md
```

Además se incluye la matriz:

```text
TestCases_SauceDemo.xlsx
```

Estos artefactos permiten relacionar:

```text
Estrategia QA
      ↓
Plan de pruebas
      ↓
Casos de prueba
      ↓
Automatización
      ↓
Ejecución
      ↓
Evidencias
      ↓
Resultados
```

---

# Metodología de Testing

El proyecto aplica conceptos de:

- Testing Funcional.
- Testing Exploratorio.
- End-to-End Testing.
- API Testing.
- Regression Testing.
- Data-Driven Testing.
- Automatización UI.
- Automatización API.
- Validación de reglas de negocio.
- Validación de resultados esperados.
- Gestión de evidencias.
- Trazabilidad de ejecución.

La automatización se integra dentro de una estrategia de QA más amplia, en lugar de considerarse únicamente como ejecución de scripts.

---

# ⚙️ Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/mariachiribao/Entrega-Final-Automation.git
```

Ingresar al proyecto:

```bash
cd Entrega-Final-Automation
```

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución

## Ejecutar toda la suite

```bash
pytest
```

La configuración de `conftest.py` genera automáticamente los reportes correspondientes.

---

## Ejecutar con Chrome

```bash
pytest --browser=chrome
```

## Ejecutar con Edge

```bash
pytest --browser=edge
```

## Ejecutar con Firefox

```bash
pytest --browser=firefox
```

---

## Ejecutar solamente las pruebas de API

```bash
pytest test/api/
```

---

# Configuración de PyTest

El proyecto utiliza:

```text
pytest.ini
```

con configuración para:

- Descubrimiento automático de tests.
- Convención `test_*.py`.
- Convención `test_*`.
- Ejecución detallada mediante `-v`.
- Marcadores personalizados para identificar Test Cases.

Ejemplo:

```python
@pytest.mark.tc("TC-009")
```

Esto permite relacionar los tests automatizados con los casos de prueba documentados.

---

# Evidencias

El repositorio conserva evidencias de diferentes etapas del proyecto:

```text
evidence-pre-entrega-clase8/
evidence-entrega-final/
reports/
screenshots/
logs/
```

Esto permite mantener trazabilidad histórica de las ejecuciones y entregas realizadas durante el desarrollo.

---

# Objetivos de Aprendizaje

Este proyecto permitió consolidar conocimientos en:

- Python aplicado a QA.
- PyTest.
- Selenium WebDriver.
- Page Object Model.
- Fixtures.
- Hooks de PyTest.
- Parametrización.
- Data-Driven Testing.
- Faker.
- API Testing.
- Requests.
- Postman.
- JSON.
- Validación de respuestas.
- Generación de reportes.
- Logging.
- Captura automática de evidencias.
- Procesamiento de resultados con Pandas.
- Generación de matrices Excel.
- Organización profesional de un framework de automatización.
- Uso de Inteligencia Artificial como herramienta de asistencia técnica bajo supervisión de QA.

---

# QA Mindset

> **Automatizar no significa solamente escribir código.**
>
> Significa comprender qué debe validarse, por qué debe validarse, cuáles son los resultados esperados y cómo determinar si el sistema cumple con ellos.
>
> La automatización es una herramienta para aumentar la cobertura, repetibilidad y trazabilidad del proceso de QA.

---

# 🤖 AI-Assisted QA Automation

Este proyecto representa además una experiencia práctica en la integración de **Inteligencia Artificial dentro de un proceso profesional de QA Automation**.

La experiencia permitió explorar un modelo de trabajo en el que:

```text
Conocimiento funcional
        +
Criterio QA
        +
Inteligencia Artificial
        +
Automatización
        +
Validación humana
        ↓
Framework de Automation Testing
```

La IA fue utilizada como asistente técnico, pero las decisiones relacionadas con el comportamiento esperado del sistema, los escenarios de prueba, la cobertura, la validación y la aceptación de los resultados fueron supervisadas desde una perspectiva de QA.

> **La tecnología puede asistir en la construcción. El criterio de QA determina qué debe construirse y cómo comprobar que funciona.**

---

# Autora

## María Chiribao

**QA Tester Funcional | QA Analyst | E2E Testing | API Testing | QA Automation**

Proyecto desarrollado con fines académicos y de práctica profesional en **QA Automation**, integrando Testing Funcional, End-to-End Testing, API Testing, automatización y uso supervisado de Inteligencia Artificial como herramienta de asistencia técnica.

---

**Gracias por visitar el proyecto.**
---
