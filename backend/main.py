import logging.config

from app import app


def main():
    logging.config.fileConfig('logging.conf')
    logging.info('(c) Sybit GmbH 2022')
    logging.info('Launching...')

    app.run(debug=True)
    return


if __name__ == "__main__":
    main()
