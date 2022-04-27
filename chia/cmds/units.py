from typing import Dict

# The rest of the codebase uses mojos everywhere.
# Only use these units for user facing interfaces.
units: Dict[str, int] = {
    "chia": 10 ** 8,  # 1 chives (XCC) is 100,000,000 mojo (100 million)
    "mojo": 1,
    "cat": 10 ** 5,  # 1 cat coin is 100,000 CAT mojos
}
