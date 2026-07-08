from auth_profile import generate_token, verify_token


def test_generate_token():
    token = generate_token("efren")
    assert token is not None
    assert isinstance(token, str)


def test_verify_valid_token():
    token = generate_token("efren")
    decoded = verify_token(token)

    assert decoded is not None
    assert decoded["username"] == "efren"


def test_verify_invalid_token():
    decoded = verify_token("this_is_not_a_valid_token")

    assert decoded is None