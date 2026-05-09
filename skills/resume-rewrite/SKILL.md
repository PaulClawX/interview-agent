# Resume Rewrite Skill / 简历修改 Skill

Use this skill to score, rewrite, and tailor resumes for AI-focused roles.

## Inputs

- Resume text or PDF extraction.
- Target job description.
- Company, level, location, and interview stage.
- Candidate type: campus, experienced, researcher, infra engineer, applied scientist, founder, or tech lead.

## Research Requirement

Before finalizing a targeted resume, research the target role and company. Use official job descriptions, company engineering/research blogs, public interview reports, and similar job postings.

## AI Resume Rubric

Score each dimension from 1 to 5 and calculate a weighted score.

| Dimension | Weight | 5-point standard |
| --- | ---: | --- |
| Role alignment | 20% | Skills, projects, seniority, and keywords directly match the JD. |
| Technical depth | 20% | Shows model choices, algorithms, architecture, evaluation, failure modes, and tradeoffs. |
| Measured impact | 20% | Quantifies business, research, infra, latency, cost, quality, or adoption outcomes. |
| Ownership and scope | 15% | Makes the candidate's personal contribution, scope, and leadership clear. |
| AI domain signal | 15% | Demonstrates relevant AI domain strength: LLM, RAG, agents, multimodal, recsys, CV, NLP, RL, infra, evaluation, or safety. |
| Communication quality | 10% | Concise, scannable, action-oriented, and free from vague claims. |

## Rewrite Rules

- Prefer bullets with `Action + Technical Mechanism + Scale + Measured Outcome`.
- Replace weak verbs such as "worked on", "participated in", and "responsible for".
- Do not fabricate metrics. If a metric is missing, write a placeholder like `[latency reduction]` or ask for the number.
- Preserve truthfulness and separate inferred improvements from confirmed facts.
- For research roles, emphasize problem framing, contribution, baseline comparison, ablations, and publication quality.
- For applied roles, emphasize deployment, online metrics, constraints, and cross-functional impact.
- For infra roles, emphasize throughput, GPU utilization, reliability, cost, distributed systems, observability, and incident handling.

## Output Format

1. Resume scorecard.
2. Biggest gaps.
3. Rewritten summary.
4. Rewritten experience bullets.
5. Keyword alignment table.
6. Questions for missing metrics.
7. Final ATS and human-reader recommendations.

## 中文说明

这个 skill 的目标不是把简历写得“更华丽”，而是让面试官在 30 秒内看出候选人的技术深度、个人贡献、业务/研究价值和岗位匹配度。不要编造数据；缺失数据用占位符或向用户追问。
