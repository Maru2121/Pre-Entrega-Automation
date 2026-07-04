# Guía de la Colección de Postman

## 1. Propósito
Este documento describe el orden secuencial y los alcances lógicos aplicados para validar las peticiones a la API Rest de ReqRes de forma manual o automatizada fuera del ecosistema Selenium.

## 2. Estructura de la Colección
* **Carpeta Usuarios:** Contiene flujos de consulta masiva y paginación de datos.
* **Carpeta Mutaciones:** Agrupa los métodos de alteración de estado (Inserciones con `POST` y borrados lógicos mediante `DELETE`).

## 3. Variables de Entorno (Environment Variables)
* `base_url`: `https://reqres.in/api`
* `user_id`: ID dinámico devuelto en las respuestas para encadenamiento de peticiones.