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
module: oci_database_exadata_infrastructure_facts
short_description: Fetches details about one or multiple ExadataInfrastructure resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ExadataInfrastructure resources in Oracle Cloud Infrastructure
    - Lists the Exadata infrastructure resources in the specified compartment. Applies to Exadata Cloud@Customer instances only.
      To list the Exadata Cloud Service infrastructure resources in a compartment, use the  L(ListCloudExadataInfrastructures,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/database/latest/CloudExadataInfrastructure/ListCloudExadataInfrastructures) operation.
    - If I(exadata_infrastructure_id) is specified, the details of a single ExadataInfrastructure will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    exadata_infrastructure_id:
        description:
            - The Exadata infrastructure L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific exadata_infrastructure.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple exadata_infrastructures.
        type: str
    sort_by:
        description:
            - The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME
              is ascending. The DISPLAYNAME sort order is case sensitive.
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
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state exactly.
        type: str
        choices:
            - "CREATING"
            - "REQUIRES_ACTIVATION"
            - "ACTIVATING"
            - "ACTIVE"
            - "ACTIVATION_FAILED"
            - "FAILED"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "DISCONNECTED"
            - "MAINTENANCE_IN_PROGRESS"
            - "WAITING_FOR_CONNECTIVITY"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given. The match is not case sensitive.
        type: str
        aliases: ["name"]
    excluded_fields:
        description:
            - If provided, the specified fields will be excluded in the response.
        type: list
        elements: str
        choices:
            - "multiRackConfigurationFile"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific exadata_infrastructure
  oci_database_exadata_infrastructure_facts:
    # required
    exadata_infrastructure_id: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    excluded_fields: [ "multiRackConfigurationFile" ]

- name: List exadata_infrastructures
  oci_database_exadata_infrastructure_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: CREATING
    display_name: display_name_example
    excluded_fields: [ "multiRackConfigurationFile" ]

