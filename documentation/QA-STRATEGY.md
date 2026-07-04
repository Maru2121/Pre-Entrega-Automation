# Estrategia de Control de Calidad (QA Strategy)

## 1. Alcance del Proyecto
Esta estrategia define el enfoque de pruebas para la plataforma **Swag Labs** (Pruebas de Interfaz de Usuario) y la API pública **ReqRes** (Pruebas de Integración/API).

## 2. Tipos de Pruebas Ejecutadas
* **Pruebas Funcionales (UI):** Validación de flujos críticos de extremo a extremo (E2E) bajo el patrón Page Object Model (POM).
* **Pruebas de Regresión de API:** Verificación de consistencia y contratos de endpoints mediante métodos HTTP (GET, POST, DELETE).
* **Pruebas de Datos:** Validación de combinaciones de credenciales mediante testing parametrizado.

## 3. Criterios de Aceptación Globales
* El 100% de los casos críticos de negocio (Login, Carrito, Compra exitosa) deben ejecutarse sin errores fatales.
* Todo test fallido en la interfaz web debe capturar una evidencia fotográfica adjunta al reporte dinámico de Pytest de manera automatizada.