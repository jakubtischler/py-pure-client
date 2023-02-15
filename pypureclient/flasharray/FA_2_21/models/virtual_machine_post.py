# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.21
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_21 import models

class VirtualMachinePost(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'source': 'Reference',
        'vm_id': 'str',
        'vm_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'source': 'source',
        'vm_id': 'vm_id',
        'vm_type': 'vm_type'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        source=None,  # type: models.Reference
        vm_id=None,  # type: str
        vm_type=None,  # type: str
    ):
        """
        Keyword args:
            id (str): The ID of the virtual machine to create or modify, as assigned by the external system. `id` is deprecated. Use `vm_id` instead.
            source (Reference): The recovery context for the virtual machine or virtual machine snapshot being modified.
            vm_id (str): The ID of the virtual machine to create or modify, as assigned by the external system.
            vm_type (str): The type of virtual machine. The only valid value is `vvol`.
        """
        if id is not None:
            self.id = id
        if source is not None:
            self.source = source
        if vm_id is not None:
            self.vm_id = vm_id
        if vm_type is not None:
            self.vm_type = vm_type

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VirtualMachinePost`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
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
        if issubclass(VirtualMachinePost, dict):
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
        if not isinstance(other, VirtualMachinePost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
