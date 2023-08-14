

class Point:
    """A class representing a point"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
    def isPointInRectangle(self, lowerLeft, upperRight):
        """
        

        Parameters
        ----------
        lowerLeft : TYPE
            DESCRIPTION.
        upperRight : TYPE
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        if lowerLeft[0] < self.x < upperRight[0] \
        and lowerLeft[1] < self.y < upperRight[1]:
            return True
        else:
            return False