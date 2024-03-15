# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.27
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_27 import models

class Connection(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'host': 'ReferenceNoId',
        'host_group': 'ReferenceNoId',
        'lun': 'int',
        'protocol_endpoint': 'Reference',
        'volume': 'FixedReference',
        'nsid': 'int'
    }

    attribute_map = {
        'host': 'host',
        'host_group': 'host_group',
        'lun': 'lun',
        'protocol_endpoint': 'protocol_endpoint',
        'volume': 'volume',
        'nsid': 'nsid'
    }

    required_args = {
    }

    def __init__(
        self,
        host=None,  # type: models.ReferenceNoId
        host_group=None,  # type: models.ReferenceNoId
        lun=None,  # type: int
        protocol_endpoint=None,  # type: models.Reference
        volume=None,  # type: models.FixedReference
        nsid=None,  # type: int
    ):
        """
        Keyword args:
            host (ReferenceNoId)
            host_group (ReferenceNoId)
            lun (int): The logical unit number (LUN) by which the specified hosts are to address the specified volume. A LUN is set for SCSI connections only. A LUN can be in one of two formats: a simple LUN, or a LUN and Sublun with virtual volumes. The first format is simply the LUN. The second format is a single int64 combining both ((LUN << 32) + Sublun) or (LUN * 4294967296 + Sublun). In the FA UI, a combined LUN and Sublun is represented as `LUN:Sublun`. The maximum int64 LUN:Sublun value is `17587891081215`.
            protocol_endpoint (Reference): A protocol endpoint (also known as a conglomerate volume) which acts as a proxy through which virtual volumes are created and then connected to VMware ESXi hosts or host groups. The protocol endpoint itself does not serve I/Os; instead, its job is to form connections between FlashArray volumes and ESXi hosts and host groups.
            volume (FixedReference): A container that manages the storage space on the array.
            nsid (int): Namespace identifier allocated for the NVMe namespace backing the volume. NSID is set for NVMe connections only.
        """
        if host is not None:
            self.host = host
        if host_group is not None:
            self.host_group = host_group
        if lun is not None:
            self.lun = lun
        if protocol_endpoint is not None:
            self.protocol_endpoint = protocol_endpoint
        if volume is not None:
            self.volume = volume
        if nsid is not None:
            self.nsid = nsid

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Connection`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Connection`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Connection`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Connection`".format(key))
        object.__delattr__(self, key)

    def keys(self):
        return self.attribute_map.keys()

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
        if issubclass(Connection, dict):
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
        if not isinstance(other, Connection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
