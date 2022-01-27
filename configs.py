class Config():
    def __init__(self):
        self.remove_symbol = True
        self.remove_digits = False
        self.make_lower_case = False

        self.classfication_method = 'two-binary' # 'one-multi', 'two-binary'
        self.count_method = 'appear' # 'appear', 'sum'
        self.smoothing_method = 'laplace' # 'none', 'add_one', 'laplace'
        self.add_one_scale = 1.0

config = Config()