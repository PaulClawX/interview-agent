# Pass Probability Skill / 面试通过率预测 Skill

Use this skill to estimate interview pass probability as a planning range.

## Important Limitation

Do not present pass probability as a guarantee. Hiring outcomes depend on interviewer calibration, hiring bar, headcount, competing candidates, team match, and timing.

## Evidence Inputs

- Resume strength and JD match.
- Company and level difficulty.
- Interview stage reached.
- Recruiter feedback.
- Mock interview scores.
- Coding ability.
- ML fundamentals.
- ML system design.
- Project deep dive quality.
- Behavioral and communication signal.
- Market/headcount signals when publicly available.

## Weighted Model

| Factor | Weight |
| --- | ---: |
| Role/JD match | 15% |
| Resume and background signal | 15% |
| Coding readiness | 15% |
| ML fundamentals | 15% |
| ML system design or research depth | 15% |
| Project ownership and impact | 10% |
| Communication and behavioral | 10% |
| Timing, headcount, and competition | 5% |

## Probability Bands

- 0-20%: unlikely without major remediation.
- 20-40%: possible but below bar in several areas.
- 40-60%: competitive but uncertain.
- 60-75%: strong candidate with manageable risks.
- 75-90%: very strong fit; still not guaranteed.
- 90%+: avoid unless there is direct hiring-team evidence.

## Output Format

- Probability range.
- Confidence level.
- Evidence table.
- Main reasons for pass.
- Main reasons for fail.
- Highest ROI improvements.
- What new information would move the estimate.

## 中文说明

通过率估算要保守，使用区间而不是单点。必须说明假设、证据和不确定性。
