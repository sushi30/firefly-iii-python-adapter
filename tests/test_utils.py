from utils import map_jsonpath


def test_convert_json():
    source = {"string": "a", "int": 2, "array": [1, 2], "object": {"nested": "value"}}
    mapping = {
        "mapped_string": "string",
        "mapped_array": "array",
        "mapped_array_first_index": "array[0]",
        "mapped_object": "object.nested",
    }
    res = map_jsonpath(source, mapping)
    assert res == {
        "mapped_object": "value",
        "mapped_array_first_index": 1,
        "mapped_array": [1, 2],
        "mapped_string": "a",
    }
