from importlib import util
from pathlib import Path
from types import ModuleType

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative_path: str) -> ModuleType:
    """Load a module from a relative path so we can import directories with special characters."""
    module_path = PROJECT_ROOT / relative_path
    spec = util.spec_from_file_location(name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module {name} from {module_path}")
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

