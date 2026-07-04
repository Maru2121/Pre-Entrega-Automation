### 4. `TESTING_METHODOLOGY.md`
Explica las buenas prácticas y patrones de diseño utilizados en tu código.

```markdown
# Metodología de Testing Aplicada

## 1. Page Object Model (POM)
Para asegurar que los scripts de prueba sean mantenibles, se separó por completo la lógica de interacción física del navegador de las validaciones lógicas de negocio.
* Cada interfaz de Swag Labs se modeló como una clase dedicada en la carpeta `pages/` (ej: `CartPage`, `CheckoutOverviewPage`).
* Si un elemento cambia su ID en la web, solo se actualiza una única línea en el Page Object sin romper los casos de prueba funcionales.

## 2. Independencia y Aislamiento (Isolation)
Las pruebas son completamente agnósticas e independientes. La ejecución o falla de un caso de prueba individual no altera ni bloquea la continuidad ni los datos de los demás scripts.

## 3. Data-Driven Testing
Se implementó testing basado en datos mediante la anotación `@pytest.mark.parametrize`, inyectando múltiples perfiles de usuario desde fuentes de configuración dedicadas (`data/users.py`) de forma externa.