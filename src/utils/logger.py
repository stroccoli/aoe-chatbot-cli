import logging
import sys
from pathlib import Path
from src.config import LOG_LEVEL, LOG_FILE


formatter = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(LOG_LEVEL)
console_handler.setFormatter(formatter)

root_logger = logging.getLogger()
root_logger.setLevel(LOG_LEVEL)
root_logger.addHandler(console_handler)

def get_logger(name: str) -&gt; logging.Logger:
    return logging.getLogger(name)

# sample usage
if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.info("Logger initialized successfully")
