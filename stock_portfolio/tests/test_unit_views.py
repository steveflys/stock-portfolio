def test_default_behavior_of_base_route(dummy_request):
    from ..views.default import home_view
    from pyramid.response import Response

    request = dummy_request
    response = home_view(request)
    assert isinstance(response, Response)
