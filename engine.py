class Value:
    def __init__(self, data, _children=(), _op='', label=''):
        self.data = data
        self._prev = set(_children)
        self._op = _op
        self.label = label

    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), _op='+')
        return out

    def __sub__(self, other):
        out = Value(self.data - other.data, (self, other), _op='-')
        return out

    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), _op='*')
        return out

    def relu(self):
        out = Value(self.data if self.data > 0 else 0, (self,), _op="ReLU")
        return out

    def __repr__(self):
        return (f"Value(data={self.data}, label={self.label})")