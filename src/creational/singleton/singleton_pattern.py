

class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, *kwargs)
        return cls._instance

    def __init__(self):
        self.theme = "Dark"
        self.fontSize = "18px"


if __name__ == '__main__':
    as1 = AppSettings()
    print(as1.theme, as1.fontSize)
