# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.9, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_9 import models

class Keytab(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'encryption_type': 'str',
        'fqdn': 'str',
        'kvno': 'int',
        'prefix': 'str',
        'principal': 'str',
        'realm': 'str',
        'source': 'FixedReference',
        'suffix': 'int'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'encryption_type': 'encryption_type',
        'fqdn': 'fqdn',
        'kvno': 'kvno',
        'prefix': 'prefix',
        'principal': 'principal',
        'realm': 'realm',
        'source': 'source',
        'suffix': 'suffix'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        encryption_type=None,  # type: str
        fqdn=None,  # type: str
        kvno=None,  # type: int
        prefix=None,  # type: str
        principal=None,  # type: str
        realm=None,  # type: str
        source=None,  # type: models.FixedReference
        suffix=None,  # type: int
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            encryption_type (str): The encryption type used by the Kerberos key distribution center to generate the keytab.
            fqdn (str): The fully qualified domain name to which the keytab was issued.
            kvno (int): The key version number of the key used to generate the keytab.
            prefix (str): The prefix in the name of the keytab object. This is the same for all keytab objects created from a single keytab file. The name of a keytab entry is created in the format `<prefix>.<suffix>` for all entries.
            principal (str): The service name for which the keytab was issued.
            realm (str): The Kerberos realm that issued the keytab.
            source (FixedReference): A reference to the Active Directory configuration for the computer account that was used to create this keytab. If this keytab was uploaded from a file, all fields in the reference possess `null` values.
            suffix (int): The suffix in the name of the keytab object, determined at creation time using the slot number of the keytab entry in a file and the number of existing entries with the same prefix. The name of a keytab entry is created in the format `<prefix>.<suffix>` for all entries.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if encryption_type is not None:
            self.encryption_type = encryption_type
        if fqdn is not None:
            self.fqdn = fqdn
        if kvno is not None:
            self.kvno = kvno
        if prefix is not None:
            self.prefix = prefix
        if principal is not None:
            self.principal = principal
        if realm is not None:
            self.realm = realm
        if source is not None:
            self.source = source
        if suffix is not None:
            self.suffix = suffix

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Keytab`".format(key))
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
        if issubclass(Keytab, dict):
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
        if not isinstance(other, Keytab):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
