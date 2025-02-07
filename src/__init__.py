from data_loader import DataLoader
from var import MyFiles, MyDirectories
from util import MyUtil
from jinja2 import FileSystemLoader, Environment

dl = DataLoader()
print(dl.data.site)

env = Environment(
    loader=FileSystemLoader(searchpath=MyDirectories.TEMPLATES)
)

html_template = env.get_template(MyFiles.Template.INDEX)
html = html_template.render(**dl.data.model_dump())

MyUtil.File.write(f"src/generated/index.html", html)