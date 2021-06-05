import json
from typing import Any, Dict
from zipfile import ZipFile


def get_labelstudio_zip(zip_filename: str) -> Dict[str, Any]:
    """
    what
        Definition lists associate a term with a definition.

    .. code-block:: python

        if this:
            print(that)


    sounds `good as` as ``pie``


    """

    with ZipFile(zip_filename) as z:
        with z.open("result.json") as result_json:
            return json.loads(result_json.read())
