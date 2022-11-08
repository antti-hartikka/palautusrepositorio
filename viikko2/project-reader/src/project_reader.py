from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        content_dict = toml.loads(content)
        poetry = content_dict["tool"]["poetry"]
        name = poetry["name"]
        desc = poetry["description"]
        dependencies = poetry["dependencies"]
        dev_dependencies = poetry["dev-dependencies"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, dependencies, dev_dependencies)
