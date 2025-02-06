
class MyVars:
    class Template:
        INDEX="base.html"
        
        @staticmethod
        def dir() -> str:
            return "src/templates/"
        
    class Data:
        CATEGORIES="src/data/categories.csv"
        ENTRIES="src/data/entries.csv"
        SITE="src/data/site.toml"