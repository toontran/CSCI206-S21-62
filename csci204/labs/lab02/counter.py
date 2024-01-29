'''CSCI 204 Lab 02 Class Design, Implementation, and Exceptions
Lab section: CSCI 204.L60, Thursday 1-2:52
Student name: Tung Tran
Instructor name: Professor Fuchsberger'''


class BasicCounter:

    def __init__(self, counted, the_initial_count):
        self._counted = counted
        self.the_initial_count = self.the_initial_count

    def count(self):
        self._counted += 1

    def un_count(self):
        self._counted -= 1

    def reset(self):
        self._counted = self.the_initial_count

    def set_count_to(self, new_counted):
        self._counted = new_counted

    def get_count_value(self):
        return self._counted


class LimitedCounter(BasicCounter):

    def __init__(self, DEFAULT_MIN, DEFAULT_MAX):
        self.DEFAULT_MIN = DEFAULT_MIN
        self.DEFAULT_MAX = DEFAULT_MAX
        self._counted = DEFAULT_MIN
        self.the_initial_count = DEFAULT_MIN
        
    def is_at_min(self):
        return self._counted == self.DEFAULT_MIN

    def is_at_max(self):
        return self._counted == self.DEFAULT_MAX

    def get_min(self):
        return self.DEFAULT_MIN

    def get_max(self):
        return self.DEFAULT_MAX


class StoppingCounter(LimitedCounter):

    def count(self):
        if self._counted >= self.DEFAULT_MAX:
            pass
        else:
            self._counted += 1

    def un_count(self):
        if self._counted <= self.DEFAULT_MIN:
            pass
        else:
            self._counted -= 1


class RollOverCounter(LimitedCounter):

    def count(self):
        if self._counted >= self.DEFAULT_MAX:
            self._counted = self.DEFAULT_MIN
        else:
            self._counted += 1

    def un_count(self):
        if self._counted <= self.DEFAULT_MIN:
            self._counted = self.DEFAULT_MAX
        else:
            self._counted -= 1


class CounterException(Exception):
    pass


class WarningCounter(LimitedCounter):

    def count(self):
        if self._counted >= self.DEFAULT_MAX:
            raise CounterException
        else:
            self._counted += 1

    def un_count(self):
        if self._counted <= self.DEFAULT_MIN:
            raise CounterException
        else:
            self._counted -= 1
