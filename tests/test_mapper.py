from src.mapper import map_severity_to_priority

def test_severity_mapping():
    assert map_severity_to_priority("High") == "Highest"

