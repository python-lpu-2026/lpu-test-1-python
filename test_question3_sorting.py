import json
from question3 import high_earners_by_department

def test_q3_sorting(tmp_path):             # 4 marks
    f = tmp_path / "e.json"
    f.write_text(json.dumps([
        {"name":"A","department":"IT","salary":60000},
        {"name":"B","department":"IT","salary":80000}
    ]))
    assert high_earners_by_department(str(f), "IT", 50000) == ["B", "A"]
