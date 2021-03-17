import importlib.util
from importlib.metadata import version
import logging

def get_package_path(package_name):

    logging.basicConfig(filename= 'info.log', level=logging.DEBUG)

    error = 'Package not found'
    try:
        package_name = importlib.util.find_spec(package_name)

        if package_name is None:
            print(error)
        else:
            logging.warning(package_name.__doc__)
            logging.info(package_name.submodule_search_locations)
            #logging.debug(version(package_name))

            return package_name.submodule_search_locations
    except ModuleNotFoundError:
        logging.error(error)


    #print(import_module)
    #return package_path

print(get_package_path('test'))