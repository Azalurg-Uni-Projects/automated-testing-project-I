import pytest
from assertpy import add_extension


def is_5(self):
    if self.val != 5:
        return self.error(f'{self.val} is NOT 5!')
    return self


@pytest.fixture(scope='module')
def my_extensions():
    add_extension(is_5)
