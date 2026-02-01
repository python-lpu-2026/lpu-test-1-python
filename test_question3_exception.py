import json
from question3 import high_earners_by_department

def test_q3_exception():                   # 4 marks
    assert high_earners_by_department("bad.json", "IT", 50000) == []
