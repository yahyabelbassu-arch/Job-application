from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Platform(str, Enum):
    LINKEDIN = "linkedin"
    JOBTEASER = "jobteaser"


@dataclass
class JobOffer:
    id: str
    title: str
    company: str
    location: str
    description: str
    url: str
    platform: Platform


@dataclass
class CandidateProfile:
    full_name: str
    email: str = ""
    phone: str = ""
    linkedin_url: str = ""
    cv_path: str = ""
    target_keywords: list[str] = field(default_factory=list)
    preferred_locations: list[str] = field(default_factory=list)


@dataclass
class ApplicationDecision:
    offer: JobOffer
    score: float
    should_apply: bool
    reasons: list[str] = field(default_factory=list)
