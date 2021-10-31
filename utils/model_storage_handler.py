class ModelStorageHandler:
    """
    class for working with data storage
    loading and unloading from repositories(LFS) hdfs etc

    this class knows how models are stored in the storage
    and which model to download / load
    """

    def __init__(self):
        """
        initialization of config connections, etc.
        """
        pass

    def download_model(self, *args, **kwargs):
        """
        function of downloading from storage
        unloads data based on input data
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def load_model(self, *args, **kwargs):
        """
        loads the model into repository
        :param args:
        :param kwargs:
        :return:
        """
        pass
