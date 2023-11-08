from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        as_dict = toml.loads(content)
        infos = as_dict["tool"]["poetry"]
        name = infos["name"]
        description = infos["description"]
        dependencies = infos["dependencies"]
        dev_dependencies = infos["group"]["dev"]["dependencies"]
        license = infos["license"]
        authors = infos["authors"]


        return Project(name, description, dependencies, dev_dependencies, license, authors)
