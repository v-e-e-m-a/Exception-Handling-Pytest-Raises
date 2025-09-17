from school_name import claim_unreserved_code_school_name

def test_invalid_name_no_pytest():
    # Implement the equivalent of this test logic but DO NOT import or otherwise access pytest:

    # with pytest.raises(ValueError):
    #     claim_unreserved_code_school_name("Ada Developers Academy")

    # Think about what the test actually does and think about how to write them ourselves.
    try:
        school_name = 'Ada Developers Academy'
        claim_unreserved_code_school_name(school_name)
        assert False
    except ValueError as error:
        assert "There's already an awesome school with that name!"
    

    # Replace this with your own logic
    #raise Exception("test not implemented")