import pytest
import script

@pytest.fixture
def mock_csv_data():
    msg = "AAABBCAAD"
    return msg

def test_get_score_difference(mock_csv_data):
    assert script.HuffmanEncoding().get_encoding() == ""

