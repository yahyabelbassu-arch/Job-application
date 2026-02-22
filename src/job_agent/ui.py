from __future__ import annotations

from dataclasses import replace

import streamlit as st

from job_agent.agent import JobApplicationAgent
from job_agent.config import load_config
from job_agent.models import CandidateProfile
from job_agent.profile import load_profile, save_profile, save_cv


st.set_page_config(page_title="Job Application Agent", page_icon="💼", layout="wide")


st.title("💼 Agent de candidature")
st.caption("Pilotage des recherches, suivi des candidatures et configuration de votre profil.")

saved_profile = load_profile()
config = load_config()

with st.sidebar:
    st.header("Vos coordonnées")
    full_name = st.text_input("Nom complet", value=saved_profile.full_name)
    email = st.text_input("Email", value=saved_profile.email)
    phone = st.text_input("Téléphone", value=saved_profile.phone)
    linkedin_url = st.text_input("URL LinkedIn", value=saved_profile.linkedin_url)

    st.header("Préférences")
    keywords = st.text_input(
        "Mots-clés (séparés par virgule)",
        value=", ".join(saved_profile.target_keywords or config.keywords),
    )
    locations = st.text_input(
        "Localisations (séparées par virgule)",
        value=", ".join(saved_profile.preferred_locations or config.locations),
    )

    st.header("CV")
    uploaded_cv = st.file_uploader("Déposez votre CV (PDF)", type=["pdf"])

    if st.button("💾 Enregistrer mon profil", use_container_width=True):
        profile = CandidateProfile(
            full_name=full_name,
            email=email,
            phone=phone,
            linkedin_url=linkedin_url,
            target_keywords=[x.strip() for x in keywords.split(",") if x.strip()],
            preferred_locations=[x.strip() for x in locations.split(",") if x.strip()],
            cv_path=saved_profile.cv_path,
        )

        if uploaded_cv is not None:
            profile = replace(profile, cv_path=save_cv(uploaded_cv.name, uploaded_cv.getvalue()))

        save_profile(profile)
        st.success("Profil enregistré. ✅")
        saved_profile = profile

st.subheader("Indicateurs")
scanned = st.session_state.get("scanned", 0)
applied = st.session_state.get("applied", 0)
success_rate = (applied / scanned * 100) if scanned else 0.0

c1, c2, c3 = st.columns(3)
c1.metric("Offres analysées", scanned)
c2.metric("Candidatures envoyées", applied)
c3.metric("Taux de réussite", f"{success_rate:.1f}%")

st.subheader("Lancer une recherche")
if st.button("🚀 Lancer la recherche", type="primary"):
    agent = JobApplicationAgent(config, profile=saved_profile)
    result = agent.run()
    st.session_state["scanned"] = result["scanned"]
    st.session_state["applied"] = result["applied"]
    st.success("Recherche terminée.")
    st.json(result)

st.info(
    "📁 Vos coordonnées sont stockées dans `data/candidate_profile.json` et le CV dans `data/cv/`. "
    "Les identifiants LinkedIn/JobTeaser restent dans `.env`."
)
