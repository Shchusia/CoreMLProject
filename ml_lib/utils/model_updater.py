from pathlib import Path
from typing import Optional, Tuple, Type, Union

from ml_lib import MLModel


class ModelUpdater:
    def update_model(
        self, model_to_update: Type[MLModel], path_to_model: Union[str, Path]
    ) -> Tuple[bool, Optional[MLModel]]:
        """

        :param model_to_update:
        :param path_to_model:
        :return:
        """
        # get data to fit
        is_better = True
        new_model = model_to_update()
        old_model = model_to_update(path_to_model)  # type: ignore # noqa
        new_model.fit(
            # data to fit
        )
        # get data for validate
        # comparison of model scores

        if is_better:
            return is_better, new_model
        return False, None
