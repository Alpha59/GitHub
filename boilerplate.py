#!/usr/bin/env python3
import sys, tempfile, os
from subprocess import call

def create(name, desc, args_adder, run, console):
    class mod_call(object):
        def __call__(self, *args):
            if name == '__main__':
                # convert the first arg to a dictionary if
                # program is run from the command line
                return run(**vars(args[0]))
            else :
                # Convert all the args to arguments
                # if run as a module
                return run(*args)

    def main(func):
        # Read the arguements using argparse
        parser = argparse.ArgumentParser(description=desc)

        # Verbosity is always an option - however the amount of verbosity depends on the implementation of the run function
        parser.add_argument('-v', '--verbose', action='store_true', help="Adds verbosity to output messages")

        # Run the main function (Function is also accessible as module.exec())
        args_adder(parser)
        # Parse the arguments
        args = parser.parse_args()
        # Run the console function (the output) with or without verbosity.
        console(func(args), args.verbose)

    if name == '__main__':
        import argparse
        sys.exit(main(mod_call()))
    else :
        sys.modules[name] = mod_call()