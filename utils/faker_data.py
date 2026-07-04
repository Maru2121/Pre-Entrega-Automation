from faker import Faker

# Inicializamos Faker configurado para español
fake = Faker("es_ES")

def generar_datos_checkout():
    return {
        "nombre": fake.first_name(),
        "apellido": fake.last_name(),
        "codigo_postal": fake.postcode()
    }