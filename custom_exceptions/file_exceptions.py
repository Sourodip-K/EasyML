class TypeMismatchError(Exception):
    def __init__(self):
        self.message = "File type is mismatching!"
        super().__init__(self.message)