from Model import Model

class Post(Model):

    def __init__(self, row):
        # Todo:
        # Generate self.* from row selected from argo_fileheader_*
        # Will write it later
        self.dict = {}

    def __getattr__(self, name):
        try:
            return self.dict[name]
        except KeyError:
            pass

    def __setattr__(self, name, value):
        self.dict[name] = value

