import uuid

import pytest
from version import __version__


@pytest.mark.xfail(__version__ < "0.2.0", reason="not supported until v0.2.0")
def test_api():
    id_1 = uuid.uuid4().hex
    id_2 = uuid.uuid4().hex
    assert id_1 != id_2
