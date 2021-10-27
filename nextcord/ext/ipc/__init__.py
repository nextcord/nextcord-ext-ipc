import collections

from .client import Client
from .server import Server
from .errors import *


_VersionInfo = collections.namedtuple("_VersionInfo", "major minor micro release serial")

version = "2.1.1"
version_info = _VersionInfo(2, 1, 1, "final", 0)
