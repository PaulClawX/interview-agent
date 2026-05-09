from interview_agent.cli import PrepPlan, list_skills


def test_list_skills_includes_resume_rewrite():
    assert "resume-rewrite" in list_skills()


def test_plan_mentions_research_and_probability():
    rendered = PrepPlan(company="OpenAI", role="AI Engineer", level="L5").render()
    assert "Research official JD" in rendered
    assert "Estimate pass probability" in rendered
    assert "OpenAI AI Engineer" in rendered
