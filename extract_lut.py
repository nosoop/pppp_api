#!/usr/bin/python3

# just to avoid any issues with posting secrets, this script extracts the lookup table from
# an existing APK or libPPPP_API library

import pathlib
import tempfile
import hashlib
import mmap
import zipfile

# maps libpppp_api sha1 to an offset and size
# I'd prefer to statically analyze the binary to discover this but I can't into thumb
shared_object_table = {
    '718cd2b869a12fd304132271700fb5b79308aab3': (0x12228, 0x36),
}

def extract_lut(library):
    with open(library, 'rb') as f:
        bin = mmap.mmap(f.fileno(), length = 0, access = mmap.ACCESS_READ)
        bin.seek(0)
        
        sha1 = hashlib.sha1()
        while True:
            data = bin.read(65536)
            if not data:
                break
            sha1.update(data)
        
        offset, length = shared_object_table.get(sha1.hexdigest(), (None, None))
        if offset and length:
            bin.seek(offset)
            return bin.read(length)
    return None

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description = "Extracts the libPPPP_API lookup table from an APK or shared object.")
    parser.add_argument('binary', help = "Binary file to extract", type = pathlib.Path)
    
    args = parser.parse_args()
    
    lut = None
    if args.binary.suffix == '.apk':
        # extract libpppp
        with zipfile.ZipFile(args.binary, 'r') as archive, tempfile.TemporaryDirectory() as tmpdir:
            libfile = archive.extract('lib/armeabi/libPPPP_API.so', tmpdir)
            lut = extract_lut(libfile)
    else:
        lut = extract_lut(args.binary)
    
    if lut:
        print(*(format(byte, '02x') for byte in lut))
    else:
        print('Failed to locate lookup table.')
