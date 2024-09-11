import flask


article_app = flask.Blueprint(
    name = "article_app",
    import_name = "article_app",
    static_folder = "static", 
    template_folder = "templates",
    static_url_path = "/article_app/"
)