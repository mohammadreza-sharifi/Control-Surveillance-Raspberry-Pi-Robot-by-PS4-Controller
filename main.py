from pyPS4Controller.controller import Controller
import RPi.GPIO as io
from picamera import PiCamera

camera = PiCamera()

#define driver pins
in1 = 3
in2 = 5
in3 = 8
in4 = 10

#buzzer pin
buzz = 12

io.setmode(io.BOARD)
io.setwarnings(False)
io.setup(in1,io.OUT)
io.setup(in2,io.OUT)
io.setup(in3,io.OUT)
io.setup(in4,io.OUT)
io.setup(buzz,io.OUT)
    
class MyController(Controller):
    
    
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

	#move the robot forward
    def on_up_arrow_press(self):
        io.output(in1,1)
        io.output(in2,0)
        io.output(in3,1)
        io.output(in4,0)
        
	#stop the robot	
    def on_up_down_arrow_release(self):
        io.output(in1,0)
        io.output(in2,0)
        io.output(in3,0)
        io.output(in4,0)
        
	#move the robot backward
    def on_down_arrow_press(self):
        io.output(in1,0)
        io.output(in2,1)
        io.output(in3,0)
        io.output(in4,1)
        
	#move the robot right
    def on_right_arrow_press(self):
        io.output(in1,1)
        io.output(in2,0)
        io.output(in3,0)
        io.output(in4,0)
        
	#stop the robot
    def on_left_right_arrow_release(self):
        io.output(in1,0)
        io.output(in2,0)
        io.output(in3,0)
        io.output(in4,0)
        
	#move the robot left
    def on_left_arrow_press(self):
        io.output(in1,0)
        io.output(in2,0)
        io.output(in3,1)
        io.output(in4,0)

    def on_circle_press(self):
        camera.start_preview()
        
    def on_x_press(self):
        io.output(buzz,1)
        
    def on_x_release(self):
        io.output(buzz,0)

    #def on_triangle_press(self):
        #camera.stop_preview()
    
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)
