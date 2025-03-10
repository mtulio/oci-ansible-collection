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
module: oci_queue_facts
short_description: Fetches details about one or multiple Queue resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Queue resources in Oracle Cloud Infrastructure
    - Returns a list of Queues.
    - If I(queue_id) is specified, the details of a single Queue will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    queue_id:
        description:
            - unique Queue identifier
            - Required to get a specific queue.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources their lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific queue
  oci_queue_facts:
    # required
    queue_id: "ocid1.queue.oc1..xxxxxxEXAMPLExxxxxx"

- name: List queues
  oci_queue_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
queues:
    description:
        - List of Queue resources
    returned: on success
    type: complex
    contains:
        retention_in_seconds:
            description:
                - The retention period of the messages in the queue, in seconds.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        visibility_in_seconds:
            description:
                - The default visibility of the messages consumed from the queue.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        timeout_in_seconds:
            description:
                - The default polling timeout of the messages in the queue, in seconds.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        dead_letter_queue_delivery_count:
            description:
                - The number of times a message can be delivered to a consumer before being moved to the dead letter queue. A value of 0 indicates that the DLQ
                  is not used.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        custom_encryption_key_id:
            description:
                - Id of the custom master encryption key which will be used to encrypt messages content
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.customencryptionkey.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Queue Identifier, can be renamed
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the the Queue was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the Queue was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Queue.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        messages_endpoint:
            description:
                - The endpoint to use to consume or publish messages in the queue.
            returned: on success
            type: str
            sample: messages_endpoint_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "retention_in_seconds": 56,
        "visibility_in_seconds": 56,
        "timeout_in_seconds": 56,
        "dead_letter_queue_delivery_count": 56,
        "custom_encryption_key_id": "ocid1.customencryptionkey.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "messages_endpoint": "messages_endpoint_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.queue import QueueAdminClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class QueueFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "queue_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_queue, queue_id=self.module.params.get("queue_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_queues, **optional_kwargs
        )


QueueFactsHelperCustom = get_custom_class("QueueFactsHelperCustom")


class ResourceFactsHelper(QueueFactsHelperCustom, QueueFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            queue_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="queue",
        service_client_class=QueueAdminClient,
        namespace="queue",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(queues=result)


if __name__ == "__main__":
    main()
