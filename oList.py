class oList:
    """
    oList Methods:\n
    .attach(data) # data type -> any\n
    .get_attachments(data) # returns: attachment data\n
    .as_tuple() # returns: list to tuple\n
    .as_dict(_attachments=True) # returns: dict by list index,\n
    \t\t_attachments will also add 'attachments': to the dict
    """

    def __init__(self, _list=[]):
        assert type(_list) is list, 'oList argument should be a list!'
        self.__list = _list
        self.__index = -1
        self.__data = []

    def __str__(self):
        return str(self.__list)

    def __repr__(self):
        return str(self.__list)

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index >= len(self.__list):
            self.__index = 0
            raise StopIteration
        return self.__list[self.__index]

    def pop(self, index):
        return self.__list.pop(index)

    def clear(self):
        return self.__list.clear()

    def append(self, _append):
        return self.__list.append(_append)

    def sort(self, *args, **kwargs):
        return self.__list.sort(*args, **kwargs)

    def reverse(self):
        return self.__list.reverse()

    def index(self, val, *args, **kwargs):
        return self.__list.index(val, *args, **kwargs)

    def insert(self, val, *args, **kwargs):
        return self.__list.insert(val, *args, **kwargs)

    def copy(self):
        return self.__list.copy()

    def count(self):
        return self.__list.count()

    def attach(self, data):
        """
        Attach data to the list object.
        Does not affect the lists' contents
        """
        self.__data.append(data)
        return self

    def get_attachments(self):
        if len(self.__data) == 1:
            return self.__data[0]  # type: any
        return self.__data  # type: list

    def as_dict(self, _attachments=False):
        _dict = {
        }
        for index, li in enumerate(self.__list):
            _dict[index] = li
        if _attachments:
            _dict['attachments'] = self.__data
        return _dict

    def as_tuple(self):
        return tuple(self.__list)
