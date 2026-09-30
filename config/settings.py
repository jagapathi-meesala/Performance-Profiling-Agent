"""Runtime configuration loaded exclusively from environment variables."""
import os
from dataclasses import dataclass


def _required(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Required environment variable is missing: {name}")
    return value


@dataclass(frozen=True)
class Settings:
    log_level: str
    max_input_bytes: int
    profile_timeout_seconds: float

    @classmethod
    def from_env(cls) -> "Settings":
        try:
            max_bytes = int(_required("PERF_MAX_INPUT_BYTES"))
            timeout = float(_required("PERF_PROFILE_TIMEOUT_SECONDS"))
        except ValueError as exc:
            raise ValueError(f"Invalid performance configuration: {exc}") from exc
        if max_bytes <= 0 or timeout <= 0:
            raise ValueError("PERF_MAX_INPUT_BYTES and PERF_PROFILE_TIMEOUT_SECONDS must be positive")
        return cls(_required("PERF_LOG_LEVEL"), max_bytes, timeout)
