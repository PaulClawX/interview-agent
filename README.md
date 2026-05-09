# Interview Agent

[![中文 README](https://img.shields.io/badge/README-%E4%B8%AD%E6%96%87-blue)](README.zh-CN.md)

![Interview Agent Architecture](docs/interview-agent.png)

Interview Agent is a skill-driven preparation workspace for artificial intelligence interviews. It helps candidates research roles and interviewers, improve resumes, generate self-introductions, build mock interview question sets, run mock interview loops, estimate pass probability, and estimate offer packages.

## Usage (Minimal)

Paste this as-is into your agent/chat tool, attach your resume + JD, then answer follow-ups:

```text
Use this repository's interview-agent skill.

Company:
Role:
Level:
Location:
Stage:
Timeline:

Deliverables:
1) Deep research (sources + confidence)
2) Resume rewrite + scorecard
3) 30s / 90s / 2-min self-introduction
4) Mock loop + question bank + rubrics
5) Pass probability range
6) Offer package range
```

Focused skills (narrow tasks):

```text
Use skills/resume-rewrite ...
Use skills/job-and-interviewer-research ...
Use skills/self-introduction ...
Use skills/mock-question-generator ...
Use skills/mock-interview-flow ...
Use skills/pass-probability ...
Use skills/offer-package-estimator ...
```

## Default Language

English is the default project language. Several skills include bilingual English and Chinese instructions because the target users may prepare in either language.

## Optional: Local CLI

```bash
uv venv
source .venv/bin/activate
uv pip install -e .
interview-agent list-skills
interview-agent plan --company "Meta" --role "Senior Machine Learning Engineer" --level "E5"
```

## Deep Research Requirement

For role-specific or company-specific interview preparation, the agent must browse broadly before producing final recommendations. The research pass should include:

- Official company career pages, recruiter guides, engineering blogs, and job descriptions.
- Recent interview guides and candidate reports.
- Public compensation sources such as Levels.fyi, company pay bands, H1B data where relevant, and recruiter-posted ranges.
- Interview experiences from communities such as LeetCode Discuss, Reddit, Blind-style posts, and GitHub repos, treated as anecdotal evidence.
- Current AI domain signals: model architectures, LLM systems, RAG, agents, multimodal systems, recommendation systems, distributed training, evaluation, safety, and AI infrastructure.

The agent must cite sources, separate verified facts from inference, and avoid presenting compensation or pass probability as guaranteed.

## Disclaimer

This repository provides interview preparation support, not legal, financial, immigration, or employment guarantees. Pass probability and compensation estimates are probabilistic planning aids based on available evidence.
