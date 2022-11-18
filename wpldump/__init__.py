try:
    from .version import version as __version__
except ImportError:
    __version__ = '0.0.0'
from .wpldump import _run, WplParser, wav_data
