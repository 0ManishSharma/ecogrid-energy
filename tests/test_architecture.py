from pathlib import Path


def test_max_four_deployable_services():
    services = [
        p for p in Path("services").iterdir()
        if p.is_dir() and not p.name.startswith("__")
    ]
    assert len(services) <= 4