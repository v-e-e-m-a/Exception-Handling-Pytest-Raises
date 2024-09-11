import pytest
from school_name import claim_unreserved_code_school_name

def test_valid_name():
    result = claim_unreserved_code_school_name("Some Code School")
    assert result is True


def test_invalid_name():
    with pytest.raises(ValueError):
        claim_unreserved_code_school_name("Ada Developers Academy")