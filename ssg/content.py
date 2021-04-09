import re
from collections.abc import Mapping
from yaml import FullLoader, load


class Content(Mapping):
    __delimiter = r'^(?:-|\+){3}\s*$'
    __regex = re.compile(__delimiter, re.MULTILINE)

    def __init__(self, metadata, content):
        super().__init__()
        self.data = metadata
        self.data['content'] = content

    def __repr__(self):
        data = {}
        for key, value in self.data.items():
            if key != 'content':
                data[key] = value
        return str(data)

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return self.data.__iter__()

    def __len__(self):
        return len(self.data)

    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata, content)

    @property
    def body(self):
        return self.data['content']

    @property
    def type(self):
        return self.data['type'] if 'type' in self.data else None

    @type.setter
    def type(self, type):
        self.data['type'] = type

    '''
    11
Content representation

The final custom method that we will implement is the __repr__() method. It will create a custom representation of self.data. Create a __repr__() method, and on the first line create an empty dictionary called data. Return a call to str(), passing in data.
12
Removing content from the representation

We would like the custom representation to include only certain values. Loop through self.data.items() with a for loop. The current key should be called key, and the value should be value. In the for loop, test if key is not equal to "content". In the if, assign the value to data[key].
    '''
