"""Logging with Python standard logger"""

import logging
logging.basicConfig()

# logging.debug("Debug message")
# logging.info("Info message")
# logging.warning("Warning message")
# logging.error("Error message")
# logging.critical("Critical message")

# LOGGING FROM A MODULE

log = logging.getLogger("trylog")
log.setLevel("DEBUG")
log.debug("Debug message")
log.info("Info message")
log.warning("Warning message")
log.error("Error message")
log.critical("Critical message")
