import os
from google import genai
from dotenv import load_dotenv

# Carga de variables de entorno desde el archivo .env
load_dotenv()

clave_api = os.getenv("GEMINI_API_KEY")

if not clave_api or clave_api == "PEGA_AQUI_TU_API_KEY":
    raise ValueError("No se encontro GEMINI_API_KEY. Agrega tu clave real en el archivo .env")

# Inicializa el cliente de Gemini con la clave API
cliente = genai.Client(api_key=clave_api)

def ejecutar_consulta():
    consulta = input("Escribe tu consulta para Gemini: ")

    if not consulta.strip():
        print("No escribiste ninguna consulta.")
        return

    print("Ejecutando consulta a Gemini...")

    try:
        respuesta = cliente.models.generate_content(
            model="gemini-flash-latest",
            contents=consulta
        )
        print("Respuesta de Gemini:")
        print(respuesta.text)

    except Exception as e:
        print("Error al ejecutar la consulta:", e)

if __name__ == "__main__":
    ejecutar_consulta()
