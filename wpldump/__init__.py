try:
    from .version import version as __version__
except ImportError:
    __version__ = '0.0.0'

from .__main__ import run as _run