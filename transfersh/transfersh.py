from os.path import isfile, basename
from .abc_transfer import *

class TransferSh(TransferShABC):


    def uploadFile(file):
        if not isfile(file):
            raise FileNotExists('"{}" is not exists!'.format(file))

        # read file
        with open(file, 'rb') as f:
            return super(TransferSh, TransferSh).uploadBytes(f, basename(file))

    def uploadFromBinary(b, outputFilename):

        return super(TransferSh, TransferSh).uploadBytes(b, outputFilename)
