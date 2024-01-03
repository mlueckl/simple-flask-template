import imp
from pathlib import Path
from flask import current_app


# Blueprint name must be different from func names
# TODO: Add option to filter unwanted bp's
def load_blueprints() -> None:
    blueprints_path = Path().cwd().joinpath("project", "blueprints")

    for bp in blueprints_path.iterdir():
        bp = str(bp)

        if bp.endswith(".py"):
            bp_name = bp.split(".")[0].split("/")[-1:][0]
            module = imp.load_source(bp_name, str(blueprints_path.joinpath(bp)))
            current_app.register_blueprint(module.__getattribute__(bp_name))
