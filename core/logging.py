import logging
from config.settings import LOGGING_LEVEL

# Configure logging format and level
logging.basicConfig(
    level=LOGGING_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

def get_logger(module_name):
    """
    Create a logger for the specified module.
    
    Args:
        module_name: The name of the module for which the logger is being created.
    
    Returns:
        Logger object.
    """
    return logging.getLogger(module_name)
