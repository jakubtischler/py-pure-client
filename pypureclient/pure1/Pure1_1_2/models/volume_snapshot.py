# coding: utf-8

"""
    Pure1 Public REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.pure1.Pure1_1_2 import models

class VolumeSnapshot(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'as_of': 'int',
        'id': 'str',
        'name': 'str',
        'arrays': 'list[FixedReferenceFqdn]',
        'created': 'int',
        'destroyed': 'bool',
        'pod': 'FixedReference',
        'provisioned': 'int',
        'on': 'FixedReferenceFqdn',
        'serial': 'str',
        'snapshot_group': 'FixedReference',
        'source': 'FixedReference',
        'suffix': 'str'
    }

    attribute_map = {
        'as_of': '_as_of',
        'id': 'id',
        'name': 'name',
        'arrays': 'arrays',
        'created': 'created',
        'destroyed': 'destroyed',
        'pod': 'pod',
        'provisioned': 'provisioned',
        'on': 'on',
        'serial': 'serial',
        'snapshot_group': 'snapshot_group',
        'source': 'source',
        'suffix': 'suffix'
    }

    required_args = {
    }

    def __init__(
        self,
        as_of=None,  # type: int
        id=None,  # type: str
        name=None,  # type: str
        arrays=None,  # type: List[models.FixedReferenceFqdn]
        created=None,  # type: int
        destroyed=None,  # type: bool
        pod=None,  # type: models.FixedReference
        provisioned=None,  # type: int
        on=None,  # type: models.FixedReferenceFqdn
        serial=None,  # type: str
        snapshot_group=None,  # type: models.FixedReference
        source=None,  # type: models.FixedReference
        suffix=None,  # type: str
    ):
        """
        Keyword args:
            as_of (int): The freshness of the data (timestamp in millis since epoch).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            name (str): A non-modifiable, locally unique name chosen by the system.
            arrays (list[FixedReferenceFqdn]): The list of arrays where this resource exists. Many resources are on a single array, but some resources, such as pods, can be shared across multiple arrays.
            created (int): Creation time in milliseconds since UNIX epoch.
            destroyed (bool): Indicates if this snapshot has been destroyed and is pending eradication.
            pod (FixedReference): A reference to the pod the source volume belongs to, if applicable.
            provisioned (int): Indicates the size (in bytes) of the volume when the snapshot was taken.
            on (FixedReferenceFqdn)
            serial (str): Serial number generated by Purity when the snapshot was created.
            snapshot_group (FixedReference): A reference to a consistency group snapshot that this snapshot is part of.
            source (FixedReference): A reference to the volume that the snapshot was taken from.
            suffix (str): Suffix added to the source volume name used to generate the volume snapshot name.
        """
        if as_of is not None:
            self.as_of = as_of
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if arrays is not None:
            self.arrays = arrays
        if created is not None:
            self.created = created
        if destroyed is not None:
            self.destroyed = destroyed
        if pod is not None:
            self.pod = pod
        if provisioned is not None:
            self.provisioned = provisioned
        if on is not None:
            self.on = on
        if serial is not None:
            self.serial = serial
        if snapshot_group is not None:
            self.snapshot_group = snapshot_group
        if source is not None:
            self.source = source
        if suffix is not None:
            self.suffix = suffix

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeSnapshot`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeSnapshot`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeSnapshot`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeSnapshot`".format(key))
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
        if issubclass(VolumeSnapshot, dict):
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
        if not isinstance(other, VolumeSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
