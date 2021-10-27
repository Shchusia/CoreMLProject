from unittest import TestCase

from ml_lib.config import MLConfig
from ml_lib.utils import get_object_config


class InvalidSubclassConfig(object):
    """
    class for test
    """

    pass


class ValidSubclassConfig(MLConfig):
    """
    class for test
    """

    pass


class TestGetConfigClass(TestCase):
    """
    Test correct work
    """

    def SetUp(self):
        pass

    def test_empty_config_class(self):
        config = get_object_config()
        self.assertEqual(config.__class__.__name__, MLConfig.__name__)
        config = get_object_config(None)
        self.assertEqual(config.__class__.__name__, MLConfig.__name__)

    def test_base_config_class(self):
        config = get_object_config(MLConfig)
        self.assertEqual(config.__class__.__name__, MLConfig.__name__)
        config = get_object_config(MLConfig())
        self.assertEqual(config.__class__.__name__, MLConfig.__name__)

    def test_sub_config_class(self):
        self.assertTrue(issubclass(ValidSubclassConfig, MLConfig))
        config = get_object_config(ValidSubclassConfig)
        self.assertEqual(config.__class__.__name__, ValidSubclassConfig.__name__)
        config = get_object_config(ValidSubclassConfig())
        self.assertEqual(config.__class__.__name__, ValidSubclassConfig.__name__)

    def test_invalid_config_class(self):
        self.assertFalse(issubclass(InvalidSubclassConfig, MLConfig))
        config = get_object_config(InvalidSubclassConfig)
        self.assertEqual(config.__class__.__name__, MLConfig.__name__)
        config = get_object_config(InvalidSubclassConfig())
        self.assertEqual(config.__class__.__name__, MLConfig.__name__)
