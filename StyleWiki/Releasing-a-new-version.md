## How to release a new version?

After developing a new version, the files have to be packed in an `.oxt` file. Such an extension is essentially a `.zip` file with altered extension.

We have a script called `release.py` in order to automate this process. Examples:

#### Releasing a version `0.0.3` for LibreOffice:

```bash
./release.py --LibreOffice 0.0.3
```

#### Releasing a version `0.0.3` for OpenOffice:

```bash
./release.py --OpenOffice 0.0.3
```

#### Changing the final filename:

```bash
./release.py --OpenOffice 0.0.3 -f awesome-release
```

#### Changing the source folder:

```bash
./release.py --OpenOffice 0.0.3 -s ../lo-page-numbering
```

`./release.py --help`:

```
usage: release.py [-h] [-L] [-O] [-s SOURCE] [-f FILENAME] version

Release a new version

positional arguments:
  version               version (e.g., 0.1.0)

optional arguments:
  -h, --help            show this help message and exit
  -L, --LibreOffice     for LibreOffice
  -O, --OpenOffice      for OpenOffice
  -s SOURCE, --source SOURCE
                        source folder
  -f FILENAME, --filename FILENAME
                        filename
```
