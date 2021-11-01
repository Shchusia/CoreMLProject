"""
cron function for make predict
"""
import sys
from pathlib import Path

# block for use files base directory in docker runner
directory = Path(__file__)
sys.path.insert(0, str(directory.parent.absolute().parent))

from apps import CONFIG, DICT_MODELS, LOGGER  # noqa


def main() -> None:
    """
    Function logic
    :return:
    """
    # args = sys.argv # optional args that you can supply when calling in docker file
    LOGGER.info("Started cron function %s for predict use lgbm", CONFIG.SERVICE_NAME)
    # extract data to predict
    DICT_MODELS["lgbm"].predict()
    # save predict
    LOGGER.info("Finished cron function %s for predict use lgbm", CONFIG.SERVICE_NAME)


if __name__ == "__main__":
    main()
