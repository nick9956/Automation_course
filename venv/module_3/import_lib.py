import importlib.util
from importlib.metadata import version
import sys
import prettytable
import itertools
import argparse
import logging

def get_package_path(package_name):

    error_message = 'Package not found'

    try:
        module_version = version(package_name)
        module_doc = sys.modules[package_name].__doc__
        module_parameters = importlib.util.find_spec(package_name)

        parser = argparse.ArgumentParser(description='This is a parser.')
        parser.add_argument("-c", "--console_log", dest="console_log",
                            choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                            help="Set the logging level for console",
                            default='INFO')
        parser.add_argument("-f", "--file_log", dest="file_log",
                            choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                            help="Set the logging level for file",
                            default='DEBUG')

        args = parser.parse_args()

        if args.console_log:
            console_loger = logging.getLogger('console loger')
            level = getattr(logging, args.console_log)
            console_loger.setLevel(level)
            console_loger.addHandler(logging.StreamHandler())
            if console_loger.level == 10:
                console_loger.debug(module_version)
            elif console_loger.level == 20:
                console_loger.info(module_parameters.submodule_search_locations)
            elif console_loger.level == 30:
                console_loger.warning(module_doc)

        if args.file_log:
            file_loger = logging.getLogger('console loger')
            file_level = getattr(logging, args.file_log)
            file_loger.setLevel(file_level)
            file_loger.addHandler(logging.FileHandler('info.log'))
            if file_loger.level == 10:
                file_loger.debug(module_version)
            elif file_loger.level == 20:
                file_loger.info(module_parameters.submodule_search_locations)
            elif file_loger.level == 30:
                file_loger.warning(module_doc)

        if module_parameters is None:
            if console_loger.level == 40:
                console_loger.error(error_message)
            elif file_loger.level == 40:
                file_loger.error(error_message)
        else:
            return module_parameters.submodule_search_locations
    except ModuleNotFoundError:
        logging.error(error_message)

get_package_path("prettytable")