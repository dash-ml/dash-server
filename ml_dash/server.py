from sanic import Sanic, views
from sanic_cors import CORS
from sanic_graphql import GraphQLView

from ml_dash.schema import schema

# to support HTTPS.
views.HTTP_METHODS += ('FETCH', 'OPTIONS')

app = Sanic("ml_dash.server")
# CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}}, automatic_options=True)

# NOTE: disable for laziness. Should enable it in the future.
# @app.listener('before_server_start')
# def init_graphql(app, loop):
#     app.add_route(GraphQLView.as_view(schema=schema, executor=AsyncioExecutor(loop=loop)), '/graphql')

# new graphQL endpoints
app.add_route(GraphQLView.as_view(schema=schema, graphiql=True), '/graphql',
              methods=['GET', 'POST', 'FETCH', 'OPTIONS'])
app.add_route(GraphQLView.as_view(schema=schema, batch=True), '/graphql/batch',
              methods=['GET', 'POST', 'FETCH', 'OPTIONS'])


@app.listener('before_server_start')
def setup_static(app, loop):
    from ml_dash import config
    from os.path import expanduser
    app.static('/files', expanduser(config.Args.logdir),
               use_modified_since=True, use_content_range=True, stream_large_files=True)


# note: currently disabled, file events API.
# from .file_events import file_events, setup_watch_queue
# app.add_route(file_events, '/file-events', methods=['GET', 'OPTIONS'])
# app.add_route(file_events, '/file-events/<file_path:path>', methods=['GET', 'OPTIONS'])
# app.listener('before_server_start')(setup_watch_queue)


def run(logdir=None, **kwargs):
    from ml_dash import config
    from termcolor import cprint

    if logdir:
        config.Args.logdir = logdir

    cprint("launched server with config:", "green")
    cprint("Args:", 'yellow')
    print(vars(config.Args))
    cprint("Sanic Server Args:", 'yellow')
    print(vars(config.ServerArgs))
    cprint("SSL Args:", 'yellow')
    print(vars(config.SSLArgs))

    config.ServerArgs.update(**kwargs)
    if config.SSLArgs.cert:
        app.run(**vars(config.ServerArgs), ssl=vars(config.SSLArgs))
    else:
        app.run(**vars(config.ServerArgs))


if __name__ == "__main__":
    # see: https://sanic.readthedocs.io/en/latest/sanic/deploying.html
    # call this as `python -m ml_logger.main`
    run()
