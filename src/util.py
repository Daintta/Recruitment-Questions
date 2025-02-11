import toml
import csv

class MyUtil:
    class File:

        @staticmethod
        def read_csv(path) -> list | None:
            try:
                with open(path, "r") as f:
                    rows = []
                    reader = csv.reader(f)
                    next(reader)
                    for r in reader:
                        rows.append(r)
                    return rows
            except Exception as e:
                print(e)
                return None

        @staticmethod
        def read_toml(path) -> dict | None:
            try:
                with open(path, "r") as f:
                    return toml.load(f)
            except Exception as e:
                print(e)
                return None

        @staticmethod
        def write(path, contents):
            try:
                with open(path, "w") as f:
                    f.write(contents)
            except Exception as e:
                print(e)
