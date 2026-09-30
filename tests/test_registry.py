import pytest
from adapters.registry import ToolRegistry
from tools import profile_source


def test_register_and_duplicate_rejected():
    registry = ToolRegistry()
    registry.register(profile_source)
    assert registry.get("profile_source") is profile_source
    with pytest.raises(ValueError):
        registry.register(profile_source)
