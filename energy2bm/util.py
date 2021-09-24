import numpy as np

from energy2bm import log


def positive_int(value):
    """Convert *value* to an integer and make sure it is positive."""
    result = int(value)
    if result < 0:
        raise argparse.ArgumentTypeError('Only positive integers are allowed')

    return result

def yes_or_no(question):
    answer = str(input(question + " (Y/N): ")).lower().strip()
    while not(answer == "y" or answer == "yes" or answer == "n" or answer == "no"):
        log.warning("Input yes or no")
        answer = str(input(question + "(Y/N): ")).lower().strip()
    if answer[0] == "y":
        return True
    else:
        return False

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    value = "{0:4.3f}".format(array[idx])
    return value