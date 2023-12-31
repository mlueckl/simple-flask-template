# Entry point, to not explicilty specify Flask app
from project.app import create_app

app = application = create_app()  # noqa
