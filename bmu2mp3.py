#!/usr/bin/env python
import argparse

def argparsing():
    parser = argparse.ArgumentParser(description=
            "Converts Neverwinter Nights' BMU music file format to mp3 by stripping the header")
    parser.add_argument("-o", "--output-directory", help="directory to store the generated mp3s [default: current directory]", default=".")
    parser.add_argument("files", nargs='*', type=argparse.FileType('rb'))
    return (parser.parse_args(), parser)
class bmuconverter:
    def __init__(self,args):
        self.target_dir = args.output_directory
        self.files = args.files
        self.target_suffix = ".mp3"
        self.orig_suffix = ".bmu"
        self._bmu_prefix = "BMU V1.0".encode("ascii")
    def convert(self):
        for f in self.files:
            prefix = f.read(8)
            if prefix == self._bmu_prefix :
                targetf = self.targetfile(f)
                targetf.write(f.read())
                targetf.close()
            else:
                print f.name + " is not a BMU file! Not converting."
            f.close()
    def targetfile(self, orig):
        if orig.name[-len(self.orig_suffix):] == self.orig_suffix :
            fname = orig.name[:-len(self.orig_suffix)]
        else:
            fname = orig.name
        fname = self.target_dir + "/" + fname + self.target_suffix
        return open(fname , "wb")

if __name__ == "__main__" :
    args, parser = argparsing()
    if len(args.files) < 1 :
        parser.print_help()
    else :
        converter = bmuconverter(args)
        converter.convert()
