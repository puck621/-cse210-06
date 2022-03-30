class Border_Service:
    
    def has_collided(self, subject, agent):
        """Whether or not the given subject has collided
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_above(self, subject, agent):
        """Whether or not the given subject is above
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_below(self, subject, agent):
        """Whether or not the given subject is below
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_left_of(self, subject, agent):
        """Whether or not the given subject is to the left
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_right_of(self, subject, agent):
        """Whether or not the given subject is to the right
        """
        raise NotImplementedError("not implemented in base class")