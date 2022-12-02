from turtle import*

class Car:
    def__init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
        self.turtle = Turtle()
        self.turtle.shape("car.git")

    def drive(self):
        self.turtle.forword(self.speed)

    def left_turn(self):
        self.turtle.left(90)

register_shape("car.gif")
mycar = Car(200, "red", "E-class")
for i in range(100):
    myCar.drive()
    myCar.left_turn()
        
