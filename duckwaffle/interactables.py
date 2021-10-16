class Interactable:
    """
    Interactables are objects ingame which can be interacted with.


    Parameters
    ==========       
    ia_is_gettable : bool
        Check if item can be picked up

    iacombine : dict 
        pairs of interactable and associated function

    iadescribe : str
        description while looking at the object

    iastate : bool
        the state an object is in e.g. doors closed/open

    iavalue : int, optional 
        The value or number of objects 

        Default to None
    """

    def __init__(self, ia_is_gettable, iacombine, iadescribe, iastate, iavalue=None):
        self.is_gettable = ia_is_gettable
        self.iacombine = iacombine
        self.iadescribe = iadescribe
        self.iastate = iastate
        self.iavalue = iavalue

    def __str__(self):
        return self.iadescribe
