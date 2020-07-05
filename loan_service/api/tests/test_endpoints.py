import pytest
from django.urls import reverse


@pytest.fixture
def loan_request_valid_data(db):
    loan_data = {'name': 'a', 'cpf': 'a', 'birthdate': '1990-7-13', 'amount': 1200.00, 'terms': 6, 'income': 1045.00}
    return loan_data


@pytest.fixture
def loan_request_invalid_data_amount_over_4000(db):
    loan_data = {'name': 'a', 'cpf': 'a', 'birthdate': '1990-7-13', 'amount': 4200.00, 'terms': 6, 'income': 1045.00}
    return loan_data


@pytest.fixture
def loan_request_invalid_data_amount_less_1000(db):
    loan_data = {'name': 'a', 'cpf': 'a', 'birthdate': '1990-7-13', 'amount': 4200.00, 'terms': 6, 'income': 900.00}
    return loan_data


@pytest.fixture
def loan_request_invalid_data_terms(db):
    loan_data = {'name': 'a', 'cpf': 'a', 'birthdate': '1990-7-13', 'amount': 4200.00, 'terms': 3, 'income': 1045.00}
    return loan_data


@pytest.fixture
def resp(loan_request_valid_data, client):
    return client.post(reverse('api:loan'), data=loan_request_valid_data)


@pytest.fixture
def resp_amount_over_4000(loan_request_invalid_data_amount_over_4000, client):
    return client.post(reverse('api:loan'), data=loan_request_invalid_data_amount_over_4000)


@pytest.fixture
def resp_amount_less_1000(loan_request_invalid_data_amount_less_1000, client):
    return client.post(reverse('api:loan'), data=loan_request_invalid_data_amount_less_1000)


@pytest.fixture
def resp_invalid_terms(loan_request_invalid_data_terms, client):
    return client.post(reverse('api:loan'), data=loan_request_invalid_data_terms)


def test_resp_amount_over_4000_status_code_400(resp_amount_over_4000):
    assert resp_amount_over_4000.status_code == 400


def test_resp_amount_less_1000_status_code_400(resp_amount_less_1000):
    assert resp_amount_less_1000.status_code == 400


def test_resp_invalid_terms_status_code_400(resp_invalid_terms):
    assert resp_invalid_terms.status_code == 400


def test_cria_um_loan(resp):
    assert 'uuid' in resp.data.keys()
