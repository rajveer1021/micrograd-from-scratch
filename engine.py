class Value:
    def __init__(self, data, label=''):
        self.data = data
        self.label = label

    def __repr__(self):
        return (f"Value(data={self.data}, label={self.label})")