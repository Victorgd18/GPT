from guardar import guardar_string_en_archivo, guardar_respuesta_en_archivo_apend
import openai
openai.api_key = "API"

# para modelo Chat
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Hablas en español, eres un experto narrador de cuentos con coherencia y mucha creatividad."},
    {"role": "user", "content": "Genera un cuento sobre un robot donde al final muere. El final tiene que ser un final que segun la sociedad sea visto como triste, o tragico, o malo. No generes un cuento con final feliz."}
  ]
)

# Lee el contenido del archivo con codigo
with open("archivo.txt", "r") as archivo:
    codigo = archivo.read()

#Para modelo instruct
response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt=f'Habla en español. Eres un experto programador, generador de codigo y altamente capacitado para solucionar problemas de desarrollo de software web. Modifica el siguiente codigo para que tenga otro input más y pueda ingresar en ese input el idioma. El codigo que tienes que modificar es:\n\n```\n{codigo}\n```\n\n',
  max_tokens=2048,
  temperature=0.8
)



# print(completion.choices[0].message)
# print(response.choices[0].text)
nombre_archivo = "respuestas.txt"
guardar_respuesta_en_archivo_apend(response.choices[0].text, nombre_archivo)