from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Route, WebSocketRoute
from strawberry.asgi import GraphQL

from api.graphql import Mutation, Query, schema
from api.routes import homepage

graphql_app = CORSMiddleware(
    app=GraphQL(schema, debug=True),
    allow_origins=["*"],
    allow_methods=("GET", "POST", "OPTIONS"),
    allow_headers=[
        "access-control-allow-origin",
        "authorization",
        "content-type",
    ],
)

middlewares = [
    Middleware(
        CORSMiddleware, allow_origins=["*"],
        allow_methods=("GET", "POST", "OPTIONS"),
        allow_headers=[
            "access-control-allow-origin",
            "authorization",
            "content-type",
        ],
    ),
]

routes = [
    Route("/graphql", graphql_app),
    Route("/", homepage),
]

app = Starlette(debug=True, routes=routes, middleware=middlewares)
