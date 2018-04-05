from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response, FileResponse


def basic_view(request):
    """basic home view sends a 200 OK response"""
    return Response('Hello World')


def json_view(request):

    return {'content': 'Hello World'}


def html_view(request):

    return FileResponse('./base.html', content_type='text/html')


if __name__ == '__main__':
    """set up a config object to work with"""
    config = Configurator

    """define routes"""
    config.add_route('basic', '/')
    config.add_route('json', '/')
    config.add_route('html', '/')

    config.add_view(basic_view, route_name='basic')
    config.add_view(json_view, route_name='json', renderer='json')
    config.add_view(html_view, route_name='home')

    app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 6543, app)

    server.serve_forever()



