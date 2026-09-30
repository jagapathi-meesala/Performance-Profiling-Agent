from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_manifest_required_fields_and_local_references():
    data = yaml.safe_load((ROOT / "agent.yaml").read_text())
    assert data["spec_version"] == "0.1.0"
    assert data["name"] == "performance-profiling-agent"
    assert data["version"] == "1.0.0"
    for key in ("skills", "tools"):
        assert isinstance(data[key], list)
        assert all(isinstance(item, str) for item in data[key])
        if key == "skills":
            assert all(
                (ROOT / "skills" / item / "SKILL.md").is_file()
                for item in data[key]
            )
        else:
            assert all(
                (ROOT / "tools" / f"{item}.yaml").is_file()
                for item in data[key]
            )
    assert "display_name" not in data
    assert "entrypoint" not in data
    assert "portability" not in data
