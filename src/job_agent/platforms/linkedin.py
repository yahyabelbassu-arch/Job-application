from __future__ import annotations

from job_agent.models import JobOffer, Platform
from job_agent.platforms.base import PlatformClient


class LinkedInClient(PlatformClient):
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password

    def fetch_offers(self, keywords: list[str], locations: list[str]) -> list[JobOffer]:
        # TODO: brancher Playwright + sélecteurs réels LinkedIn.
        # Mock initial pour valider le pipeline.
        return [
            JobOffer(
                id="li-1",
                title="Backend Python Engineer",
                company="ExampleCorp",
                location="Paris",
                description="Conception APIs Python, FastAPI, CI/CD.",
                url="https://www.linkedin.com/jobs/view/1",
                platform=Platform.LINKEDIN,
            )
        ]

    def apply(self, offer: JobOffer, dry_run: bool = True) -> bool:
        if dry_run:
            print(f"[DRY-RUN][LinkedIn] Candidature simulée: {offer.title} - {offer.company}")
            return True
        # TODO: implémenter la soumission réelle.
        return False
