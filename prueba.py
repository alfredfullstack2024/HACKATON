import spacy

# Cargar el modelo de español
nlp = spacy.load('es_core_news_sm')


doc = nlp("Hola, esto es una prueba para verificar la instalación de spaCy.")
for token in doc:
    print(token.text, token.lemma_, token.pos_)


