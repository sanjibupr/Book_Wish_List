import os

from flask import render_template, request
from flask_restful import Resource


class IndexResource(Resource):
    """Sample Index resource. Not normally used"""

    def get(self):
        """main page"""
        # Generally, instrumenting your code in the resource class probably isn't what you want, but you may need
        # request locals or access to things like the request, you'll do that up here.  However, since these µservices
        # are stateless REST endpoints, it probably makes more sense to write your code in a functional paradigm unless
        # you have a reason to do it OO (which is totally fine and reasonable).  In either case, you'll probably want
        # to pop out of this class and put everything either in functions or classes outside of this one.  Generally
        # speaking, it'll make unit testing a lot easier, since you won't have to mock the REST portion.  We trust flask
        # to do the job we ask it to, so traditionally we don't do a lot of testing around it, and when we do, it takes
        # fewer resources to do those as integration tests.  Using the Resource classes allows us to break up the code
        # in a clean fashion and neatly namespace the functions that are called by flask.
        return cluster_hello()

def cluster_hello():
    cluster = os.environ.get('CLUSTER')
    if cluster is None:
        cluster = 'unknown'

    return f"Hello from the {cluster} cluster"
