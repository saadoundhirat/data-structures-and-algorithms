import pytest
from stack_and_queue.stack_queue_brackets import *

def test_string_cases():
    assert validate_brackets("[stack]") == True
    assert validate_brackets("{}(){}") == True
    assert validate_brackets("{}{Code}[Fellows](())") == True
    assert validate_brackets("[({}]") == False
    assert validate_brackets("(](") == False
    assert validate_brackets("{(})") == False