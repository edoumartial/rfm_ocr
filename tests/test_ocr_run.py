import os
from app.services.ocr_service import ocr_service  # Ou importez votre fonction d'extraction

# Chemin vers une image de test dans votre dossier data
image_path = os.path.join("data", "fichier.pdf") # Remplacez par le nom réel d'une image

print(f"Lancement de l'OCR sur : {image_path}...")

# Simulation / Appel de votre service OCR
try:
    # Assurez-vous d'adapter selon la fonction définie dans votre ocr_service.py
    # Exemple typique avec EasyOCR :
    import easyocr
    reader = easyocr.Reader(['fr', 'en'])
    results = reader.readtext(image_path, detail=0)
    
    print("\n--- TEXTE EXTRAIT ---")
    for line in results:
        print(line)
        
except Exception as e:
    print(f"Erreur lors du test OCR : {e}")