def generate_joints():
    """
    Signals that the object should accept its physical state from game.
    """
    pass

def reset_state_selection():
    """
    Signals that physics state must be reset on the selected objects.
    """
    pass

def set_physics_tool():
    """
    Turns on physics tool mode (Ctrl/Shift modify)
    """
    pass

def reset_state(arg1):
    """
    Signals that physics state must be reset on the object.
    
    :param str arg1:
    """
    pass

def get_state_selection():
    """
    Signals that the object should accept its physical state from game.
    """
    pass

def step():
    """
    Do a single physics step ('>' in game mode)
    """
    pass

def get_state(arg1):
    """
    Signals that the object should accept its physical state from game.
    
    :param str arg1:
    """
    pass

def single_step():
    """
    Toggle single-step mode in physics ('<' in game mode)
    """
    pass

def simulate_selection():
    """
    Applies the physics simulation to the selected objects.
    """
    pass

def simulate_objects():
    """
    Applies the physics simulation.
    """
    pass

