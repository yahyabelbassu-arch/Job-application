from job_agent.agent import JobApplicationAgent
from job_agent.config import load_config
from job_agent.profile import load_profile


def main() -> None:
    config = load_config()
    profile = load_profile()
    agent = JobApplicationAgent(config, profile=profile)
    result = agent.run()
    print(f"Résumé: {result}")


if __name__ == "__main__":
    main()
