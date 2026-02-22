from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
import json

from job_agent.models import CandidateProfile


DEFAULT_PROFILE_PATH = Path("data/candidate_profile.json")
DEFAULT_CV_DIR = Path("data/cv")


def load_profile(path: Path = DEFAULT_PROFILE_PATH) -> CandidateProfile:
    if not path.exists():
        return CandidateProfile(full_name="")
    with path.open("r", encoding="utf-8") as f:
        raw = json.load(f)
    return CandidateProfile(**raw)


def save_profile(profile: CandidateProfile, path: Path = DEFAULT_PROFILE_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(asdict(profile), f, indent=2, ensure_ascii=False)


def save_cv(filename: str, content: bytes, cv_dir: Path = DEFAULT_CV_DIR) -> str:
    cv_dir.mkdir(parents=True, exist_ok=True)
    target = cv_dir / filename
    with target.open("wb") as f:
        f.write(content)
    return str(target)
