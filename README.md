# Job Application Agent

Base pour automatiser la recherche/candidature (en mode dry-run au départ), avec interface utilisateur.

## Lancer l'interface utilisateur

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[ui]
streamlit run src/job_agent/ui.py
```

## Où mettre tes coordonnées et ton CV

- **Coordonnées candidat**: via l'interface, bouton **"Enregistrer mon profil"**.
  - Le fichier est sauvegardé dans: `data/candidate_profile.json`
- **CV (PDF)**: via l'upload dans l'interface.
  - Le fichier est sauvegardé dans: `data/cv/`
- **Identifiants LinkedIn / JobTeaser**: dans `.env` (à partir de `.env.example`).

## Lancer en CLI (sans interface)

```bash
cp .env.example .env
PYTHONPATH=src python -m job_agent.main
```

## Fonctionnalités actuelles

- Bouton pour lancer la recherche
- Indicateurs: nombre d'offres scannées, candidatures envoyées, taux de réussite
- Connecteurs LinkedIn/JobTeaser en mode mock (safe)

## Prochaines étapes

- Brancher Playwright avec les sélecteurs réels
- Générer les réponses de formulaire/lettres
- Ajouter stockage historique (SQLite)
