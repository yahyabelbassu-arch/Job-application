from __future__ import annotations

from abc import ABC, abstractmethod
from job_agent.models import JobOffer


class PlatformClient(ABC):
    """Contrat minimal pour tout connecteur de plateforme."""

    @abstractmethod
    def fetch_offers(self, keywords: list[str], locations: list[str]) -> list[JobOffer]:
        """Récupère des offres selon les filtres.

        Cette méthode peut utiliser API officielle ou navigateur automatisé.
        """

    @abstractmethod
    def apply(self, offer: JobOffer, dry_run: bool = True) -> bool:
        """Soumet (ou simule) une candidature pour une offre."""
