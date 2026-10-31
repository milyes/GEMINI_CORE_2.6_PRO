import zipfile
import os
import sys

ZIP_FILENAME = "GEMINI_CORE_2.6_PRO_DOCS.zip"
DOCS_DIR = "docs_temp"

HTML_CONTENT = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>FICHE TECHNIQUE OFFICIELLE GEMINI CORE 2.6 PRO</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; color: #333; }
        .container { border: 2px solid #004c99; padding: 20px; border-radius: 8px; }
        h1 { color: #004c99; }
    </style>
</head>
<body>
    <div class="container">
        <h1>GEMINI CORE 2.6 PRO — Noyau Cognitif Souverain</h1>
        <p><strong>Auteur :</strong> Zoubirou Mohammed Ilyes (ORCID: 0009-0007-7571-3178)</p>
        <p><strong>Statut :</strong> Publication Officielle (Sceau Vérifié)</p>
    </div>
</body>
</html>"""

MD_CONTENT = """# GEMINI CORE 2.6 PRO — Noyau Cognitif Souverain
- **Auteur :** Zoubirou Mohammed Ilyes
- **ORCID :** 0009-0007-7571-3178
- **Doctrine :** IA22_LOGIC (Offline-First, Zero-Trust)
"""

def main():
    print(f"[*] Génération du pack {ZIP_FILENAME}...")
    os.makedirs(DOCS_DIR, exist_ok=True)
    
    html_path = os.path.join(DOCS_DIR, "FICHE_TECHNIQUE.html")
    md_path = os.path.join(DOCS_DIR, "README.md")
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(MD_CONTENT)
        
    with zipfile.ZipFile(ZIP_FILENAME, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(html_path, arcname="FICHE_TECHNIQUE.html")
        zipf.write(md_path, arcname="README.md")
        
    os.remove(html_path)
    os.remove(md_path)
    os.rmdir(DOCS_DIR)
    print(f"[✔] Pack ZIP généré avec succès : {ZIP_FILENAME}")

if __name__ == "__main__":
    main()
