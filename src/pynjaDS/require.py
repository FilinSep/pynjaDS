import os
import importlib

import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

class WrongPath(Exception):
    def __str__(self) -> str:
        return "require: Wrong extension path"

class WrongExtension(Exception):
    def __str__(self) -> str:
        return "require: Wrong extension"

class WrongExtensionInitStructure(Exception):
    def __str__(self) -> str:
        return "require: Wrong extension init structure"

class WrongImportItem(Exception):
    def __str__(self) -> str:
        return "require: Wrong import item"

def require(ext: str, item: str = "all"):
    i = None
    try: 
        i = importlib.import_module("extensions."+ext)
    except:
        raise WrongPath()
    
    try: 
        ini = i._iinit
    except:
        raise WrongExtension() 
    
    if item == "all":
        try:
            if len(i._iinit.keys()) == 1:
                ks = list(i._iinit.keys())
                return i._iinit[ks[0]]
        except Exception:
            raise WrongExtensionInitStructure
        return i._iinit
    
    if item in i._iinit:
        try:
            return i._iinit[item]
        except:
            raise WrongExtensionInitStructure()
    else:
        raise WrongImportItem()
