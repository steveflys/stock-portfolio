from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPBadRequest
from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import Entry
from . import DB_ERR_MSG
import requests
import os


API_URL = 'https://api.iextrading.com/1.0'


@view_config(route_name='portfolio', renderer='../templates/portfolio.jinja2', request_method='GET')
def entries_view(request):
    try:
        query = request.dbsession.query(Stock)
        all_entries = query.all()
    except DBAPIError:
        return Response(DB_ERR_MSG, content_type='text/plain', status=500)

    return {'stocks': all_stocks}


@view_config(route_name='detail', renderer='../templates/stock-detail.jinja2', request_method='GET')
def detail_view(request):
    # try:
    #     stock_symbol = request.matchdict['symbol']
    # except KeyError:
    #     return HTTPNotFound()

    try:
        query = request.dbsession.query(Stock)
        stock_detail = query.filter(Stock.id == stock_id).first()
    except DBAPIError:
        return Response(DB_ERR_MSG, content_type='text/plain', status=500)

    # res = requests.get('https://pixabay.com/api?key={}&q={}'.format(
    #     API_KEY, entry_detail.title.split(' ')[0]))

    # try:
    #     url = res.json()['hits'][0]['webformatURL']
    # except (KeyError, IndexError):
    #     url = 'https://via.placeholder.com/300x300'

    return {
        "entry": entry_detail,
        "img": url,
        stock.companyName
        stock.symbol
        stock.CEO
        stock.website
        stock.industry
        stock.sector
        stock.exchange
        stock.issueType
        stock.description

    'id'
    'symbol'
    'companyName' 
    'CEO'
    'website'
    'industry'
    'sector'
    'exchange'
    'issueType'
    'description'
    }


@view_config(route_name='new', renderer='../templates/new.jinja2')
def new_view(request):
    if request.method == 'POST':
        if not all([field in request.POST for field in ['title', 'body', 'date', 'author']]):
            raise HTTPBadRequest

        instance = Entry(
            title=request.POST['title'],
            body=request.POST['body'],
            date=request.POST['date'],
            author=request.POST['author'],
        )

        try:
            request.dbsession.add(instance)
        except DBAPIError:
            return Response(DB_ERR_MSG, content_type='text/plain', status=500)

        return HTTPFound(location=request.route_url('entries'))
    if request.method == 'GET':
        return {}