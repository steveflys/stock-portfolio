import pytest
from pyramid import testing


@pytest.fixture
def dummy_request():
    return testing.DummyRequest()


# @pytest.fixture
# def confiuration(request):

#     config = testing.setUp(settings={
#         # 'sqlalchemy.url': 'postgres://localhost:5432/entries_test'
          
#     })
    #   config.include('stock_portfolio.models')
    #   config.include('stock_portfolio.routes')