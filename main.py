import sys

from geocode import get_coord, geocode


def main():
    toponym_to_find = ' '.join(sys.argv[1:])
    if toponym_to_find:
        coord = get_coord(toponym_to_find)
        print(geocode(coord))


if __name__ == '__main__':
    main()
