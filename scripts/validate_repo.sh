#!/usr/bin/env bash
set -euo pipefail

${PYTHON:-python3} -m pytest -q
${PYTHON:-python3} -m interview_agent.cli list-skills >/tmp/interview-agent-skills.txt
for skill in resume-rewrite job-and-interviewer-research self-introduction mock-question-generator mock-interview-flow pass-probability offer-package-estimator; do
  grep -q "$skill" /tmp/interview-agent-skills.txt
done
