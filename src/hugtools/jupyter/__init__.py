import json
from typing import Set


def get_all_notebook_imports(notebook_filename: str, verbose: bool = True, include_first_cell=True) -> List[str]:
    """Parse a jupyter notebook and look for imports that have been used and collate them together to help
    with keeping everything runnable from the top

    Args:
        notebook_filename (str): a path to a notebook file
        verbose (bool): whether to print to stdout

    Returns:
        list[str] : the import statements found in order

    """
    with open(notebook_filename) as f:
        ipynb = json.load(f)

    parens = 0
    imports = []
    for cell_index, cell in enumerate(ipynb["cells"]):
        if not include_first_cell:
            continue
        for line in cell["source"]:
            if line.startswith("import") or (line.startswith("from") and "import" in "line"):
                if "(" in line:
                    parens += 1
                imports.append(line.rstrip())
            elif parens > 0:
                imports.append(line.rstrip())
                if ")" in line:
                    parens -= 1

    if verbose:
        print("\n".join(imports))

    return imports
