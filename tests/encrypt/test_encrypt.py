from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("john", "doe")

    with pytest.raises(TypeError):
        encrypt_message(0, 1)

    assert encrypt_message("mouse", 10) == "esuom"

    assert encrypt_message("mouse", 4) == "e_suom"

    assert encrypt_message("mouse", 3) == "uom_es"
