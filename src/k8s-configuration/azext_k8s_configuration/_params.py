# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements

from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azure.cli.core.commands.parameters import (
    get_enum_type,
    get_three_state_flag,
    tags_type
)
from .validators import (
    validate_configuration_name,
    validate_fluxconfig_name,
    validate_namespace,
    validate_operator_instance_name,
    validate_operator_namespace
)

from .action import (
    KustomizationAddAction,
)
from . import consts


def load_arguments(self, _):
    with self.argument_context('k8s-configuration') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cluster_name',
                   options_list=['--cluster-name', '-c'],
                   help='Name of the Kubernetes cluster')
        c.argument('cluster_type',
                   options_list=['--cluster-type', '-t'],
                   arg_type=get_enum_type(['connectedClusters', 'managedClusters']),
                   help='Specify Arc connected clusters or AKS managed clusters.')

    with self.argument_context('k8s-configuration flux') as c:
        c.argument('name',
                   options_list=['--name', '-n'],
                   help='Name of the flux configuration',
                   validator=validate_fluxconfig_name)
        c.argument('scope',
                   options_list=['--scope', '-s'],
                   arg_type=get_enum_type(['namespace', 'cluster']),
                   help="Specify scope of the operator to be 'namespace' or 'cluster'")
        c.argument('namespace',
                   help='Namespace to deploy the configuration',
                   options_list=['--namespace', '--ns'],
                   validator=validate_namespace)
        c.argument('kind',
                   arg_type=get_enum_type([consts.GIT]),
                   help='Source kind to reconcile')
        c.argument('url',
                   options_list=['--url', '-u'],
                   help='URL of the git repo source to reconcile')
        c.argument('timeout',
                   help='Maximum time to reconcile the source before timing out')
        c.argument('sync_interval',
                   options_list=['--interval', '--sync-interval'],
                   help='Time between reconciliations of the source on the cluster')
        c.argument('branch',
                   arg_group="Git Repo Ref",
                   help='Branch within the git source to reconcile with the cluster')
        c.argument('tag',
                   arg_group="Git Repo Ref",
                   help='Tag within the git source to reconcile with the cluster')
        c.argument('semver',
                   arg_group="Git Repo Ref",
                   help='Semver range within the git source to reconcile with the cluster')
        c.argument('commit',
                   arg_group="Git Repo Ref",
                   help='Commit within the git source to reconcile with the cluster')
        c.argument('ssh_private_key',
                   arg_group="Auth",
                   help='Base64-encoded private ssh key for private repository sync')
        c.argument('ssh_private_key_file',
                   arg_group="Auth",
                   help='File path to private ssh key for private repository sync')
        c.argument('https_user',
                   arg_group="Auth",
                   help='HTTPS username for private repository sync')
        c.argument('https_key',
                   arg_group="Auth",
                   help='HTTPS token/password for private repository sync')
        c.argument('https_ca_cert',
                   arg_group="Auth",
                   help='Base64-encoded HTTPS CA certificate for TLS communication with private repository sync')
        c.argument('https_ca_cert_file',
                   arg_group="Auth",
                   help='File path to HTTPS CA certificate file for TLS communication with private repository sync')
        c.argument('known_hosts',
                   arg_group="Auth",
                   help='Base64-encoded known_hosts data containing public SSH keys required to access private Git instances')
        c.argument('known_hosts_file',
                   arg_group="Auth",
                   help='File path to known_hosts contents containing public SSH keys required to access private Git instances')
        c.argument('local_auth_ref',
                   options_list=['--local-auth-ref', '--local-ref'],
                   arg_group="Auth",
                   help='Local reference to a kubernetes secret in the configuration namespace to use for communication to the source')
        c.argument('suspend',
                   arg_type=get_three_state_flag(),
                   help='Suspend the reconciliation of the source and kustomizations associated with this configuration')
        c.argument('kustomization',
                   action=KustomizationAddAction,
                   options_list=['--kustomization', '-k'],
                   help="Define kustomizations to sync sources with parameters ['name', 'path', 'depends_on', 'timeout', 'sync_interval', 'retry_interval', 'prune', 'force']",
                   nargs='+')

    with self.argument_context('k8s-configuration flux delete') as c:
        c.argument('force',
                   arg_type=get_three_state_flag(),
                   help='Force delete the flux configuration from the cluster.')
        c.argument('yes',
                   options_list=['--yes', '-y'],
                   help='Do not prompt for confirmation')

    with self.argument_context('k8s-configuration') as c:
        c.argument('name',
                   options_list=['--name', '-n'],
                   help='Name of the configuration',
                   validator=validate_configuration_name)

    with self.argument_context('k8s-configuration create') as c:
        c.argument('repository_url',
                   options_list=['--repository-url', '-u'],
                   help='Url of the source control repository')
        c.argument('scope',
                   arg_type=get_enum_type(['namespace', 'cluster']),
                   help='''Specify scope of the operator to be 'namespace' or 'cluster' ''')
        c.argument('enable_helm_operator',
                   arg_group="Helm Operator",
                   arg_type=get_three_state_flag(),
                   options_list=['--enable-helm-operator', '--enable-hop'],
                   help='Enable support for Helm chart deployments')
        c.argument('helm_operator_params',
                   arg_group="Helm Operator",
                   options_list=['--helm-operator-params', '--hop-params'],
                   help='Chart values for the Helm Operator (if enabled)')
        c.argument('helm_operator_chart_version',
                   arg_group="Helm Operator",
                   options_list=['--helm-operator-chart-version', '--hop-chart-version'],
                   help='Chart version of the Helm Operator (if enabled)')
        c.argument('operator_params',
                   arg_group="Operator",
                   help='Parameters for the Operator')
        c.argument('operator_instance_name',
                   arg_group="Operator",
                   help='Instance name of the Operator',
                   validator=validate_operator_instance_name)
        c.argument('operator_namespace',
                   arg_group="Operator",
                   help='Namespace in which to install the Operator',
                   validator=validate_operator_namespace)
        c.argument('operator_type',
                   arg_group="Operator",
                   help='''Type of the operator. Valid value is 'flux' ''')
        c.argument('ssh_private_key',
                   arg_group="Auth",
                   help='Specify Base64-encoded private ssh key for private repository sync')
        c.argument('ssh_private_key_file',
                   arg_group="Auth",
                   help='Specify file path to private ssh key for private repository sync')
        c.argument('https_user',
                   arg_group="Auth",
                   help='Specify HTTPS username for private repository sync')
        c.argument('https_key',
                   arg_group="Auth",
                   help='Specify HTTPS token/password for private repository sync')
        c.argument('ssh_known_hosts',
                   arg_group="Auth",
                   help='Specify Base64-encoded known_hosts contents containing public SSH keys required to access private Git instances')
        c.argument('ssh_known_hosts_file',
                   arg_group="Auth",
                   help='Specify file path to known_hosts contents containing public SSH keys required to access private Git instances')

    with self.argument_context('k8s-configuration flux kustomization') as c:
        c.argument('kustomization_name',
                   options_list=['--kustomization-name', '-k'],
                   help='Specify the name of the kustomization to target')
        c.argument('path',
                   help='Specify the path in the source that the kustomization should apply')
        c.argument('dependencies',
                   options_list=['--depends', '--dependencies', "--depends-on"],
                   help='Comma-separated list of kustomization dependencies')
        c.argument('timeout',
                   help='Maximum time to reconcile the kustomization before timing out')
        c.argument('sync_interval',
                   options_list=['--interval', '--sync-interval'],
                   help='Time between reconciliations of the kustomization on the cluster')
        c.argument('retry_interval',
                   help='Time between reconciliations of the kustomization on the cluster on failures, defaults to --sync-interval')
        c.argument('prune',
                   arg_type=get_three_state_flag(),
                   help='Garbage collect resources deployed by the kustomization on the cluster')
        c.argument('force',
                   arg_type=get_three_state_flag(),
                   help='Re-create resources that cannot be updated on the cluster (i.e. jobs)')

    with self.argument_context('k8s-configuration flux kustomization delete') as c:
        c.argument('yes',
                   options_list=['--yes', '-y'],
                   help='Do not prompt for confirmation')
