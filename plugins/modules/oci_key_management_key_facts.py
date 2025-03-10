#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_key_management_key_facts
short_description: Fetches details about one or multiple Key resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Key resources in Oracle Cloud Infrastructure
    - Lists the master encryption keys in the specified vault and compartment.
    - As a management operation, this call is subject to a Key Management limit that applies to the total number
      of requests across all management read operations. Key Management might throttle this call to reject an
      otherwise valid request when the total rate of management read operations exceeds 10 requests per second
      for a given tenancy.
    - If I(key_id) is specified, the details of a single Key will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    key_id:
        description:
            - The OCID of the key.
            - Required to get a specific key.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple keys.
        type: str
    sort_by:
        description:
            - The field to sort by. You can specify only one sort order. The default
              order for `TIMECREATED` is descending. The default order for `DISPLAYNAME`
              is ascending.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    protection_mode:
        description:
            - A key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed. A
              protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are
              performed inside the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's
              RSA wrapping key which persists on the HSM. All cryptographic operations that use a key with a protection mode of
              `SOFTWARE` are performed on the server.
        type: str
        choices:
            - "HSM"
            - "SOFTWARE"
    algorithm:
        description:
            - The algorithm used by a key's key versions to encrypt or decrypt data. Currently, support includes AES, RSA, and ECDSA algorithms.
        type: str
        choices:
            - "AES"
            - "RSA"
            - "ECDSA"
    length:
        description:
            - The length of the key in bytes, expressed as an integer. Supported values include 16, 24, or 32.
        type: int
    curve_id:
        description:
            - The curve ID of the keys. (This pertains only to ECDSA keys.)
        type: str
        choices:
            - "NIST_P256"
            - "NIST_P384"
            - "NIST_P521"
    service_endpoint:
        description:
            - The endpoint of the service to call using this client. For example 'https://kms.{region}.{secondLevelDomain}'.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific key
  oci_key_management_key_facts:
    # required
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

- name: List keys
  oci_key_management_key_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: TIMECREATED
    sort_order: ASC
    protection_mode: HSM
    algorithm: AES
    length: 56
    curve_id: "ocid1.curve.oc1..xxxxxxEXAMPLExxxxxx"
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

"""

RETURN = """
keys:
    description:
        - List of Key resources
    returned: on success
    type: complex
    contains:
        current_key_version:
            description:
                - The OCID of the key version used in cryptographic operations. During key rotation, the service might be
                  in a transitional state where this or a newer key version are used intermittently. The `currentKeyVersion`
                  property is updated when the service is guaranteed to use the new key version for all subsequent encryption operations.
                - Returned for get operation
            returned: on success
            type: str
            sample: current_key_version_example
        key_shape:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                algorithm:
                    description:
                        - The algorithm used by a key's key versions to encrypt or decrypt.
                    returned: on success
                    type: str
                    sample: AES
                length:
                    description:
                        - "The length of the key in bytes, expressed as an integer. Supported values include the following:
                            - AES: 16, 24, or 32
                            - RSA: 256, 384, or 512
                            - ECDSA: 32, 48, or 66"
                    returned: on success
                    type: int
                    sample: 56
                curve_id:
                    description:
                        - Supported curve IDs for ECDSA keys.
                    returned: on success
                    type: str
                    sample: "ocid1.curve.oc1..xxxxxxEXAMPLExxxxxx"
        time_of_deletion:
            description:
                - "An optional property indicating when to delete the key, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2019-04-03T21:10:29.600Z`"
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        replica_details:
            description:
                - The value to assign to the replica_details property of this Key.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                replication_id:
                    description:
                        - ReplicationId associated with a key operation
                    returned: on success
                    type: str
                    sample: "ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx"
        is_primary:
            description:
                - The value to assign to the is_primary property of this Key.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        compartment_id:
            description:
                - The OCID of the compartment that contains this master encryption key.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name for the key. It does not have to be unique, and it is changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of the key.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The key's current lifecycle state.
                - "Example: `ENABLED`"
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The date and time the key was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                - "Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vault_id:
            description:
                - The OCID of the vault that contains this key.
            returned: on success
            type: str
            sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        protection_mode:
            description:
                - The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed.
                  A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed
                  inside
                  the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists
                  on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default,
                  a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported.
            returned: on success
            type: str
            sample: HSM
        algorithm:
            description:
                - The algorithm used by a key's key versions to encrypt or decrypt data.
                - Returned for list operation
            returned: on success
            type: str
            sample: AES
    sample: [{
        "current_key_version": "current_key_version_example",
        "key_shape": {
            "algorithm": "AES",
            "length": 56,
            "curve_id": "ocid1.curve.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "time_of_deletion": "2013-10-20T19:20:30+01:00",
        "replica_details": {
            "replication_id": "ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "is_primary": true,
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
        "protection_mode": "HSM",
        "algorithm": "AES"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.key_management import KmsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class KeyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "key_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_key, key_id=self.module.params.get("key_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "protection_mode",
            "algorithm",
            "length",
            "curve_id",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_keys,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


KeyFactsHelperCustom = get_custom_class("KeyFactsHelperCustom")


class ResourceFactsHelper(KeyFactsHelperCustom, KeyFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            key_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            protection_mode=dict(type="str", choices=["HSM", "SOFTWARE"]),
            algorithm=dict(type="str", choices=["AES", "RSA", "ECDSA"]),
            length=dict(type="int"),
            curve_id=dict(type="str", choices=["NIST_P256", "NIST_P384", "NIST_P521"]),
            display_name=dict(type="str"),
            service_endpoint=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="key",
        service_client_class=KmsManagementClient,
        namespace="key_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(keys=result)


if __name__ == "__main__":
    main()
