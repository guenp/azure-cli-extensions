# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .tracked_resource import TrackedResource


class QuantumWorkspace(TrackedResource):
    """The resource proxy definition object for quantum workspace.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :param providers: List of Providers selected for this Workspace
    :type providers: list[~azure.quantum.models.Provider]
    :ivar usable: Whether the current workspace is ready to accept Jobs.
     Possible values include: 'Yes', 'No', 'Partial'
    :vartype usable: str or ~azure.quantum.models.UsableStatus
    :ivar provisioning_state: Provisioning status field. Possible values
     include: 'Succeeded', 'ProviderLaunching', 'ProviderUpdating',
     'ProviderDeleting', 'ProviderProvisioning', 'Failed'
    :vartype provisioning_state: str or
     ~azure.quantum.models.ProvisioningStatus
    :param storage_account: ARM Resource Id of the storage account associated
     with this workspace.
    :type storage_account: str
    :ivar endpoint_uri: The URI of the workspace endpoint.
    :vartype endpoint_uri: str
    :param identity: Managed Identity information.
    :type identity: ~azure.quantum.models.QuantumWorkspaceIdentity
    :ivar system_data: System metadata
    :vartype system_data: ~azure.quantum.models.SystemData
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'usable': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'endpoint_uri': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'providers': {'key': 'properties.providers', 'type': '[Provider]'},
        'usable': {'key': 'properties.usable', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'storage_account': {'key': 'properties.storageAccount', 'type': 'str'},
        'endpoint_uri': {'key': 'properties.endpointUri', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'QuantumWorkspaceIdentity'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
    }

    def __init__(self, **kwargs):
        super(QuantumWorkspace, self).__init__(**kwargs)
        self.providers = kwargs.get('providers', None)
        self.usable = None
        self.provisioning_state = None
        self.storage_account = kwargs.get('storage_account', None)
        self.endpoint_uri = None
        self.identity = kwargs.get('identity', None)
        self.system_data = None