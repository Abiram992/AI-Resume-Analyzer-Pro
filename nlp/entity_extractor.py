import spacy


# LOAD MODEL
nlp = spacy.load(
    "en_core_web_sm"
)


# =========================
# ENTITY EXTRACTION
# =========================
def extract_entities(text):

    doc = nlp(text)

    entities = []

    for ent in doc.ents:

        entities.append({
            "text": ent.text,
            "label": ent.label_
        })

    return entities