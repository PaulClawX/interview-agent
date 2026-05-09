from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = REPO_ROOT / "skills"


@dataclass(frozen=True)
class PrepPlan:
    company: str
    role: str
    level: str | None = None
    language: str = "English"

    def render(self) -> str:
        level = self.level or "unspecified level"
        return "\n".join(
            [
                f"Preparation plan for {self.company} {self.role} ({level})",
                "",
                "1. Research official JD, engineering/research blogs, recent interview reports, and compensation sources.",
                "2. Score resume against role alignment, technical depth, measured impact, ownership, AI domain signal, and communication quality.",
                "3. Build a positioning narrative and 30s/90s/2min self-introduction.",
                "4. Generate coding, ML fundamentals, ML system design, project deep dive, and behavioral questions.",
                "5. Run timed mock rounds with pass/lean-pass/lean-no/no-hire scoring.",
                "6. Estimate pass probability as a range with assumptions and improvement levers.",
                "7. Estimate offer package after current market research and level mapping.",
                "",
                f"Default output language: {self.language}",
            ]
        )


def list_skills() -> str:
    if not SKILLS_DIR.exists():
        return "No skills directory found."
    names = sorted(p.name for p in SKILLS_DIR.iterdir() if (p / "SKILL.md").exists())
    return "\n".join(f"- {name}" for name in names)


def read_skill(name: str) -> str:
    path = SKILLS_DIR / name / "SKILL.md"
    if not path.exists():
        available = list_skills()
        raise SystemExit(f"Skill not found: {name}\n\nAvailable skills:\n{available}")
    return path.read_text(encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Interview Agent local helper CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list-skills", help="List available focused skills")

    show_skill = subparsers.add_parser("show-skill", help="Print a skill file")
    show_skill.add_argument("name", help="Skill directory name, such as resume-rewrite")

    plan = subparsers.add_parser("plan", help="Render a preparation plan skeleton")
    plan.add_argument("--company", required=True)
    plan.add_argument("--role", required=True)
    plan.add_argument("--level")
    plan.add_argument("--language", default="English")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "list-skills":
        print(list_skills())
        return 0
    if args.command == "show-skill":
        print(read_skill(args.name))
        return 0
    if args.command == "plan":
        print(PrepPlan(company=args.company, role=args.role, level=args.level, language=args.language).render())
        return 0

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
