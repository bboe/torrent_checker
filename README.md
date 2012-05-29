# torrent_checker

## Installation

First download
([tar.gz](https://github.com/bboe/torrent_checker/tarball/master),
[zip](https://github.com/bboe/torrent_checker/zipball/master)) and extract or
clone (`git clone https://github.com/bboe/torrent_checker.git`) this
repository.

Then install via:

    python setup.py install

## Running the program

After installation you should have access to `torrent_checker` on your path.
Simply run via:

    torrent_checker torrent_dir seed_dir

Where `torrent_dir` is a directory that contains torrent files and `seed_dir`
is a directory that contains the files you've downloaded. After torrent_checker
runs `torrent_dir` will have two new subdirectories, `failed` and
`success`. The `failed` subdirectory will contain all torrent files whose
contents either could not be found or could not be 100% verified and `success`
contains the remainder.
