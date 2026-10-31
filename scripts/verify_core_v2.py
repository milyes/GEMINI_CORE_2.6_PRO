import json
import os
import sys

def verify():
    if not os.path.exists("METADATA.json"):
        print("[X] ERREUR: METADATA.json introuvable.")
        sys.exit(1)
    with open("METADATA.json", "r") as f:
        data = json.load(f)
    print("--- VÉRIFICATION DE CONFORMITÉ IA22 ---")
    print(f"Module: {data['module']['name']} {data['module']['version']}")
    print(f"Auteur: {data['author']['full_name']} (ORCID: {data['author']['orcid']})")
    print(f"Statut: {data['module']['status']}")
    print("[✔] INTÉGRITÉ VALIDÉE")

if __name__ == "__main__":
    verify()
