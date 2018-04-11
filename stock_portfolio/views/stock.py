from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPBadRequest
from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import Stock
from . import DB_ERR_MSG
import requests


API_URL = 'https://api.iextrading.com/1.0'


@view_config(route_name='portfolio', renderer='../templates/portfolio.jinja2', request_method='GET')
def entries_view(request):
    try:
        query = request.dbsession.query(Stock)
        all_stocks = query.all()
    except DBAPIError:
        return Response(DB_ERR_MSG, content_type='text/plain', status=500)

    return {'stocks': all_stocks}


@view_config(route_name='detail', renderer='../templates/stock-detail.jinja2', request_method='GET')
def detail_view(request):
    try:
        stock_symbol = request.matchdict['symbol']
    except KeyError:
        return HTTPNotFound()

    try:
        query = request.dbsession.query(Stock)
        stock_detail = query.filter(Stock.symbol == stock_symbol).first()
    except DBAPIError:
        return Response(DB_ERR_MSG, content_type='text/plain', status=500)

    return {'stock': stock_detail}


@view_config(route_name='add', renderer='../templates/stock-add.jinja2')
def my_add_view(request):
    """This alows the customer to query the API with the stock symbol and returns the stock data. The customer can then add that stock to their portfolio and bget passed to the new portfolio page"""
    if request.method == 'GET':
        try:
            symbol = request.GET['symbol']

        except KeyError:
            return {}

        response = requests.get(API_URL + '/stock/{}/company'.format(symbol))
        company = response.json()
        return {'data': company}

    if request.method == 'POST':

        try:
            symbol = request.POST['symbol']
        except KeyError:
            raise HTTPBadRequest()

        try:
            response = requests.get(API_URL + '/stock/{}/company'.format(symbol))
            data = response.json()
        except ValueError:
            raise HTTPNotFound()

        instance = Stock(**data)

    try:
        request.dbsession.add(instance)
    except DBAPIError:
        return Response(DB_ERR_MSG, content_type='text/plain', status=500)

    return HTTPFound(location=request.route_url('portfolio'))
