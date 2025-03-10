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
module: oci_loadbalancer_rule_set_facts
short_description: Fetches details about one or multiple RuleSet resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RuleSet resources in Oracle Cloud Infrastructure
    - Lists all rule sets associated with the specified load balancer.
    - If I(rule_set_name) is specified, the details of a single RuleSet will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    rule_set_name:
        description:
            - The name of the rule set to retrieve.
            - "Example: `example_rule_set`"
            - Required to get a specific rule_set.
        type: str
        aliases: ["name"]
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the specified load balancer.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific rule_set
  oci_loadbalancer_rule_set_facts:
    # required
    rule_set_name: rule_set_name_example
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

- name: List rule_sets
  oci_loadbalancer_rule_set_facts:
    # required
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
rule_sets:
    description:
        - List of RuleSet resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name for this set of rules. It must be unique and it cannot be changed. Avoid entering
                  confidential information.
                - "Example: `example_rule_set`"
            returned: on success
            type: str
            sample: name_example
        items:
            description:
                - An array of rules that compose the rule set.
            returned: on success
            type: complex
            contains:
                value:
                    description:
                        - "A header value that conforms to RFC 7230. With the following exceptions:
                          *  value cannot contain `$`
                          *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid."
                        - "Example: `example_value`"
                    returned: on success
                    type: str
                    sample: value_example
                description:
                    description:
                        - A brief description of the access control rule. Avoid entering confidential information.
                        - "example: `192.168.0.0/16 and 2001:db8::/32 are trusted clients. Whitelist them.`"
                    returned: on success
                    type: str
                    sample: description_example
                allowed_methods:
                    description:
                        - The list of HTTP methods allowed for this listener.
                        - By default, you can specify only the standard HTTP methods defined in the
                          L(HTTP Method Registry,http://www.iana.org/assignments/http-methods/http-methods.xhtml). You can also
                          see a list of supported standard HTTP methods in the Load Balancing service documentation at
                          L(Managing Rule Sets,https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrulesets.htm).
                        - Your backend application must be able to handle the methods specified in this list.
                        - The list of HTTP methods is extensible. If you need to configure custom HTTP methods, contact
                          L(My Oracle Support,http://support.oracle.com/) to remove the restriction for your tenancy.
                        - "Example: [\\"GET\\", \\"PUT\\", \\"POST\\", \\"PROPFIND\\"]"
                    returned: on success
                    type: list
                    sample: []
                status_code:
                    description:
                        - The HTTP status code to return when the requested HTTP method is not in the list of allowed methods.
                          The associated status line returned with the code is mapped from the standard HTTP specification. The
                          default value is `405 (Method Not Allowed)`.
                        - "Example: 403"
                    returned: on success
                    type: int
                    sample: 56
                prefix:
                    description:
                        - "A string to prepend to the header value. The resulting header value must conform to RFC 7230.
                          With the following exceptions:
                          *  value cannot contain `$`
                          *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid."
                        - "Example: `example_prefix_value`"
                    returned: on success
                    type: str
                    sample: prefix_example
                suffix:
                    description:
                        - "A string to append to the header value. The resulting header value must conform to RFC 7230.
                          With the following exceptions:
                          *  value cannot contain `$`
                          *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid."
                        - "Example: `example_suffix_value`"
                    returned: on success
                    type: str
                    sample: suffix_example
                are_invalid_characters_allowed:
                    description:
                        - "Indicates whether or not invalid characters in client header fields will be allowed.
                          Valid names are composed of English letters, digits, hyphens and underscores.
                          If \\"true\\", invalid characters are allowed in the HTTP header.
                          If \\"false\\", invalid characters are not allowed in the HTTP header"
                    returned: on success
                    type: bool
                    sample: true
                http_large_header_size_in_kb:
                    description:
                        - The maximum size of each buffer used for reading http client request header.
                          This value indicates the maximum size allowed for each buffer.
                          The allowed values for buffer size are 8, 16, 32 and 64.
                    returned: on success
                    type: int
                    sample: 56
                response_code:
                    description:
                        - The HTTP status code to return when the incoming request is redirected.
                        - "The status line returned with the code is mapped from the standard HTTP specification. Valid response
                          codes for redirection are:"
                        - "*  301
                          *  302
                          *  303
                          *  307
                          *  308"
                        - The default value is `302` (Found).
                        - "Example: `301`"
                    returned: on success
                    type: int
                    sample: 56
                conditions:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        operator:
                            description:
                                - A string that specifies how to compare the PathMatchCondition object's `attributeValue` string to the
                                  incoming URI.
                                - "*  **EXACT_MATCH** - The incoming URI path must exactly and completely match the `attributeValue` string."
                                - "*  **FORCE_LONGEST_PREFIX_MATCH** - The system looks for the `attributeValue` string with the best,
                                     longest match of the beginning portion of the incoming URI path."
                                - "*  **PREFIX_MATCH** - The beginning portion of the incoming URI path must exactly match the
                                     `attributeValue` string."
                                - "*  **SUFFIX_MATCH** - The ending portion of the incoming URI path must exactly match the `attributeValue`
                                     string."
                            returned: on success
                            type: str
                            sample: EXACT_MATCH
                        attribute_name:
                            description:
                                - ""
                            returned: on success
                            type: str
                            sample: SOURCE_IP_ADDRESS
                        attribute_value:
                            description:
                                - The path string that the redirection rule applies to.
                                - "Example: `/example`"
                            returned: on success
                            type: str
                            sample: attribute_value_example
                redirect_uri:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        protocol:
                            description:
                                - The HTTP protocol to use in the redirect URI.
                                - "When this value is null, not set, or set to `{protocol}`, the service preserves the original protocol from the
                                  incoming HTTP request URI. Allowed values are:"
                                - "*  HTTP
                                  *  HTTPS
                                  *  {protocol}"
                                - "`{protocol}` is the only valid token for this property. It can appear only once in the value string."
                                - "Example: `HTTPS`"
                            returned: on success
                            type: str
                            sample: protocol_example
                        host:
                            description:
                                - The valid domain name (hostname) or IP address to use in the redirect URI.
                                - When this value is null, not set, or set to `{host}`, the service preserves the original domain name from the
                                  incoming HTTP request URI.
                                - All RedirectUri tokens are valid for this property. You can use any token more than once.
                                - Curly braces are valid in this property only to surround tokens, such as `{host}`
                                - "Examples:"
                                - "*  **example.com** appears as `example.com` in the redirect URI."
                                - "*  **in{host}** appears as `inexample.com` in the redirect URI if `example.com` is the hostname in the
                                     incoming HTTP request URI."
                                - "*  **{port}{host}** appears as `8081example.com` in the redirect URI if `example.com` is the hostname and
                                     the port is `8081` in the incoming HTTP request URI."
                            returned: on success
                            type: str
                            sample: host_example
                        port:
                            description:
                                - The communication port to use in the redirect URI.
                                - Valid values include integers from 1 to 65535.
                                - When this value is null, the service preserves the original port from the incoming HTTP request URI.
                                - "Example: `8081`"
                            returned: on success
                            type: int
                            sample: 56
                        path:
                            description:
                                - The HTTP URI path to use in the redirect URI.
                                - "When this value is null, not set, or set to `{path}`, the service preserves the original path from the
                                  incoming HTTP request URI. To omit the path from the redirect URI, set this value to an empty string, \\"\\"."
                                - All RedirectUri tokens are valid for this property. You can use any token more than once.
                                - The path string must begin with `/` if it does not begin with the `{path}` token.
                                - "Examples:"
                                - "*  __/example/video/123__ appears as `/example/video/123` in the redirect URI."
                                - "*  __/example{path}__ appears as `/example/video/123` in the redirect URI if `/video/123` is the path in the
                                     incoming HTTP request URI."
                                - "*  __{path}/123__ appears as `/example/video/123` in the redirect URI if `/example/video` is the path in the
                                     incoming HTTP request URI."
                                - "*  __{path}123__ appears as `/example/video123` in the redirect URI if `/example/video` is the path in the
                                     incoming HTTP request URI."
                                - "*  __/{host}/123__ appears as `/example.com/123` in the redirect URI if `example.com` is the hostname
                                     in the incoming HTTP request URI."
                                - "*  __/{host}/{port}__ appears as `/example.com/123` in the redirect URI if `example.com` is the hostname and
                                     `123` is the port in the incoming HTTP request URI."
                                - "*  __/{query}__ appears as `/lang=en` in the redirect URI if the query is `lang=en` in the incoming HTTP
                                     request URI."
                            returned: on success
                            type: str
                            sample: path_example
                        query:
                            description:
                                - The query string to use in the redirect URI.
                                - When this value is null, not set, or set to `{query}`, the service preserves the original query parameters
                                  from the incoming HTTP request URI.
                                - All `RedirectUri` tokens are valid for this property. You can use any token more than once.
                                - If the query string does not begin with the `{query}` token, it must begin with the question mark (?) character.
                                - "You can specify multiple query parameters as a single string. Separate each query parameter with an ampersand
                                  (&) character. To omit all incoming query parameters from the redirect URI, set this value to an empty
                                  string, \\"\\"."
                                - If the specified query string results in a redirect URI ending with `?` or `&`, the last character is truncated.
                                  For example, if the incoming URI is `http://host.com:8080/documents` and the query property value is
                                  `?lang=en&{query}`, the redirect URI is `http://host.com:8080/documents?lang=en`. The system
                                  truncates the final ampersand (&) because the incoming URI included no value to replace the {query} token.
                                - "Examples:
                                  * **lang=en&time_zone=PST** appears as `lang=en&time_zone=PST` in the redirect URI."
                                - "* **{query}** appears as `lang=en&time_zone=PST` in the redirect URI if `lang=en&time_zone=PST` is the query
                                    string in the incoming HTTP request. If the incoming HTTP request has no query parameters, the `{query}`
                                    token renders as an empty string."
                                - "* **lang=en&{query}&time_zone=PST** appears as `lang=en&country=us&time_zone=PST` in the redirect URI if
                                    `country=us` is the query string in the incoming HTTP request. If the incoming HTTP request has no query
                                    parameters, this value renders as `lang=en&time_zone=PST`."
                                - "*  **protocol={protocol}&hostname={host}** appears as `protocol=http&hostname=example.com` in the redirect
                                     URI if the protocol is `HTTP` and the hostname is `example.com` in the incoming HTTP request."
                                - "*  **port={port}&hostname={host}** appears as `port=8080&hostname=example.com` in the redirect URI if the
                                     port is `8080` and the hostname is `example.com` in the incoming HTTP request URI."
                            returned: on success
                            type: str
                            sample: query_example
                action:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: ADD_HTTP_REQUEST_HEADER
                header:
                    description:
                        - A header name that conforms to RFC 7230.
                        - "Example: `example_header_name`"
                    returned: on success
                    type: str
                    sample: header_example
    sample: [{
        "name": "name_example",
        "items": [{
            "value": "value_example",
            "description": "description_example",
            "allowed_methods": [],
            "status_code": 56,
            "prefix": "prefix_example",
            "suffix": "suffix_example",
            "are_invalid_characters_allowed": true,
            "http_large_header_size_in_kb": 56,
            "response_code": 56,
            "conditions": [{
                "operator": "EXACT_MATCH",
                "attribute_name": "SOURCE_IP_ADDRESS",
                "attribute_value": "attribute_value_example"
            }],
            "redirect_uri": {
                "protocol": "protocol_example",
                "host": "host_example",
                "port": 56,
                "path": "path_example",
                "query": "query_example"
            },
            "action": "ADD_HTTP_REQUEST_HEADER",
            "header": "header_example"
        }]
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.load_balancer import LoadBalancerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RuleSetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "load_balancer_id",
            "rule_set_name",
        ]

    def get_required_params_for_list(self):
        return [
            "load_balancer_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_rule_set,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            rule_set_name=self.module.params.get("rule_set_name"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_rule_sets,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            **optional_kwargs
        )


RuleSetFactsHelperCustom = get_custom_class("RuleSetFactsHelperCustom")


class ResourceFactsHelper(RuleSetFactsHelperCustom, RuleSetFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            rule_set_name=dict(aliases=["name"], type="str"),
            load_balancer_id=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="rule_set",
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(rule_sets=result)


if __name__ == "__main__":
    main()
