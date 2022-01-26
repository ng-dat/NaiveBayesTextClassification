class Config():
    def __init__(self):
        self.remove_symbol = True
        self.remove_digits = False
        self.make_lower_case = True

        self.classfication_method = 'one-multi' # 'one-multi', 'two-binary'
        self.count_method = 'appear' # 'appear', 'sum'
        self.smoothing_method = 'add_one' # 'none', 'add_one', 'laplace'

config = Config()