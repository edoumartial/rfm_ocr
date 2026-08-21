import shutil
from pathlib import Path

def archiver_pdf_avec_arborescence(chemin_source_absolu: str, chemin_relatif_origine: str) -> str:
    """
    Duplique l'arborescence d'un fichier PDF source vers le dossier 'archives'
    s'il n'existe pas déjà.
    """
    dossier_destination_racine = "archives"
    destination_finale = Path(dossier_destination_racine) / chemin_relatif_origine
    
    # Création automatique de l'arborescence des sous-dossiers si elle n'existe pas
    destination_finale.parent.mkdir(parents=True, exist_ok=True)
    
    # Vérification 'if not exists'
    if not destination_finale.exists():
        shutil.copy2(chemin_source_absolu, destination_finale)
        print(f"[SUCCÈS] Copié dans l'archive : {destination_finale}")
    else:
        print(f"[INFO] Existe déjà dans les archives : {destination_finale}")
        
    return str(destination_finale)