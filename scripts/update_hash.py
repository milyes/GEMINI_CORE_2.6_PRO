import hashlib
import json
import os
import sys

ZIP_FILENAME = "GEMINI_CORE_2.6_PRO_DOCS.zip"
METADATA_FILENAME = "METADATA.json"

def calculate_sha256(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()

def main():
    if not os.path.exists(ZIP_FILENAME):
        print(f"[X] ERREUR : {ZIP_FILENAME} introuvable. Exécutez create_zip.py d'abord.")
        sys.exit(1)
        
    sha256_hash = calculate_sha256(ZIP_FILENAME)
    print(f"[*] Hash SHA256 calculé : {sha256_hash}")
    
    with open(METADATA_FILENAME, 'r') as f:
        data = json.load(f)
        
    data['traceability']['sha256_pack_zip'] = sha256_hash
    
    with open(METADATA_FILENAME, 'w') as f:
        json.dump(data, f, indent=2)
        
    print(f"[✔] METADATA.json mis à jour avec le hash réel.")

if __name__ == "__main__":
    main()
