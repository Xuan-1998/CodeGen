import io
import sys
import logging

logger = logging.getLogger("__name__")

def code_runner(code: str, input_str: str) -> str:
    sys.stdin = io.StringIO(input_str)
    sys.stdout = io.StringIO()

    try:
        # Execute the code
        exec(code)
    except Exception as e:
        # If any exception occurs, capture the error message
        output = str(e)
    else:
        # Get the output from standard output
        output = sys.stdout.getvalue()

    # Reset standard input and output
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__

    return output
