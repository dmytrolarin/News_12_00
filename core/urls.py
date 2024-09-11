import article_app
from .settings import project


article_app.article_app.add_url_rule(
    rule= "/",
    view_func= article_app.show_article_list
)
project.register_blueprint(blueprint= article_app.article_app)