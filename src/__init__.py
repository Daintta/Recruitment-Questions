from data_loader import DataLoader
from var import MyVars
from util import MyUtil
from jinja2 import FileSystemLoader, Environment

dl = DataLoader()
print(dl.data.site)

env = Environment(
    loader=FileSystemLoader(searchpath=MyVars.Template.dir())
)

template = MyVars.Template.INDEX
html_template = env.get_template(template)
html = html_template.render(**dl.data.model_dump())

# print(html)

MyUtil.File.write(f"src/generated/index.html", html)