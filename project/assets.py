import imp
from pathlib import Path
from sys import stderr
from flask import current_app


# INFO: Blueprint name must be different from func name
def load_blueprints() -> None:
    """Loads all blueprints from blueprints/"""
    blueprints_path = Path().cwd().joinpath("project", "blueprints")

    for bp in blueprints_path.iterdir():
        bp = str(bp)

        if bp.endswith(".py"):
            bp_name = bp.split(".")[0].split("/")[-1:][0]
            module = imp.load_source(bp_name, str(blueprints_path.joinpath(bp)))
            current_app.register_blueprint(module.__getattribute__(bp_name))
            print(f" * Blueprint '{bp_name}' loaded", file=stderr)
