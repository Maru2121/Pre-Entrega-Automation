Colección de Validaciones y Snippets de API (Postman Assertions)
A continuación se detallan los códigos de control aplicados en la sección de "Tests" de Postman para asegurar la consistencia del backend:

1. Validación de Código de Estado (Status 200 OK)
pm.test("Status code is 200 OK", function () {
pm.response.to.have.status(200);
});

2. Validación de Contrato JSON Estructurado
pm.test("Estructura de usuario correcta", function () {
var jsonData = pm.response.json();
pm.expect(jsonData.data).to.be.an('array');
pm.expect(jsonData.data[0]).to.have.property('id');
pm.expect(jsonData.data[0]).to.have.property('email');
});

3. Validación de Códigos de Creación Éxito (Status 201 Created)
pm.test("Recurso creado exitosamente", function () {
pm.response.to.have.status(201);
});

4. Validación de Tiempo de Respuesta (Performance)
pm.test("El tiempo de respuesta es menor a 500ms", function () {
pm.expect(pm.response.responseTime).to.be.below(500);
});
