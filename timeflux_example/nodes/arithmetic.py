"""Simple example nodes"""

from timeflux.core.node import Node

class Add(Node):

    """Adds ``value`` to each cell of the input.

    This is one of the simplest possible nodes.

    Attributes:
        i (Port): Default input, expects DataFrame.
        o (Port): Default output, provides DataFrame.

    Example:
        .. literalinclude:: /../test/graphs/test.yaml
           :language: yaml
    """

    def __init__(self, value):
        """
        Args:
            value (int): The value to add to each cell.
        """
        self._value = value

    def update(self):
        # Copy the input to the output
        self.o = self.i
        # Add the value to each cell
        self.o.data += self._value


class MatrixAdd(Node):

    """Sum two input matrices together.

    This node illustrates multiple named inputs.
    Note that it is not necessary to declare the ports. They will be created dynamically.

    Attributes:
        i_m1 (Port): First matrix, expects DataFrame.
        i_m2 (Port): Second matrix, expects DataFrame.
        o (Port): Default output, provides DataFrame.

    Example:
        .. literalinclude:: /../test/graphs/multi.yaml
           :language: yaml
    """

    def __init__(self):
        pass

    def update(self):
        self.o.data = self.i_m1.data + self.i_m2.data
