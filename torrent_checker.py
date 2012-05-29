#!/usr/bin/env python
import os
import shutil
import sys
from pyrobase import bencode
from pyrocore.util import metafile

__version__ = '0.0.1'


def check_torrent(torrent_file, seed_dir):
    metainfo = bencode.bread(torrent_file)
    name = metainfo['info']['name']
    print name

    torrent = metafile.Metafile(torrent_file)
    path = os.path.join(seed_dir, name)
    try:
        success = torrent.check(metainfo, path, metafile.console_progress())
    except OSError:
        success = False
    dest_dir = os.path.join(os.path.dirname(torrent_file),
                            'success' if success else 'failure')

    if not os.path.isdir(dest_dir):
        os.mkdir(dest_dir)
    shutil.move(torrent_file, dest_dir)


def main():
    if len(sys.argv) != 3:
        print 'Usage: {} torrent_dir seed_dir'.format(
            os.path.basename(sys.argv[0]))
        sys.exit(1)

    for directory in sys.argv[1:]:
        if not os.path.isdir(directory):
            print '{!r} is not a directory'.format(directory)
            sys.exit(1)

    torrent_dir, seed_dir = sys.argv[1:]

    for torrent_file in [os.path.join(torrent_dir, x) for x in
                         os.listdir(torrent_dir) if x.endswith('.torrent')]:
        check_torrent(torrent_file, seed_dir)


if __name__ == '__main__':
    sys.exit(main())
