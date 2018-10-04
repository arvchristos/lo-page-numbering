#!/usr/bin/env python3

import os
import zipfile
import argparse

def zipall(ob, path, rel=""):
    basename = os.path.basename(path)
    if os.path.isdir(path):
        if rel == "":
            rel = basename
        ob.write(path, os.path.join(rel))
        for root, dirs, files in os.walk(path):
            for d in dirs:
                zipall(ob, os.path.join(root, d), os.path.join(rel, d))
            for f in files:
                ob.write(os.path.join(root, f), os.path.join(rel, f))
            break
    elif os.path.isfile(path):
        ob.write(path, os.path.join(rel, basename))
    else:
        pass


def release(prefix, version, source, filename):
    release = version.replace('.', '_')
    release_dir = os.path.join(
        source,
        '{}/versions/{}'.format(prefix, release)
    )

    os.makedirs(release_dir, exist_ok=True)

    files_dir = os.path.join(
        source,
        '{}/python/oxt_metadata'.format(prefix)
    )
    oxt_file = '{}/{}.oxt'.format(release_dir, filename)

    with zipfile.ZipFile(oxt_file, "w") as oxt:
        for f in os.listdir(files_dir):
            zipall(oxt, os.path.join(files_dir, f))
    
    print('Release file available in {}'.format(oxt_file))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Release a new version')
    parser.add_argument('version', type=str, help='version (e.g., 0.1.0)')
    parser.add_argument('-L', '--LibreOffice', dest='is_libre', default=False,
                        action='store_true', help='for LibreOffice')
    parser.add_argument('-O', '--OpenOffice', dest='is_open', default=False,
                        action='store_true', help='for OpenOffice')
    parser.add_argument('-s', '--source', dest='source', default=os.getcwd(),
                        type=str, help='source folder')
    parser.add_argument('-f', '--filename', dest='filename', default='PageNumberingAddon',
                        type=str, help='filename')
    args = parser.parse_args()

    if args.is_open and args.is_libre:
        parser.error('--LibreOffice and --OpenOffice should not be used at the same time')
    
    prefix = ''
    if args.is_open:
        prefix = 'OpenOffice'
    if args.is_libre:
        prefix = 'LibreOffice'
    if prefix == '':
        parser.error('You should specify --LibreOffice or --OpenOffice')
    
    release(prefix, args.version, args.source, args.filename)