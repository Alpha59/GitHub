#!/usr/bin/env python3
import sys, os
sys.path.append(os.getcwd())

desc = "Opens the default editor with a specified message"

def args_adder(parser):
    parser.add_argument('initial_message', type=str,default="", help="Name of the PR branch to review")

def run(initial_message, verbose):
    import ghCommands as gitHub
    import gitCommands as git
    import sys, os, tempfile
    from subprocess import call
    EDITOR = os.environ.get('EDITOR','vim') #that easy!
    cwd = os.getcwd().split("/")[-1]
    with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
        tf.write(initial_message)
        tf.flush()
        call([EDITOR, tf.name])

        tf.seek(0)
        return tf.read()

def console(output, verbose):
    print(output)

#########################################################################
# Boiler plate code to create a new module / command line module to be used.
#########################################################################
import boilerplate
boilerplate.create(__name__, desc, args_adder, run, console)
