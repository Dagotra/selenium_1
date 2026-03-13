import logging

def setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format="%(asctime) | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
    )