"""

RETURN = """
exadata_infrastructures:
    description:
        - List of ExadataInfrastructure resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current lifecycle state of the Exadata infrastructure.
            returned: on success
            type: str
            sample: CREATING
        display_name:
            description:
                - The user-friendly name for the Exadata Cloud@Customer infrastructure. The name does not need to be unique.
            returned: on success
            type: str
            sample: display_name_example
        shape:
            description:
                - The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.
            returned: on success
            type: str
            sample: shape_example
        time_zone:
            description:
                - The time zone of the Exadata infrastructure. For details, see L(Exadata Infrastructure Time
                  Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
            returned: on success
            type: str
            sample: time_zone_example
        cpus_enabled:
            description:
                - The number of enabled CPU cores.
            returned: on success
            type: int
            sample: 56
        max_cpu_count:
            description:
                - The total number of CPU cores available.
            returned: on success
            type: int
            sample: 56
        memory_size_in_gbs:
            description:
                - The memory allocated in GBs.
            returned: on success
            type: int
            sample: 56
        max_memory_in_gbs:
            description:
                - The total memory available in GBs.
            returned: on success
            type: int
            sample: 56
        db_node_storage_size_in_gbs:
            description:
                - The local node storage allocated in GBs.
            returned: on success
            type: int
            sample: 56
        max_db_node_storage_in_g_bs:
            description:
                - The total local node storage available in GBs.
            returned: on success
            type: int
            sample: 56
        data_storage_size_in_tbs:
            description:
                - Size, in terabytes, of the DATA disk group.
            returned: on success
            type: float
            sample: 1.2
        max_data_storage_in_t_bs:
            description:
                - The total available DATA disk group size.
            returned: on success
            type: float
            sample: 1.2
        rack_serial_number:
            description:
                - The serial number for the Exadata infrastructure.
            returned: on success
            type: str
            sample: rack_serial_number_example
        storage_count:
            description:
                - The number of Exadata storage servers for the Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
        additional_storage_count:
            description:
                - The requested number of additional storage servers for the Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
        activated_storage_count:
            description:
                - The requested number of additional storage servers activated for the Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
        compute_count:
            description:
                - The number of compute servers for the Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
        is_multi_rack_deployment:
            description:
                - Indicates if deployment is Multi-Rack or not.
            returned: on success
            type: bool
            sample: true
        multi_rack_configuration_file:
            description:
                - The base64 encoded Multi-Rack configuration json file.
            returned: on success
            type: str
            sample: "null"

        additional_compute_count:
            description:
                - The requested number of additional compute servers for the Exadata infrastructure.
            returned: on success
            type: int
            sample: 56
        additional_compute_system_model:
            description:
                - Oracle Exadata System Model specification. The system model determines the amount of compute or storage
                  server resources available for use. For more information, please see L(System and Shape Configuration
                  Options],https://docs.oracle.com/en/engineered-systems/exadata-cloud-at-customer/ecccm/ecc-system-config-
                  options.html#GUID-9E090174-5C57-4EB1-9243-B470F9F10D6B)
            returned: on success
            type: str
            sample: X7
        cloud_control_plane_server1:
            description:
                - The IP address for the first control plane server.
            returned: on success
            type: str
            sample: cloud_control_plane_server1_example
        cloud_control_plane_server2:
            description:
                - The IP address for the second control plane server.
            returned: on success
            type: str
            sample: cloud_control_plane_server2_example
        netmask:
            description:
                - The netmask for the control plane network.
            returned: on success
            type: str
            sample: netmask_example
        gateway:
            description:
                - The gateway for the control plane network.
            returned: on success
            type: str
            sample: gateway_example
        admin_network_cidr:
            description:
                - The CIDR block for the Exadata administration network.
            returned: on success
            type: str
            sample: admin_network_cidr_example
        infini_band_network_cidr:
            description:
                - The CIDR block for the Exadata InfiniBand interconnect.
            returned: on success
            type: str
            sample: infini_band_network_cidr_example
        corporate_proxy:
            description:
                - The corporate network proxy for access to the control plane network.
            returned: on success
            type: str
            sample: corporate_proxy_example
        dns_server:
            description:
                - The list of DNS server IP addresses. Maximum of 3 allowed.
            returned: on success
            type: list
            sample: []
        ntp_server:
            description:
                - The list of NTP server IP addresses. Maximum of 3 allowed.
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The date and time the Exadata infrastructure was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        csi_number:
            description:
                - The CSI Number of the Exadata infrastructure.
            returned: on success
            type: str
            sample: csi_number_example
        contacts:
            description:
                - The list of contacts for the Exadata infrastructure.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the Exadata Infrastructure contact.
                    returned: on success
                    type: str
                    sample: name_example
                phone_number:
                    description:
                        - The phone number for the Exadata Infrastructure contact.
                    returned: on success
                    type: str
                    sample: phone_number_example
                email:
                    description:
                        - The email for the Exadata Infrastructure contact.
                    returned: on success
                    type: str
                    sample: email_example
                is_primary:
                    description:
                        - If `true`, this Exadata Infrastructure contact is a primary contact. If `false`, this Exadata Infrastructure is a secondary contact.
                    returned: on success
                    type: bool
                    sample: true
                is_contact_mos_validated:
                    description:
                        - If `true`, this Exadata Infrastructure contact is a valid My Oracle Support (MOS) contact. If `false`, this Exadata Infrastructure
                          contact is not a valid MOS contact.
                    returned: on success
                    type: bool
                    sample: true
        maintenance_slo_status:
            description:
                - A field to capture 'Maintenance SLO Status' for the Exadata infrastructure with values 'OK', 'DEGRADED'. Default is 'OK' when the
                  infrastructure is provisioned.
            returned: on success
            type: str
            sample: OK
        maintenance_window:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                preference:
                    description:
                        - The maintenance window scheduling preference.
                    returned: on success
                    type: str
                    sample: NO_PREFERENCE
                patching_mode:
                    description:
                        - "Cloud Exadata infrastructure node patching method, either \\"ROLLING\\" or \\"NONROLLING\\". Default value is ROLLING."
                        - "*IMPORTANT*: Non-rolling infrastructure patching involves system down time. See L(Oracle-Managed Infrastructure Maintenance
                          Updates,https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/examaintenance.htm#Oracle) for more information."
                    returned: on success
                    type: str
                    sample: ROLLING
                is_custom_action_timeout_enabled:
                    description:
                        - If true, enables the configuration of a custom action timeout (waiting period) between database server patching operations.
                    returned: on success
                    type: bool
                    sample: true
                custom_action_timeout_in_mins:
                    description:
                        - Determines the amount of time the system will wait before the start of each database server patching operation.
                          Custom action timeout is in minutes and valid value is between 15 to 120 (inclusive).
                    returned: on success
                    type: int
                    sample: 56
                is_monthly_patching_enabled:
                    description:
                        - If true, enables the monthly patching option.
                    returned: on success
                    type: bool
                    sample: true
                months:
                    description:
                        - Months during the year when maintenance should be performed.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the month of the year.
                            returned: on success
                            type: str
                            sample: JANUARY
                weeks_of_month:
                    description:
                        - Weeks during the month when maintenance should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a
                          duration of 7 days. Weeks start and end based on calendar dates, not days of the week.
                          For example, to allow maintenance during the 2nd week of the month (from the 8th day to the 14th day of the month), use the value 2.
                          Maintenance cannot be scheduled for the fifth week of months that contain more than 28 days.
                          Note that this parameter works in conjunction with the  daysOfWeek and hoursOfDay parameters to allow you to specify specific days of
                          the week and hours that maintenance will be performed.
                    returned: on success
                    type: list
                    sample: []
                days_of_week:
                    description:
                        - Days during the week when maintenance should be performed.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the day of the week.
                            returned: on success
                            type: str
                            sample: MONDAY
                hours_of_day:
                    description:
                        - "The window of hours during the day when maintenance should be performed. The window is a 4 hour slot. Valid values are
                          - 0 - represents time slot 0:00 - 3:59 UTC - 4 - represents time slot 4:00 - 7:59 UTC - 8 - represents time slot 8:00 - 11:59 UTC - 12
                            - represents time slot 12:00 - 15:59 UTC - 16 - represents time slot 16:00 - 19:59 UTC - 20 - represents time slot 20:00 - 23:59
                            UTC"
                    returned: on success
                    type: list
                    sample: []
                lead_time_in_weeks:
                    description:
                        - Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to
                          4.
                    returned: on success
                    type: int
                    sample: 56
        storage_server_version:
            description:
                - The software version of the storage servers (cells) in the Exadata infrastructure.
            returned: on success
            type: str
            sample: storage_server_version_example
        db_server_version:
            description:
                - The software version of the database servers (dom0) in the Exadata infrastructure.
            returned: on success
            type: str
            sample: db_server_version_example
        monthly_db_server_version:
            description:
                - The monthly software version of the database servers (dom0) in the Exadata infrastructure.
            returned: on success
            type: str
            sample: monthly_db_server_version_example
        last_maintenance_run_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last maintenance run.
            returned: on success
            type: str
            sample: "ocid1.lastmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx"
        next_maintenance_run_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the next maintenance run.
            returned: on success
            type: str
            sample: "ocid1.nextmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx"
        is_cps_offline_report_enabled:
            description:
                - Indicates whether cps offline diagnostic report is enabled for this Exadata infrastructure. This will allow a customer to quickly check status
                  themselves and fix problems on their end, saving time and frustration
                  for both Oracle and the customer when they find the CPS in a disconnected state.You can enable offline diagnostic report during Exadata
                  infrastructure provisioning. You can also disable or enable it at any time
                  using the UpdateExadatainfrastructure API.
            returned: on success
            type: bool
            sample: true
        network_bonding_mode_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                client_network_bonding_mode:
                    description:
                        - The network bonding mode for the Exadata infrastructure.
                    returned: on success
                    type: str
                    sample: ACTIVE_BACKUP
                backup_network_bonding_mode:
                    description:
                        - The network bonding mode for the Exadata infrastructure.
                    returned: on success
                    type: str
                    sample: ACTIVE_BACKUP
        availability_domain:
            description:
                - The name of the availability domain that the Exadata infrastructure is located in.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "display_name": "display_name_example",
        "shape": "shape_example",
        "time_zone": "time_zone_example",
        "cpus_enabled": 56,
        "max_cpu_count": 56,
        "memory_size_in_gbs": 56,
        "max_memory_in_gbs": 56,
        "db_node_storage_size_in_gbs": 56,
        "max_db_node_storage_in_g_bs": 56,
        "data_storage_size_in_tbs": 1.2,
        "max_data_storage_in_t_bs": 1.2,
        "rack_serial_number": "rack_serial_number_example",
        "storage_count": 56,
        "additional_storage_count": 56,
        "activated_storage_count": 56,
        "compute_count": 56,
        "is_multi_rack_deployment": true,
        "multi_rack_configuration_file": null,
        "additional_compute_count": 56,
        "additional_compute_system_model": "X7",
        "cloud_control_plane_server1": "cloud_control_plane_server1_example",
        "cloud_control_plane_server2": "cloud_control_plane_server2_example",
        "netmask": "netmask_example",
        "gateway": "gateway_example",
        "admin_network_cidr": "admin_network_cidr_example",
        "infini_band_network_cidr": "infini_band_network_cidr_example",
        "corporate_proxy": "corporate_proxy_example",
        "dns_server": [],
        "ntp_server": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "csi_number": "csi_number_example",
        "contacts": [{
            "name": "name_example",
            "phone_number": "phone_number_example",
            "email": "email_example",
            "is_primary": true,
            "is_contact_mos_validated": true
        }],
        "maintenance_slo_status": "OK",
        "maintenance_window": {
            "preference": "NO_PREFERENCE",
            "patching_mode": "ROLLING",
            "is_custom_action_timeout_enabled": true,
            "custom_action_timeout_in_mins": 56,
            "is_monthly_patching_enabled": true,
            "months": [{
                "name": "JANUARY"
            }],
            "weeks_of_month": [],
            "days_of_week": [{
                "name": "MONDAY"
            }],
            "hours_of_day": [],
            "lead_time_in_weeks": 56
        },
        "storage_server_version": "storage_server_version_example",
        "db_server_version": "db_server_version_example",
        "monthly_db_server_version": "monthly_db_server_version_example",
        "last_maintenance_run_id": "ocid1.lastmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "next_maintenance_run_id": "ocid1.nextmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cps_offline_report_enabled": true,
        "network_bonding_mode_details": {
            "client_network_bonding_mode": "ACTIVE_BACKUP",
            "backup_network_bonding_mode": "ACTIVE_BACKUP"
        },
        "availability_domain": "Uocm:PHX-AD-1",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExadataInfrastructureFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "exadata_infrastructure_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "excluded_fields",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_exadata_infrastructure,
            exadata_infrastructure_id=self.module.params.get(
                "exadata_infrastructure_id"
            ),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "display_name",
            "excluded_fields",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_exadata_infrastructures,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ExadataInfrastructureFactsHelperCustom = get_custom_class(
    "ExadataInfrastructureFactsHelperCustom"
)


class ResourceFactsHelper(
    ExadataInfrastructureFactsHelperCustom, ExadataInfrastructureFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            exadata_infrastructure_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "REQUIRES_ACTIVATION",
                    "ACTIVATING",
                    "ACTIVE",
                    "ACTIVATION_FAILED",
                    "FAILED",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "DISCONNECTED",
                    "MAINTENANCE_IN_PROGRESS",
                    "WAITING_FOR_CONNECTIVITY",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            excluded_fields=dict(
                type="list", elements="str", choices=["multiRackConfigurationFile"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="exadata_infrastructure",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(exadata_infrastructures=result)


if __name__ == "__main__":
    main()
