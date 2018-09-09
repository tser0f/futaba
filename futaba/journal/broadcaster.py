#
# journal/broadcaster.py
#
# futaba - A Discord Mod bot for the Programming server
# Copyright (c) 2017 Jake Richardson, Ammon Smith, jackylam5
#
# futaba is available free of charge under the terms of the MIT
# License. You are free to redistribute and/or modify it under those
# terms. It is distributed in the hopes that it will be useful, but
# WITHOUT ANY WARRANTY. See the LICENSE file for more details.
#

import logging
from pathlib import PurePath

logger = logging.getLogger(__name__)

__all__ = [
    'Broadcaster',
]

class Broadcaster:
    __slots__ = (
        'router',
        'path',
    )

    def __init__(self, router, path):
        self.router = router
        self.path = PurePath(path)

    def send(self, subpath, content, attributes=None):
        # Get full path
        subpath = PurePath(subpath)
        assert not subpath.is_absolute, "Broadcasting on absolute subpath"
        path = self.path.joinpath(subpath)

        # Replace attributes if not passed
        attributes = attributes or {}

        # Queue up event
        logger.info("Sending journal entry to %s: '%s' %s", path, content, attributes)
        self.router.queue.put_nowait((path, content, attributes))
