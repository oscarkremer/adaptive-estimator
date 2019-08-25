import sys

REQUIRED_MAJOR = 3


def main():
    system_major = sys.version_info.major

    if system_major != REQUIRED_MAJOR:
        raise TypeError(
            "This project requires Python {}. Found: Python {}".format(
                required_major, sys.version))

    if not has_conda():
        raise TypeError(
            "This project requires Anaconda, please install from it's source.")

    print("---> Development environment passes all tests!")


def has_conda():
    try:
        import conda
    except BaseException:
        return False
    else:
        return True


if __name__ == '__main__':
    main()
