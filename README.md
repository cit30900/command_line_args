# Python Command Line Arguments
Demo code that shows how to collect arguments from the command line.

* [index_sysargv.py](index_sysargv.py): Uses the `sys.argv` list to collect ordered but unlabeled arguments
    * Execute with the command `python index_sysargv.py alpha beta gamma delta`
* [index_argparse.py](index_argparse.py): Uses the `argparse` module to request, require, and parse arguments (and add help functionality to your program)
    * Execute with the command `python index_argparse.py -f John -l Doe`