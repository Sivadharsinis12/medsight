import logging

logger = logging.getLogger(__name__)

# Try to load models, but allow fallback
nlp = None
classifier = None

try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    logger.info("spaCy model loaded successfully")
except Exception as e:
    logger.warning(f"Could not load SpaCy model: {e}")

try:
    from transformers import pipeline
    classifier = pipeline("text-classification", model="distilbert-base-uncased")
    logger.info("Transformers classifier loaded successfully")
except Exception as e:
    logger.warning(f"Could not load transformers model: {e}")

def analyze_text(text: str):
    entities = []
    classification = []
    
    # Use spaCy if available
    if nlp:
        try:
            doc = nlp(text)
            entities = [(ent.text, ent.label_) for ent in doc.ents]
        except Exception as e:
            logger.warning(f"spaCy processing failed: {e}")
    
    # Use transformer classifier if available
    if classifier:
        try:
            classification = classifier(text[:512])
        except Exception as e:
            logger.warning(f"Transformer classification failed: {e}")
    
    # If no models available, return basic analysis
    if not entities and not classification:
        # Simple keyword-based fallback
        text_lower = text.lower()
        if "radiology" in text_lower or "imaging" in text_lower:
            classification = [{"label": "CLINICAL", "score": 0.9}]
        elif "lab" in text_lower or "blood" in text_lower:
            classification = [{"label": "LAB_REPORT", "score": 0.9}]
        else:
            classification = [{"label": "GENERAL", "score": 0.8}]
        
        # Extract simple entities
        if "patient" in text_lower:
            entities = [("patient", "PERSON")]
    
    return {
        "entities": entities,
        "classification": classification
    }
