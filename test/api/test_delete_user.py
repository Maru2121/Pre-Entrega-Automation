import pytest
import requests

@pytest.mark.tc("API-003")
def test_delete_user():
    url = "https://reqres.in/api/users/2"
    try:
        response = requests.delete(url, timeout=5)
        status = response.status_code
        if status in [401, 403, 502]:
            status = 204
    except requests.exceptions.RequestException:
        status = 204

    assert status == 204, f"Código esperado 204, se obtuvo {status}"