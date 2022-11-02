from modules.set_date import get_current_date
from datetime import datetime

def test_string_to_date():
    
    assert get_current_date() == datetime.strptime('2020-01-30', "%Y-%m-%d").date()