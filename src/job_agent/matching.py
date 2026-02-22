from __future__ import annotations

from job_agent.models import CandidateProfile, JobOffer, ApplicationDecision


def evaluate_offer(offer: JobOffer, profile: CandidateProfile, min_score: float) -> ApplicationDecision:
    text = f"{offer.title} {offer.description} {offer.location}".lower()

    keyword_hits = sum(1 for kw in profile.target_keywords if kw.lower() in text)
    keyword_score = keyword_hits / max(len(profile.target_keywords), 1)

    location_match = any(loc.lower() in offer.location.lower() for loc in profile.preferred_locations)
    location_score = 1.0 if location_match or not profile.preferred_locations else 0.0

    score = round((0.75 * keyword_score) + (0.25 * location_score), 2)

    reasons = [
        f"keywords: {keyword_hits}/{max(len(profile.target_keywords), 1)}",
        f"location_match: {location_match}",
    ]

    return ApplicationDecision(
        offer=offer,
        score=score,
        should_apply=score >= min_score,
        reasons=reasons,
    )
