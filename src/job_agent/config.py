from __future__ import annotations

from dataclasses import dataclass, field
import os


@dataclass
class PlatformCredentials:
    email: str = ""
    password: str = ""


@dataclass
class AgentConfig:
    dry_run: bool = True
    min_score: float = 0.45
    keywords: list[str] = field(default_factory=list)
    locations: list[str] = field(default_factory=list)
    linkedin: PlatformCredentials = field(default_factory=PlatformCredentials)
    jobteaser: PlatformCredentials = field(default_factory=PlatformCredentials)


def _split_csv(value: str) -> list[str]:
    return [part.strip() for part in value.split(",") if part.strip()]


def load_config() -> AgentConfig:
    min_score = float(os.getenv("JOB_AGENT_MIN_SCORE", "0.45"))
    min_score = max(0.0, min(1.0, min_score))
    return AgentConfig(
        dry_run=os.getenv("JOB_AGENT_DRY_RUN", "true").lower() == "true",
        min_score=min_score,
        keywords=_split_csv(os.getenv("KEYWORDS", "")),
        locations=_split_csv(os.getenv("LOCATIONS", "")),
        linkedin=PlatformCredentials(
            email=os.getenv("LINKEDIN_EMAIL", ""),
            password=os.getenv("LINKEDIN_PASSWORD", ""),
        ),
        jobteaser=PlatformCredentials(
            email=os.getenv("JOBTEASER_EMAIL", ""),
            password=os.getenv("JOBTEASER_PASSWORD", ""),
        ),
    )
