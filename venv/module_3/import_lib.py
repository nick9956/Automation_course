import importlib.util
from importlib.metadata import version
import itertools
import argparse
import logging

def get_package_path(package_name):

    error_message = 'Package not found'

    try:
        module_version = version(package_name)
        #module_doc = sys.modules[package_name].__doc__
        module_parameters = importlib.util.find_spec(package_name)

        parser = argparse.ArgumentParser(description='This is a parser.')
        parser.add_argument("-l", "--log", dest="logLevel",
                            choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                            help="Set the logging level", default='INFO')

        handlers_list = [logging.FileHandler('info.log'),
                         logging.StreamHandler()]

        args = parser.parse_args()
        if args.logLevel:
            logging.basicConfig(level=getattr(logging, args.logLevel),
                                handlers=handlers_list)
            if args.logLevel == 'DEBUG':
                logging.debug(module_version)
            elif args.logLevel == 'INFO':
                logging.info(module_parameters.submodule_search_locations)
            elif args.logLevel == 'WARNING':
                logging.warning(module_doc)

        if module_parameters is None:
            logging.error(error_message)
        else:
            return module_parameters.submodule_search_locations
    except ModuleNotFoundError:
        logging.error(error_message)


get_package_path("prettytable")