from job_agent.agent import JobApplicationAgent
from job_agent.config import AgentConfig
from job_agent.models import CandidateProfile


def test_agent_returns_success_rate() -> None:
    config = AgentConfig(dry_run=True, min_score=0.2, keywords=["python"], locations=["paris"])
    profile = CandidateProfile(full_name="Alice", target_keywords=["python"], preferred_locations=["paris"])

    result = JobApplicationAgent(config, profile=profile).run()

    assert result["scanned"] == 2
    assert result["applied"] == 2
    assert result["success_rate"] == 1.0
