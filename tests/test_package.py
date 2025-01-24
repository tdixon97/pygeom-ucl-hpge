from __future__ import annotations

import pytest

from pygeom_ucl_hpge.core import construct_hpge


def test_import():
    with pytest.raises(NotImplementedError):
        construct_hpge({})
