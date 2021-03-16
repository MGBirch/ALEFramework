from controller import Supervisor, Emitter
class ALESuper():
    """docstring for ALESuper."""

    def __init__(self):
        super(ALESuper, self).__init__()
        self.robot = Supervisor()
        self.emitter = Emitter()

        emitter.setChannel(1)

    
