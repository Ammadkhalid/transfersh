from abc import ABCMeta, abstractmethod
from requests import post
from .exception import *

class TransferShABC(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def uploadBytes(file, output, domain = "https://transfer.sh"):
        req = post(domain, files={output: file})

        if req.ok:
            return req.text
        else:
            raise UnkownError('Status Code: {}\ncontent: {}'.format(req.status_code, req.text))
