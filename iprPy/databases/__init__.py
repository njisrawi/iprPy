import os
import importlib

failed_databases = []

def __load_databases():
    databases_dict = {}
    names = []
    dir = os.path.dirname(__file__)

    for name in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, name)):
            names.append(name)
            
        elif os.path.isfile(os.path.join(dir, name)):
            name, ext = os.path.splitext(name)
            
            if ext.lower() in ('.py', '.pyc') and name != '__init__' and name not in names:
                names.append(name)
        
    for name in names:
        #if True:
        try:
            databases_dict[name] = importlib.import_module('.'+name, 'iprPy.databases')
        #else:
        except:
            failed_databases.append(name)

    return databases_dict

databases_dict = __load_databases()