import logging
import argparse
import sys

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main(argv):
    logger.debug("Beginning test script")

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--stage")
    parser.add_argument("-w", "--write", action="store_true")

    args = parser.parse_args(argv)
    stage = args.stage
    write = args.write

    logger.debug("Running test script on stage: %s and write: %s", stage, write)

    logger.debug("Finished test script")


if __name__ == '__main__':
    main(sys.argv)
