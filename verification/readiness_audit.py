from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
required = ["agent.yaml", "SOUL.md", "README.md", "AGENTS.md", "DUTIES.md", "RULES.md", "EXPLAINABILITY.md", ".env.example", ".gitignore", "requirements.txt", "pytest.ini"]
dirs_required = ["adapters", "config", "contracts", "core", "skills", "tools", "tests", "verification"]


def sentences(text: str) -> int:
    return len([x for x in re.split(r"(?<=[.!?])\s+", text.strip()) if x])


def main() -> int:
    errors = []
    for item in required:
        if not (ROOT / item).is_file(): errors.append(f"missing file: {item}")
    for item in dirs_required:
        if not (ROOT / item).is_dir(): errors.append(f"missing directory: {item}")
    doc = (ROOT / "EXPLAINABILITY.md").read_text(encoding="utf-8") if (ROOT / "EXPLAINABILITY.md").exists() else ""
    required_sections = ["## Inputs and Data Sources", "## Decision and Reasoning", "## Limits and Constraints"]
    for heading in required_sections:
        if doc.count(heading) != 1: errors.append(f"required heading missing or duplicated: {heading}")
    for bad in ["## Inputs\n", "## Decision\n", "## Limits\n"]:
        if bad in doc: errors.append(f"conflicting heading present: {bad.strip()}")
    for heading in required_sections:
        if heading in doc:
            body = doc.split(heading, 1)[1].split("\n## ", 1)[0]
            if sentences(body) < 2: errors.append(f"section has fewer than two sentences: {heading}")
    if errors:
        print("READINESS AUDIT: FAIL")
        print("\n".join(f"- {e}" for e in errors))
        return 1
    print("READINESS AUDIT: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
