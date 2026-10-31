#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════╗
║          FORGE D'AGENTS IA AUTONOMES                         ║
║                 GEMINI CORE 2.6 PRO                          ║
║                                                              ║
║  Système Souverain • Made in Algeria • IA22 Certified        ║
║  Auteur  : Zoubirou Mohammed Ilyes                           ║
║  ORCID   : 0009-0007-7571-3178                               ║
║  Version : Final 2.6.1 (2026-08-17)                          ║
╚══════════════════════════════════════════════════════════════╝
"""

import asyncio
import json
import hashlib
from datetime import datetime
from pathlib import Path

# ============================================================
# CONFIGURATION
# ============================================================
VERSION = "2.6.1-Final"
AUTEUR = "Zoubirou Mohammed Ilyes"
ORCID = "0009-0007-7571-3178"
CERTIFICATION = "IA22 Certified – NetSecurePro"

IDEES_PAR_DEFAUT = [
    "Boutique vêtements traditionnels",
    "Livraison repas Darija",
    "Plateforme cours en Darija",
    "Application de gestion de stock locale",
    "Marketplace artisanat algérien"
]

# ============================================================
# AGENT DE BASE
# ============================================================
class AgentBase:
    def __init__(self, nom: str):
        self.nom = nom
        self.statut = "initialisé"
        self.artefact = None
        self.trace = None

    async def executer(self, contexte: dict) -> dict:
        print(f"[{self.nom}] → Démarrage...")
        await asyncio.sleep(0.5)

        idee = contexte.get("idee", "Projet non spécifié")

        if "Archi" in self.nom:
            contenu = {
                "role": "Architecture",
                "analyse": f"Architecture technique souveraine pour : {idee}",
                "stack_recommandee": ["Python 3", "FastAPI", "SQLite", "Termux-native", "HTML/CSS/JS"],
                "structure": ["backend/", "frontend/", "docs/", "scripts/", "data/"],
                "principes": ["Offline-first", "Zero-Trust", "Local-only"]
            }
        elif "Juriste" in self.nom:
            contenu = {
                "role": "Juridique & Conformité",
                "analyse": f"Cadre légal minimal pour : {idee}",
                "points_cles": [
                    "Données 100% locales (pas de cloud)",
                    "Licence souveraine / MIT adaptée",
                    "Mentions légales simplifiées",
                    "Respect RGPD par design (données ne quittent pas l'appareil)"
                ],
                "risques": ["Très faible – exécution locale"]
            }
        elif "Dev" in self.nom:
            contenu = {
                "role": "Développement",
                "analyse": f"Plan de développement pour : {idee}",
                "etapes": [
                    "Jour 1-2 : Structure + API locale",
                    "Jour 3-4 : Interface Termux + Web minimal",
                    "Jour 5-7 : Tests + packaging"
                ],
                "langages": ["Python", "Bash", "HTML/CSS/JS"],
                "priorite": "MVP fonctionnel en 7 jours"
            }
        elif "Paiement" in self.nom:
            contenu = {
                "role": "Monétisation",
                "analyse": f"Stratégie de monétisation souveraine pour : {idee}",
                "modeles": [
                    "Freemium local",
                    "Paiement cash / CCP / BaridiMob",
                    "Abonnement mensuel hors-ligne"
                ],
                "recommandation": "Éviter les gateways internationaux au démarrage"
            }
        else:  # Marketing
            contenu = {
                "role": "Marketing & Diffusion",
                "analyse": f"Stratégie marketing locale pour : {idee}",
                "canaux": [
                    "WhatsApp Business",
                    "Groupes Facebook/Telegram locaux",
                    "Bouche-à-oreille en Darija",
                    "Affiches et réseaux de proximité"
                ],
                "slogan": f"« {idee} – 100% local, 100% souverain »"
            }

        self.statut = "terminé"
        self.artefact = contenu
        raw = json.dumps(contenu, sort_keys=True, ensure_ascii=False)
        self.trace = hashlib.sha256(raw.encode()).hexdigest()[:16] + "..."

        print(f"[{self.nom}] ✓ Terminé")
        return {
            "agent": self.nom,
            "statut": self.statut,
            "artefact": self.artefact,
            "trace": self.trace
        }


# ============================================================
# COORDINATEUR
# ============================================================
class AgentCoordinateur:
    def __init__(self):
        self.agents = [
            AgentBase("Agent Archi"),
            AgentBase("Agent Juriste"),
            AgentBase("Agent Dev"),
            AgentBase("Agent Paiement"),
            AgentBase("Agent Marketing")
        ]

    async def lancer_projet(self, idee: str):
        print(f"\n🚀 Lancement du projet : {idee}\n")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dossier = Path(f"projects/PROJ_{timestamp}")
        dossier.mkdir(parents=True, exist_ok=True)

        # Exécution des agents
        resultats = []
        for agent in self.agents:
            res = await agent.executer({"idee": idee})
            resultats.append(res)

        # ========== GÉNÉRATION DES ARTEFACTS ==========

        # 1. resume.md
        resume = f"""# {idee}

