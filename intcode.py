import attr
import numpy as np

@attr.s(auto_attribs=True)
class Intcode:
    opcodes: list
    instruction_pointer: int = attr.ib(default=0)
    user_input: list = attr.ib(factory=list)
    _jumped: bool = attr.ib(default=False)
    
    @classmethod
    def from_file(cls, path, *args, **kwargs):
        """Initialize an instance from a textfile."""
        opcodes = np.loadtxt(path, dtype=int, delimiter=",")
        return cls(opcodes=opcodes, *args, **kwargs)
    
    @property
    def opcode_string(self):
        """Represent opcode as a 5 character string.
        
        The full opcode can always be represented as a combination of 5 digits, e.g.
        
            ABCDE
             1002

            DE - two-digit opcode,      02 == opcode 2
             C - mode of 1st parameter,  0 == position mode
             B - mode of 2nd parameter,  1 == immediate mode
             A - mode of 3rd parameter,  0 == position mode
        
        Leading zeros can be omitted.
        
        Returns
        -------
        str
            String containing full opcode, including leading zeros.
        """
        return f"{self.opcodes[self.instruction_pointer]:05d}"
    
    @property
    def opcode(self):
        """Return the opcode for the current instruction."""
        return int(self.opcode_string[-2:])
    
    @property
    def modes(self):
        """Return the modes for the current instruction."""
        return tuple(int(m) for m in self.opcode_string[2::-1])
    
    @property
    def length(self):
        """Get the length of the current instruction."""
        length_map = {
            1: 4,
            2: 4,
            3: 2,
            4: 2,
            5: 3,
            6: 3,
            7: 4,
            8: 4,
            99: 1,
        }
        return length_map[self.opcode]
    
    @property
    def instruction(self):
        """Return the current instruction."""
        start = self.instruction_pointer
        return self.opcodes[start:start + self.length]
    
    def parameter(self, idx):
        """Return parameter value for current instruction."""
        if self.modes[idx - 1]:
            return self.instruction[idx]
        else:
            return self.opcodes[self.instruction[idx]]
        
    def initialize_memory(self, noun, verb):
        self.opcodes[1:3] = [noun, verb]
    
    def add(self):
        self.opcodes[self.instruction[-1]] = self.parameter(1) + self.parameter(2)
    
    def multiply(self):
        self.opcodes[self.instruction[-1]] = self.parameter(1) * self.parameter(2)
    
    def get_input(self):
        if not self.user_input:
            self.opcodes[self.instruction[-1]] = int(input('Input: '))
        else:
            self.opcodes[self.instruction[-1]] = self.user_input.pop(0)
    
    def jump_if_true(self):
        if self.parameter(1):
            self.instruction_pointer = self.parameter(2)
            self.jumped = True
    
    def jump_if_false(self):
        if not self.parameter(1):
            self.instruction_pointer = self.parameter(2)
            self.jumped = True
    
    def less_than(self):
        comparison = self.parameter(1) < self.parameter(2)
        self.opcodes[self.instruction[-1]] = int(comparison)
    
    def equals(self):
        comparison = self.parameter(1) == self.parameter(2)
        self.opcodes[self.instruction[-1]] = int(comparison)
    
    def execute(self):
        output = []
        operate = True
        while operate:
            self.jumped = False
            if self.opcode == 1:
                self.add()
            elif self.opcode == 2:
                self.multiply()
            elif self.opcode == 3:
                self.get_input()
            elif self.opcode == 4:
                output.append(self.parameter(1))
            elif self.opcode == 5:
                self.jump_if_true()
            elif self.opcode == 6:
                self.jump_if_false()
            elif self.opcode == 7:
                self.less_than()
            elif self.opcode == 8:
                self.equals()
            else:
                operate = False
            if not self.jumped:
                self.instruction_pointer += self.length
        return output
