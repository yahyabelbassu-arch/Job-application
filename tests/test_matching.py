from job_agent.matching import evaluate_offer
from job_agent.models import CandidateProfile, JobOffer, Platform


def test_evaluate_offer_returns_apply_true_on_good_match() -> None:
    offer = JobOffer(
        id="1",
        title="Python Backend Engineer",
        company="ACME",
        location="Paris",
        description="API Python, tests, CI/CD",
        url="https://example.com/job/1",
        platform=Platform.LINKEDIN,
    )
    profile = CandidateProfile(
        full_name="Test User",
        target_keywords=["python", "api"],
        preferred_locations=["paris"],
    )

    decision = evaluate_offer(offer, profile, min_score=0.5)

    assert decision.should_apply is True
    assert decision.score >= 0.5
