from zadanie4 import models_in_codes
import time
import pytest


@pytest.mark.parametrize("test_input,expected", [
    (['720', '737', '747', '767', '777', '787'], ['B', 'O', 'E', 'I', 'N', 'G']),
    (['787', '777', '767', '747', '737', '720'], ['G', 'N', 'I', 'E', 'O', 'B']),
    (['707', '717-200'], ['A', 'A']),
    (['737 NG', '747-8'], ['u', 'z']),
    (['a', 'z', 'c'], []),
    ([], []),
    ('a', 7),
    (None,None)
])
def test_models_in_codes_values(test_input, expected):
    start = time.time()
    airplanes_codes = {
            '707': 'A',
            '717-200': 'A',
            '720': 'B',
            '727': 'X',
            '737': 'O',
            '737 NG': 'U',
            '747': 'E',
            '747-8': 'Z',
            '757': 'F',
            '767': 'I',
            '777': 'N',
            '787': 'G', }
    if not type(test_input) == list:
        pytest.xfail('wrong arguments')
    current = time.time()
    assert models_in_codes(test_input, airplanes_codes) == expected
    assert current-start < 0.1
    assert type(models_in_codes(test_input, airplanes_codes)) == list
