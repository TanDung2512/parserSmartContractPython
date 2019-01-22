class InvalidAmount(Exception):
    def __init__(self,s):
        self.message = "Current balance < " + str(s)