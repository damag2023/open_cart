import pytest


@pytest.mark.usefixtures("openBrowser")
class BaseClass:

    def openBrowser(self):
        pass