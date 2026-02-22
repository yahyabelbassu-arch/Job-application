from __future__ import annotations

from job_agent.models import JobOffer, Platform
from job_agent.platforms.base import PlatformClient


class JobTeaserClient(PlatformClient):
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password

    def fetch_offers(self, keywords: list[str], locations: list[str]) -> list[JobOffer]:
        # TODO: brancher Playwright + sélecteurs réels JobTeaser.
        return [
            JobOffer(
                id="jt-1",
                title="Software Engineer Intern",
                company="CampusTech",
                location="Remote",
                description="Python, tests automatisés, APIs REST.",
                url="https://www.jobteaser.com/fr/job-offers/1",
                platform=Platform.JOBTEASER,
            )
        ]

    def apply(self, offer: JobOffer, dry_run: bool = True) -> bool:
        if dry_run:
            print(f"[DRY-RUN][JobTeaser] Candidature simulée: {offer.title} - {offer.company}")
            return True
        # TODO: implémenter la soumission réelle.
        return False
