from tqdm import tqdm


class PlaylistConverterException(Exception):
    def __init__(self, msg: str, tb=None):
        self.message = 'ERROR: ' + msg
        self.traceback = tb

        super(PlaylistConverterException, self).__init__(self.message)


class MissingEnvironmentVariableException(PlaylistConverterException):
    def __init__(self):
        super(MissingEnvironmentVariableException, self).__init__()


class ProgressBarHandler:
    def __init__(self):
        self._active_instance = None

    def create(self,
               total: int,
               description: str = '',
               postfix: dict = None,
               unit: str = '',
               ncols: int = 150):
        self._active_instance = tqdm(
            total=total,
            desc=description.ljust(49)[:49] + ']',
            postfix=postfix,
            unit=unit,
            ncols=ncols,
            dynamic_ncols=False)

    def update(self, increment: int, description: str = None, postfix: dict = None):
        if description is not None:
            self._active_instance.set_description(description.ljust(49)[:50] + ']')
        if postfix is not None:
            self._active_instance.set_postfix(postfix)

        self._active_instance.update(increment)

    def close(self):
        self._active_instance.close()

    def set_description(self, text: str):
        self._active_instance.set_description(text)

    def print_message(self, message: str):
        self._active_instance.write(message)


global progress_bar_handler
progress_bar_handler = ProgressBarHandler()

