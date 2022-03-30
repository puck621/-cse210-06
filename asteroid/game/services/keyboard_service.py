import pyray

class KeyboardService:

    """A keyboard service inteface."""

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}

        self._keys['w'] = pyray.KEY_W
        self._keys['a'] = pyray.KEY_A
        self._keys['s'] = pyray.KEY_S
        self._keys['d'] = pyray.KEY_D

        self._keys['i'] = pyray.KEY_I
        self._keys['j'] = pyray.KEY_J
        self._keys['k'] = pyray.KEY_K
        self._keys['l'] = pyray.KEY_L

    def is_key_down(self, key):
        """Detects if the given key is being pressed.
        
        Args:
            key: A string containing the key value, e.g. 'a', '0', etc.

        Returns:
            True if the key is being pressed; false if otherwise.
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)
    
    def is_key_pressed(self, key):
        """Detects if the given key was pressed once.
        
        Args:
            key: A string containing the key value, e.g. 'a', '0', etc.

        Returns:
            True if the key was pressed once; false if otherwise.
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)
    
    def is_key_released(self, key):
        """Detects if the given key was released once.
        
        Args:
            key: A string containing the key value, e.g. 'a', '0', etc.

        Returns:
            True if the key was released once; false if otherwise.
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)
    
    def is_key_up(self, key):
        """Detects if the given key is released.
        
        Args:
            key: A string containing the key value, e.g. 'a', '0', etc.

        Returns:
            True if the key is released; false if otherwise.
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)