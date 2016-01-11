with warnings.catch_warnings():
    try:
        from IPython.utils.shimmodule import ShimWarning
        warnings.filterwarnings('error', '', ShimWarning)
    except ImportError:
        class ShimWarning(Warning):
            """Warning issued by IPython 4.x regarding deprecated API."""
            pass

    try:
        # IPython 3
        from IPython.config import Config
        from IPython.kernel import KernelManager
        from IPython.nbconvert.exporters.html import HTMLExporter
        from IPython.nbformat import \
            convert, current_nbformat, reads, write, NBFormatError, NotebookNode
    except ShimWarning:
        # IPython 4
        from traitlets.config import Config
        from jupyter_client import KernelManager
        from nbconvert.exporters.html import HTMLExporter
        from nbformat import \
            convert, current_nbformat, reads, write, NBFormatError, NotebookNode
    except ImportError:
        # IPython 2
        from IPython.config import Config
        from IPython.kernel import KernelManager
        from IPython.nbconvert.exporters.html import HTMLExporter
        from IPython.nbformat.current import \
            convert, current_nbformat, reads, write, NBFormatError, NotebookNode
    finally:
        warnings.resetwarnings()
