class FunctionCall:
    def __init__(self, fun_name, *fun_params):
        self.__fun_name = fun_name
        self.__fun_params = fun_params

    def call(self):
        return self.__fun_name(*self.__fun_params)

    def __call__(self, *args, **kwargs):
        return self.call()

    def get_fun_name(self):
        return self.__fun_name


class Operation:
    def __init__(self, fundo: FunctionCall, fredo: FunctionCall):
        self.__fundo = fundo
        self.__fredo = fredo

    def undo(self):
        return self.__fundo()  # <=> to self.__fundo.call()

    def redo(self):
        return self.__fredo()

    def get_undo_fun_name(self):
        return self.__fundo.get_fun_name()


class UndoServices:
    def __init__(self):
        # history of the program's operations
        self.__history = []
        self.__index = 0
        self.__redo_index = 0

    def record(self, operations: Operation):
        if self.__index == len(self.__history):
            self.__history.append(operations)
        else:
            self.__history[self.__index] = operations
        self.__index += 1
        self.__redo_index = 0

    def undo(self):
        if self.__index == 0:
            raise NoMoreUndosException("Cannot undo any more operations")

        self.__index -= 1
        self.__history[self.__index].undo()
        self.__redo_index += 1

        if self.__index >= 0 and "add_multiple_rentals" in str(self.__history[self.__index].get_undo_fun_name()):
            self.undo()

    def redo(self):
        if self.__redo_index == 0:
            raise NoMoreRedosException("Cannot redo any more operations")

        self.__history[self.__index].redo()
        self.__index += 1
        self.__redo_index -= 1

        if (self.__index < len(self.__history) and
            "add_multiple_rentals" in str(self.__history[self.__index].get_undo_fun_name())):
            self.redo()


class UndoError(Exception):
    def __init__(self, errors):
        self.__errors = errors

    def __str__(self):
        return "Undo exception: " + self.__errors


class NoMoreUndosException(UndoError):
    def __init__(self, errors):
        UndoError.__init__(self, errors)


class NoMoreRedosException(UndoError):
    def __init__(self, errors):
        UndoError.__init__(self, errors)
