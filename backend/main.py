from url_registry import UrlRegistry
from url_dispatch_table import UrlDispatchTable


def main():
    print('(c) Sybit GmbH 2022')
    print('Launching...')
    registry = UrlRegistry()
    dispatch_table = UrlDispatchTable(registry)
    dispatch_table()
    return


if __name__ == "__main__":
    main()
