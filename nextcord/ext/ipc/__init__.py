import collections

from nextcord.ext.ipc.client import Client
from nextcord.ext.ipc.server import Server
from nextcord.ext.ipc.errors import *


_VersionInfo = collections.namedtuple("_VersionInfo", "major minor micro release serial")

version = "1.0.0"
version_info = _VersionInfo(1, 0, 0, "final", 0)
