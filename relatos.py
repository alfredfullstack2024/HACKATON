from docx import Document
import spacy

# Cargar el modelo en español de spaCy
nlp = spacy.load('es_core_news_sm')

# Función para cargar los relatos desde un archivo docx
def cargar_relato_desde_docx(ruta_archivo):
    documento = Document(ruta_archivo)
    texto_completo = []
    for parrafo in documento.paragraphs:
        texto_completo.append(parrafo.text)
    return '\n'.join(texto_completo)

# Función para anonimizar un relato
def anonimizar_relato(relato):
    relato = relato.replace('San Juan', 'Localidad 1')
    relato = relato.replace('J.E.P.', 'Persona 1')
    relato = relato.replace('Pueblito', 'Localidad 2')
    relato = relato.replace('El Mirador', 'Lugar 1')
    return relato

# Función para procesar el texto con spaCy
def procesar_texto(texto):
    doc = nlp(texto)
    palabras_filtradas = [token.text for token in doc if not token.is_stop and token.is_alpha]
    return ' '.join(palabras_filtradas)

# Ruta al archivo
ruta_al_archivo = r'C:\HACKATON\Relatos.docx'
relato_cargado = cargar_relato_desde_docx(ruta_al_archivo)

# Anonimizar y procesar el texto
relato_anonimizado = anonimizar_relato(relato_cargado)
relato_procesado = procesar_texto(relato_anonimizado)

print(relato_procesado)  # Mostrar el relato procesado

