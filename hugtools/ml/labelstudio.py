from zipfile import ZipFile
import json


def get_labelstudio_zip(zip_filename):
    with ZipFile(zip_filename) as z:
        try:
            with z.open("result.json") as result_json:
                result_dict = json.loads(result_json.read())
        except Exception as e:
            print(repr(e))
            raise
    return result_dict
