# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.2, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_2 import models

class ArrayConnectionPath(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'destination': 'str',
        'remote': 'FixedReferenceNoResourceType',
        'source': 'str',
        'status': 'str',
        'status_details': 'str'
    }

    attribute_map = {
        'id': 'id',
        'destination': 'destination',
        'remote': 'remote',
        'source': 'source',
        'status': 'status',
        'status_details': 'status_details'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        destination=None,  # type: str
        remote=None,  # type: models.FixedReferenceNoResourceType
        source=None,  # type: str
        status=None,  # type: str
        status_details=None,  # type: str
    ):
        """
        Keyword args:
            id (str): A non-modifiable, globally unique ID chosen by the system.
            destination (str): IP address with the port of the target array.
            remote (FixedReferenceNoResourceType): The remote array.
            source (str): IP address of the source array.
            status (str): Status of the connection. Valid values are `connected` and `connecting`. `connected` - The connection is OK. `connecting` - No connection exists and the array is trying to reconnect.
            status_details (str): Additional information describing any issues encountered when connecting, or `null` if the `status` is `connected`.
        """
        if id is not None:
            self.id = id
        if destination is not None:
            self.destination = destination
        if remote is not None:
            self.remote = remote
        if source is not None:
            self.source = source
        if status is not None:
            self.status = status
        if status_details is not None:
            self.status_details = status_details

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ArrayConnectionPath`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            return None
        else:
            return value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, list):
                    result[attr] = list(map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value
                    ))
                elif hasattr(value, "to_dict"):
                    result[attr] = value.to_dict()
                elif isinstance(value, dict):
                    result[attr] = dict(map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()
                    ))
                else:
                    result[attr] = value
        if issubclass(ArrayConnectionPath, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ArrayConnectionPath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
