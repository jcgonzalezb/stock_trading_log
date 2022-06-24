class Validator:

    @staticmethod
    def validate_nonempty(*args):
        validate = True

        for arg in args:
            if isinstance(arg, str):
                if arg == '':
                    validate = False
            elif isinstance(arg, int):
                if arg == -1:
                    validate = False
            elif isinstance(arg, list):
                if not arg:
                    validate = False
            elif isinstance(arg, dict):
                if not arg:
                    validate = False

        return validate
