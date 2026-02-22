from pathlib import Path

from job_agent.models import CandidateProfile
from job_agent.profile import load_profile, save_profile


def test_profile_save_and_load(tmp_path: Path) -> None:
    target = tmp_path / "candidate_profile.json"
    profile = CandidateProfile(
        full_name="Test User",
        email="test@example.com",
        phone="0102030405",
        linkedin_url="https://linkedin.com/in/test",
        cv_path="data/cv/test.pdf",
        target_keywords=["python"],
        preferred_locations=["paris"],
    )

    save_profile(profile, target)
    loaded = load_profile(target)

    assert loaded.full_name == "Test User"
    assert loaded.email == "test@example.com"
    assert loaded.cv_path == "data/cv/test.pdf"
