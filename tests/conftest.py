import pytest

@pytest.fixture
def small_list():
    return [2, 4, 6]

@pytest.fixture
def mixed_list(tmp_path):
    p = tmp_path / "nums.txt"
    p.write_text("10\n20\n30\n", encoding="utf-8")
    return [10, 20, 30]