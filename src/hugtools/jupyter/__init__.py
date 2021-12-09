import json
from typing import Set


def get_all_notebook_imports(notebook_filename: str, verbose: bool = True) -> Set[str]:
    """Parse a jupyter notebook and look for imports that have been used and collate them together to help
    with keeping everything runnable from the top

    Args:
        notebook_filename (str): a path to a notebook file
        verbose (bool): whether to print to stdout

    Returns:
        set[str] : the import statements found deduplicated into a set

    """
    with open(notebook_filename) as f:
        ipynb = json.load(f)
    imports = []
    for cell in ipynb["cells"]:
        for line in cell["source"]:
            if line.startswith("import") or (line.startswith("from") and "import in line"):
                imports.append(line)
    if verbose:
        print("\n".join(imports))
    return set(imports)
