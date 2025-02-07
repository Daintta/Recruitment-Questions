
class MyDirectories:
    GENERATED="src/generated/"
    TEMPLATES="src/templates/"
    DATA="src/data/"

class MyFiles:
    class Generated:
        INDEX=f"{MyDirectories.GENERATED}index.html"

    class Template:
        INDEX="base.html"
        
    class Data:
        CATEGORIES=f"{MyDirectories.DATA}categories.csv"
        ENTRIES=f"{MyDirectories.DATA}entries.csv"
        SITE=f"{MyDirectories.DATA}site.toml"