from __future__ import annotations

from job_agent.config import AgentConfig
from job_agent.models import CandidateProfile
from job_agent.platforms.linkedin import LinkedInClient
from job_agent.platforms.jobteaser import JobTeaserClient
from job_agent.matching import evaluate_offer


class JobApplicationAgent:
    def __init__(self, config: AgentConfig, profile: CandidateProfile | None = None) -> None:
        self.config = config
        self.profile = profile or CandidateProfile(
            full_name="Candidate",
            target_keywords=config.keywords,
            preferred_locations=config.locations,
        )
        self.clients = [
            LinkedInClient(config.linkedin.email, config.linkedin.password),
            JobTeaserClient(config.jobteaser.email, config.jobteaser.password),
        ]

    def run(self) -> dict[str, int | float]:
        scanned = 0
        applied = 0

        for client in self.clients:
            offers = client.fetch_offers(self.config.keywords, self.config.locations)
            for offer in offers:
                scanned += 1
                decision = evaluate_offer(offer, self.profile, self.config.min_score)
                print(f"[{offer.platform}] {offer.title} -> score={decision.score} apply={decision.should_apply}")
                if decision.should_apply and client.apply(offer, dry_run=self.config.dry_run):
                    applied += 1

        success_rate = round((applied / scanned), 2) if scanned else 0.0
        return {"scanned": scanned, "applied": applied, "success_rate": success_rate}
