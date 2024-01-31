

from typing import Self, Type, Any, get_args, get_origin
from dataclasses import fields, is_dataclass


def is_list(field_type: Type):
    return get_origin(field_type) == list

def get_list_item_type(list_type: Type):
    args = get_args(list_type)
    if len(args) > 0:
        return args[0]
    return Any

def parse_item(raw_value: Any, field_type: Type) -> Any:
    if not isinstance(field_type, type):
        return raw_value
    elif issubclass(field_type, BaseResponseData):
        return field_type.from_data(raw_value)
    elif is_dataclass(field_type):
        return field_type(**raw_value)
    else:
        return raw_value


class BaseResponseData:

    @classmethod
    def from_data(cls, data) -> Self:
        parsed_data = {}
        for field in fields(cls):
            raw_value = data.get(field.name, None)
            if raw_value is None:
                parsed_data[field.name] = None
                continue
            if is_list(field.type):
                field_type = get_list_item_type(field.type)
                value = list(parse_item(it, field_type) for it in raw_value)
            else:
                value = parse_item(raw_value, field.type)
            parsed_data[field.name] = value

        return cls(**parsed_data)

    @classmethod
    def from_response_data(cls, response_data: dict) -> Self:
        success = response_data.get("status", "") == "ok"
        if not success:
            raise Exception("Response status is not ok")
        data = response_data.get("media", False)
        if not data:
            raise Exception("There is no media in response")
        return cls.from_data(data)
