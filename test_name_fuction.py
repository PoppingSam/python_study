from formatted_name import get_formatted_name

def test_formatted_name():
    formatted_name = get_formatted_name("Wayne","Rooney")
    assert formatted_name == "Wayne Rooney"
