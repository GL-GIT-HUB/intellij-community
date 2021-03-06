import os
import sys

IS_PY36 = False
if sys.version_info[0] == 3 and sys.version_info[1] == 6:
    IS_PY36 = True

frame_eval_func = None
stop_frame_eval = None
set_use_code_extra = None

USE_FRAME_EVAL = os.environ.get('PYDEVD_USE_FRAME_EVAL', None)

if USE_FRAME_EVAL == 'NO':
    frame_eval_func, stop_frame_eval = None, None

else:
    if IS_PY36:
        try:
            from _pydevd_frame_eval.pydevd_frame_eval_cython_wrapper import frame_eval_func, stop_frame_eval, set_use_code_extra
        except ImportError:
            from _pydev_bundle.pydev_monkey import log_error_once

            dirname = os.path.dirname(os.path.dirname(__file__))
            log_error_once("warning: Debugger speedups using cython not found. Run '\"%s\" \"%s\" build_ext --inplace' to build." % (
                sys.executable, os.path.join(dirname, 'setup_cython.py')))
