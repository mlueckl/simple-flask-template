"""Python setup.py for package"""
from pathlib import Path
from setuptools import find_packages, setup


def read_requirements(path):
    return [line.strip() for line in Path(path).resolve().read_text().split("\n") if not line.startswith(('"', "#", "-", "git+"))]


project_name = Path("project").joinpath("NAME").resolve().read_text()
setup(
    name=project_name,
    version=Path("project").joinpath("VERSION").resolve().read_text(),
    description="project_description",
    url="https://github.com/author_name/project_urlname/",
    long_description=Path("README.md").resolve().read_text(),
    long_description_content_type="text/markdown",
    author="author_name",
    packages=find_packages(project_name),
    install_requires=read_requirements("requirements.txt"),
    entry_points={"console_scripts": [f"{project_name} = {project_name}.__main__:main"]},
)
