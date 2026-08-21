import re
import easyocr
import numpy as np
from pdf2image import convert_from_path
from PIL import Image

# Correctif de compatibilité pour Pillow 10+
if not hasattr(Image, 'ANTIALIAS'):
    Image.ANTIALIAS = Image.Resampling.LANCZOS

# Initialisation globale du lecteur EasyOCR (français et anglais, sans GPU par défaut)
reader = easyocr.Reader(['fr', 'en'], gpu=False)

def process_pdf(file_path: str):
    """Extrait le texte et structure les données exclusivement de la page 2 d'un PDF."""
    texte_page_2 = ""
    try:
        # On force la lecture unique de la page 2 avec une résolution optimale (dpi=300)
        pages = convert_from_path(file_path, dpi=300, first_page=2, last_page=2)
        
        if pages:
            image_np = np.array(pages[0])
            resultats = reader.readtext(image_np, detail=0)
            texte_page_2 = " ".join(resultats)
            
    except Exception as e:
        return {"error": str(e)}

    # Nettoyage des espaces
    texte_propre = re.sub(r'\s+', ' ', texte_page_2).strip()
    
    patterns = {
        "lieu_dit": r"Lieu-dit(.*?)Echelle",
        "province": r"Province(.*?)=Parcelle",
        "commune": r"par le requérant Commune(.*?)(?:N' Dossier)",
        "parcelle": r"Visa du CDD Section N' BX Parcelle N'(.*?)Requérant",
        "section": r"Visa du CDD Section N'(.*?)Parcelle",
        "requerant": r"Requérant(.*?)(?:Lieu-dit)",
        "reference": r"Dossier(.*?)(?:Visa)"
    }
    
    data = {cle: "Non trouvé" for cle in patterns.keys()}
    
    for cle, motif in patterns.items():
        matches = list(re.finditer(motif, texte_propre, re.IGNORECASE))
        
        # Prend la première occurrence par défaut pour tous les champs
        if matches:
            data[cle] = matches[0].group(1).strip()
            
    # On stocke uniquement le texte de la page 2
    data["texte_integral"] = texte_propre
    
    return data