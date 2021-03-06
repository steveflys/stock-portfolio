def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=None)
    config.add_route('home', '/')
    config.add_route('auth', '/auth')
    config.add_route('portfolio', '/portfolio')
    config.add_route('detail', '/portfolio/{symbol}')
    config.add_route('add', '/add')
    config.add_route('logout', '/logout')
