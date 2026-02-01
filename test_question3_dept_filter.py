import json
from question3 import high_earners_by_department

def test_q3_department_filter(tmp_path):  # 4 marks
    f = tmp_path / "e.json"
    f.write_text(json.dumps([
        {"name":"A","department":"HR","salary":60000}
    ]))
    assert high_earners_by_department(str(f), "IT", 50000) == []
