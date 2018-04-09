from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import MyModel
from ..sample_data import MOCK_DATA
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
import requests
import json

API_URL = 'https://api.iextrading.com/1.0'


@view_config(
    route_name='home',
    renderer='../templates/index.jinja2'
    )
def my_home_view(request):
    return {}


@view_config(route_name='auth',
    renderer='../templates/login.jinja2',
    )
def my_login_view(request):
    if request.method == 'GET':
        try:
            username = request.GET['username']
            password = request.GET['password']
            print('User: {}, Pass: {}'.format(username, password))

            return HTTPFound(location=request.route_url('portfolio'))

        except KeyError:
            return {}

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print('User: {}, Pass: {}, Email: {}'.format(username, password, email))

        return HTTPFound(location=request.route_url('entries'))

    return HTTPNotFound()


@view_config(route_name='portfolio',
    renderer='../templates/portfolio.jinja2',
    )
def my_portfolio_view(request):
    """This will disply their protfolio from the MOCK_DATA file. and if a stock is added will query the API and append that stock data to the MOCK_DATA"""
    if request.method == 'GET':
        return {'entries': MOCK_DATA}
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        symbol = request.POST['symbol']
        response = requests.get(API_URL + '/stock/{}/company'.format(symbol))
        data = response.json()
        MOCK_DATA.append(data)
        return {'entries': MOCK_DATA}


@view_config(route_name='detail',
    renderer='../templates/stock-detail.jinja2',
    )
def my_detail_view(request):
    """This will take the symbol from the portfolio page and display all the stock info for that symbol from MOCK_DATA"""
    for stock in MOCK_DATA:
        if stock['symbol'] == request.matchdict['symbol']:
            return {'stock': stock}


@view_config(route_name='add',
    renderer='../templates/stock-add.jinja2',
    )
def my_add_view(request):
    """This alows the customer to query the API with the stock symbol and returns the stock data. The customer can then add that stock to their portfolio and bget passed to the new portfolio page"""
    if request.method == 'GET':
        try:
            symbol = request.GET['symbol']

        except KeyError:
            return {}

        # import pdb; pdb.set_trace()
        response = requests.get(API_URL + '/stock/{}/company'.format(symbol))
        company = response.json()
        return {'data': company}
        

db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_stock_portfolio_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
