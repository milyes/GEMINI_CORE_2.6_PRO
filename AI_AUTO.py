#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FORGE D'AGENTS IA AUTONOMES - GEMINI CORE 2.6 PRO
Système Souverain Made in Algeria - IA22 Certified
Auteur : Zoubirou Mohammed Ilyes
ORCID : 0009-0007-7571-3178
"""

import asyncio
import json
import hashlib
from datetime import datetime
from pathlib import Path

class AgentBase:
    def __init__(self, nom: str):
        self.nom = nom
        self.statut = "initialisé"
        self.artefact = None
        self.trace = None

    async def executer(self, contexte: dict) -> dict:
        print(f"[{self.nom}] → Démarrage...")
        await asyncio.sleep(1)
        self.statut = "terminé"
        self.artefact = f"Artefact généré par {self.nom}"
        self.trace = hashlib.sha256(json.dumps(contexte, sort_keys=True).encode()).hexdigest()[:16] + "..."
        print(f"[{self.nom}] ✓ Terminé")
        return {"agent": self.nom, "statut": self.statut}

class AgentCoordinateur:
    def __init__(self):
        self.agents = [AgentBase(n) for n in ["Agent Archi", "Agent Juriste", "Agent Dev", "Agent Paiement", "Agent Marketing"]]

    async def lancer_projet(self, idee: str):
        print(f"\n🚀 Lancement : {idee}\n")
        resultats = [await a.executer({"idee": idee}) for a in self.agents]
        dossier = Path(f"projects/PROJ_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
        dossier.mkdir(parents=True, exist_ok=True)
        print(f"✅ PROJET CRÉÉ ! Dossier : {dossier}\n")

async def main():
    print("🔥 FORGE D'AGENTS IA AUTONOMES - GEMINI CORE 2.6 PRO\n")
    idees = ["Boutique vêtements traditionnels", "Livraison repas Darija", "Plateforme cours en Darija"]
    for i, idee in enumerate(idees, 1):
        print(f"{i}. {idee}")
    choix = input("\nVotre choix : ").strip()
    idee_sel = idees[int(choix)-1] if choix.isdigit() and 1 <= int(choix) <= len(idees) else choix
    await AgentCoordinateur().lancer_projet(idee_sel)

if __name__ == "__main__":
    asyncio.run(main())
