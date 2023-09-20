# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.11, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_11 import models

class Array(object):
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
        'as_of': 'int',
        'banner': 'str',
        'idle_timeout': 'int',
        'ntp_servers': 'list[str]',
        'os': 'str',
        'revision': 'str',
        'time_zone': 'str',
        'version': 'str',
        'smb_mode': 'str',
        'eradication_config': 'ArrayEradicationConfig',
        'product_type': 'str',
        'security_update': 'str',
        'encryption': 'ArrayEncryption'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'as_of': '_as_of',
        'banner': 'banner',
        'idle_timeout': 'idle_timeout',
        'ntp_servers': 'ntp_servers',
        'os': 'os',
        'revision': 'revision',
        'time_zone': 'time_zone',
        'version': 'version',
        'smb_mode': 'smb_mode',
        'eradication_config': 'eradication_config',
        'product_type': 'product_type',
        'security_update': 'security_update',
        'encryption': 'encryption'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        as_of=None,  # type: int
        banner=None,  # type: str
        idle_timeout=None,  # type: int
        ntp_servers=None,  # type: List[str]
        os=None,  # type: str
        revision=None,  # type: str
        time_zone=None,  # type: str
        version=None,  # type: str
        smb_mode=None,  # type: str
        eradication_config=None,  # type: models.ArrayEradicationConfig
        product_type=None,  # type: str
        security_update=None,  # type: str
        encryption=None,  # type: models.ArrayEncryption
    ):
        """
        Keyword args:
            name (str): A name chosen by the user. Can be changed. Must be locally unique.
            id (str): A non-modifiable, globally unique ID chosen by the system.
            as_of (int): Array time in milliseconds since UNIX epoch.
            banner (str): A string to be shown when logging in to the array.
            idle_timeout (int): Idle timeout in milliseconds. Valid values are in the range of 300000 and 10800000. Setting this value to 0 disables timeouts.
            ntp_servers (list[str])
            os (str): Valid values are `Purity//FA` and `Purity//FB`.
            revision (str)
            time_zone (str): The time zone to use for the array. In particular this affects the CLI formatting and the default snapshot policy time zone.
            version (str)
            smb_mode (str): The current SMB mode of the array. This controls the type of authentication that is used by the array for SMB. Possible values include `ad-auto`, `ad-rfc2307`, `guest`, and `native`. Modifying this value requires the assistance of Pure Storage Support.
            eradication_config (ArrayEradicationConfig)
            product_type (str): For `FlashBlade//S` arrays, the value is determined by the blades in the system. The value will be `FlashBlade` for all older arrays. Valid values are `FlashBlade`, `FlashBlade//S`, `FlashBlade//S200`, and `FlashBladeS500`.
            security_update (str): The name of the installed security update that currently applies to the system. This field will be `null` if either no security update has been installed, or if the most recently installed security update is no longer needed by the current FlashBlade software due to the current software fully incorporating the update.
            encryption (ArrayEncryption)
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if as_of is not None:
            self.as_of = as_of
        if banner is not None:
            self.banner = banner
        if idle_timeout is not None:
            self.idle_timeout = idle_timeout
        if ntp_servers is not None:
            self.ntp_servers = ntp_servers
        if os is not None:
            self.os = os
        if revision is not None:
            self.revision = revision
        if time_zone is not None:
            self.time_zone = time_zone
        if version is not None:
            self.version = version
        if smb_mode is not None:
            self.smb_mode = smb_mode
        if eradication_config is not None:
            self.eradication_config = eradication_config
        if product_type is not None:
            self.product_type = product_type
        if security_update is not None:
            self.security_update = security_update
        if encryption is not None:
            self.encryption = encryption

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Array`".format(key))
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
        if issubclass(Array, dict):
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
        if not isinstance(other, Array):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
