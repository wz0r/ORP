#!/usr/bin/env/python3


from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    return Response('Hello World!')


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 4000, application)