**Généré par**     : GEMINI CORE 2.6 PRO  
**Version**        : {VERSION}  
**Date**           : {datetime.now().isoformat()}  
**Auteur**         : {AUTEUR}  
**ORCID**          : {ORCID}  
**Certification**  : {CERTIFICATION}  

---

## Résumé des agents

"""
        for r in resultats:
            resume += f"### {r['agent']}\n"
            resume += f"- Statut : **{r['statut']}**\n"
            resume += f"- Trace  : `{r['trace']}`\n\n"

        (dossier / "resume.md").write_text(resume, encoding="utf-8")

        # 2. resultat_agents.json
        (dossier / "resultat_agents.json").write_text(
            json.dumps(resultats, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

        # 3. artefact_sha256.txt
        full_hash = hashlib.sha256(
            json.dumps(resultats, sort_keys=True, ensure_ascii=False).encode()
        ).hexdigest()
        (dossier / "artefact_sha256.txt").write_text(
            f"SHA256 du projet complet : {full_hash}\n"
            f"Généré le               : {datetime.now().isoformat()}\n"
            f"Version                 : {VERSION}\n"
            f"Auteur                  : {AUTEUR}\n",
            encoding="utf-8"
        )

        # 4. plan_action.md
        plan = f"""# Plan d'action – {idee}

## Phase 1 – Conception (Jours 1-2)
- Architecture technique (Agent Archi)
- Cadre juridique minimal (Agent Juriste)

## Phase 2 – Développement (Jours 3-5)
- MVP fonctionnel
- Interface compatible Termux + navigateur

## Phase 3 – Lancement (Jours 6-7)
- Communication locale en Darija
- Modèle de monétisation souverain

---
*Document généré automatiquement par GEMINI CORE 2.6 PRO – {VERSION}*  
*Sceau IA22 – {datetime.now().strftime("%Y-%m-%d")}*
"""
        (dossier / "plan_action.md").write_text(plan, encoding="utf-8")

        # 5. metadata.json (bonus)
        metadata = {
            "projet": idee,
            "version_core": VERSION,
            "auteur": AUTEUR,
            "orcid": ORCID,
            "timestamp": datetime.now().isoformat(),
            "sha256": full_hash,
            "agents": [r["agent"] for r in resultats]
        }
        (dossier / "metadata.json").write_text(
            json.dumps(metadata, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

        print(f"\n✅ PROJET CRÉÉ AVEC SUCCÈS")
        print(f"   Dossier : {dossier}")
        print(f"   Fichiers générés :")
        print(f"     • resume.md")
        print(f"     • resultat_agents.json")
        print(f"     • artefact_sha256.txt")
        print(f"     • plan_action.md")
        print(f"     • metadata.json")
        print(f"   SHA256  : {full_hash[:32]}...\n")


# ============================================================
# POINT D'ENTRÉE
# ============================================================
async def main():
    print("=" * 60)
    print("🔥  FORGE D'AGENTS IA AUTONOMES")
    print(f"    GEMINI CORE 2.6 PRO – Version {VERSION}")
    print("=" * 60)
    print()

    for i, idee in enumerate(IDEES_PAR_DEFAUT, 1):
        print(f"  {i}. {idee}")
    print(f"  0. Saisir une idée personnalisée")

    choix = input("\nVotre choix : ").strip()

    if choix == "0":
        idee_sel = input("Entrez votre idée de projet : ").strip()
        if not idee_sel:
            idee_sel = IDEES_PAR_DEFAUT[0]
    elif choix.isdigit() and 1 <= int(choix) <= len(IDEES_PAR_DEFAUT):
        idee_sel = IDEES_PAR_DEFAUT[int(choix) - 1]
    else:
        idee_sel = choix if choix else IDEES_PAR_DEFAUT[0]

    await AgentCoordinateur().lancer_projet(idee_sel)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n[!] Interrompu par l'utilisateur. Au revoir.")
