# Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.

from abc import abstractmethod, ABC

class Laptop(ABC):

    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def __init__(self, name, screen, keyboard, touchpad, webcam, ports, dynamics):
        self.name = name
        self.screen1 = screen
        self.keyboard1 = keyboard
        self.touchpad1 = touchpad
        self.webcam1 = webcam
        self.ports1 = ports
        self.dynamics1 = dynamics

    def screen(self):
        print(f'{self.name} has a {self.screen1} screen')


    def keyboard(self):
        print(f'{self.name} has {self.keyboard1} keyboard ')


    def touchpad(self):
        print(f'{self.name} has {self.touchpad1} touchpad')


    def webcam(self):
        print(f'{self.name} has a webcam with {self.webcam1}')


    def ports(self):
        print(f'{self.name} has all needed ports: {self.ports1}')


    def dynamics(self):
        print(f'{self.name} has {self.dynamics1} dynamics')


hp_lap = HPLaptop('HP Laptop', '24"','mechanical','sensitive','18px','2-USB and 1-HDMI','enough loud')
hp_lap.screen()
hp_lap.keyboard()
hp_lap.touchpad()
hp_lap.webcam()
hp_lap.ports()
hp_lap.dynamics()
