import argparse
import sys
import test_script
import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("Argv: %s", sys.argv)

parser = argparse.ArgumentParser()
parser.add_argument("--script")
args, unknown = parser.parse_known_args()
script_name = args.script

logger.debug("Known Args %s Unknown Args %s", args, unknown)
if __name__ == '__main__':
    if script_name == 'test_script':
        logger.debug("Running test_script")
        test_script.main(unknown)