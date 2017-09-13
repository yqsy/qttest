import logging

log = logging.getLogger("MyModule")


def doIt():
    log.debug("Doin's stuff...")

    raise TypeError("Bogus type rrror for testing")

