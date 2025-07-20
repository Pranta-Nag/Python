class Students:

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    @staticmethod                       # change the function behavior, make it static
    def show_name():                    # not allow object parameter
        print("Welcome,")

    def show_mark(self):
        print("Your mark is: ",self.mark)

s1 = Students("Pranta Nag", 70)
s1.show_name()
s1.show_mark()

