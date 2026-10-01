class ToolkitError(Exception):
    pass
class ValidationError(ToolkitError):
    pass
class ConversionError(ToolkitError):
    pass
class DivisionByZeroError(ValidationError):
    pass