#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_network_ip_sec_connection_facts
short_description: Fetches details about one or multiple IpSecConnection resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple IpSecConnection resources in Oracle Cloud Infrastructure
    - Lists the IPSec connections for the specified compartment. You can filter the
      results by DRG or CPE.
    - If I(ipsc_id) is specified, the details of a single IpSecConnection will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    ipsc_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.
            - Required to get a specific ip_sec_connection.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple ip_sec_connections.
        type: str
    drg_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG.
        type: str
    cpe_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the CPE.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific ip_sec_connection
  oci_network_ip_sec_connection_facts:
    # required
    ipsc_id: "ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx"

- name: List ip_sec_connections
  oci_network_ip_sec_connection_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    drg_id: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
    cpe_id: "ocid1.cpe.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
ip_sec_connections:
    description:
        - List of IpSecConnection resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the IPSec connection.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        cpe_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the L(Cpe,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/iaas/latest/Cpe/) object.
            returned: on success
            type: str
            sample: "ocid1.cpe.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        drg_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG.
            returned: on success
            type: str
            sample: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The IPSec connection's Oracle ID (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The IPSec connection's current state.
            returned: on success
            type: str
            sample: PROVISIONING
        cpe_local_identifier:
            description:
                - Your identifier for your CPE device. Can be either an IP address or a hostname (specifically,
                  the fully qualified domain name (FQDN)). The type of identifier here must correspond
                  to the value for `cpeLocalIdentifierType`.
                - If you don't provide a value when creating the IPSec connection, the `ipAddress` attribute
                  for the L(Cpe,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Cpe/) object specified by `cpeId` is used as the
                  `cpeLocalIdentifier`.
                - For information about why you'd provide this value, see
                  L(If Your CPE Is Behind a NAT Device,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/overviewIPsec.htm#nat).
                - "Example IP address: `10.0.3.3`"
                - "Example hostname: `cpe.example.com`"
            returned: on success
            type: str
            sample: cpe_local_identifier_example
        cpe_local_identifier_type:
            description:
                - The type of identifier for your CPE device. The value here must correspond to the value
                  for `cpeLocalIdentifier`.
            returned: on success
            type: str
            sample: IP_ADDRESS
        static_routes:
            description:
                - Static routes to the CPE. The CIDR must not be a
                  multicast address or class E address.
                - Used for routing a given IPSec tunnel's traffic only if the tunnel
                  is using static routing. If you configure at least one tunnel to use static routing, then
                  you must provide at least one valid static route. If you configure both
                  tunnels to use BGP dynamic routing, you can provide an empty list for the static routes.
                - The CIDR can be either IPv4 or IPv6. IPv6 addressing is supported for all commercial and government regions.
                  See L(IPv6 Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm).
                - "Example: `10.0.1.0/24`"
                - "Example: `2001:db8::/32`"
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The date and time the IPSec connection was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "cpe_id": "ocid1.cpe.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "drg_id": "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "cpe_local_identifier": "cpe_local_identifier_example",
        "cpe_local_identifier_type": "IP_ADDRESS",
        "static_routes": [],
        "time_created": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IpSecConnectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "ipsc_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ip_sec_connection,
            ipsc_id=self.module.params.get("ipsc_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "drg_id",
            "cpe_id",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_ip_sec_connections,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


IpSecConnectionFactsHelperCustom = get_custom_class("IpSecConnectionFactsHelperCustom")


class ResourceFactsHelper(
    IpSecConnectionFactsHelperCustom, IpSecConnectionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            ipsc_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            drg_id=dict(type="str"),
            cpe_id=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="ip_sec_connection",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(ip_sec_connections=result)


if __name__ == "__main__":
    main()
