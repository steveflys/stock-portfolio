from pyramid.response import Response
from pyramid.view import view_config
from pyramid.security import NO_PERMISSION_REQUIRED, remember, forget
from sqlalchemy.exc import DBAPIError
from ..models import Stock
from ..models import Account
from ..sample_data import MOCK_DATA
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPBadRequest, HTTPUnauthorized
import requests
import json
from . import DB_ERR_MSG

@view_config(route_name='auth', renderer='../templates/login.jinja2', permission= )
def my_login_view(request):
    if request.method == 'GET':
        try:
            username = request.GET['username']
            password = request.GET['password']
 
        except KeyError:
            return {}
        
        is_authenticated = Account.check_credentials(request, username, password)
        if is_authenticated[0]:
            headers = remember(request, userid=instance.username)
            return HTTPFound(location=request.route_url('portfolio'), headers=headers)
        else:
            HTTPUnauthorized()

    return HTTPFound(location=request.route_url('home')   

    if request.method == 'POST':
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
        except KeyError:
            return HTTPBadRequest()

        try:
            instance = Account(
                username=username
                email=email
                password=password
            )

            headers = remember(request, userid=instance.username)
            request.dbsession.add(instance)

            return HTTPFound(location=request.route_url('stocks'), headers=headers)

    return HTTPNotFound()


@view_congig(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location=request.route_url('home'), headers=headers)
