from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_skill_frontmatter_and_explainability():
    for path in (ROOT / "skills").glob("*/SKILL.md"):
        text = path.read_text()
        assert text.startswith("---\n")
        assert "name:" in text.split("---", 2)[1]
    text = (ROOT / "EXPLAINABILITY.md").read_text()
    for heading in ["## Inputs and Data Sources", "## Decision and Reasoning", "## Limits and Constraints"]:
        assert text.count(heading) == 1
