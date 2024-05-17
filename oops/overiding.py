
class Demo:
    def display(self):
        print("Demo class display calling")


class Sample(Demo):
    def display(self):
        print("Sample calss display calling")



s = Sample()
s.display()