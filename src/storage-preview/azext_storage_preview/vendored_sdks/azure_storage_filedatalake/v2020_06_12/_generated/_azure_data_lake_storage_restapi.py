# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

    from azure.core.pipeline.transport import HttpRequest, HttpResponse

from ._configuration import AzureDataLakeStorageRESTAPIConfiguration
from .operations import ServiceOperations
from .operations import FileSystemOperations
from .operations import PathOperations
from . import models


class AzureDataLakeStorageRESTAPI(object):
    """Azure Data Lake Storage provides storage for Hadoop and other big data workloads.

    :ivar service: ServiceOperations operations
    :vartype service: azure.storage.filedatalake.operations.ServiceOperations
    :ivar file_system: FileSystemOperations operations
    :vartype file_system: azure.storage.filedatalake.operations.FileSystemOperations
    :ivar path: PathOperations operations
    :vartype path: azure.storage.filedatalake.operations.PathOperations
    :param url: The URL of the service account, container, or blob that is the targe of the desired operation.
    :type url: str
    """

    def __init__(
        self,
        url,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        base_url = '{url}'
        self._config = AzureDataLakeStorageRESTAPIConfiguration(url, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.service = ServiceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.file_system = FileSystemOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.path = PathOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, http_request, **kwargs):
        # type: (HttpRequest, Any) -> HttpResponse
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.HttpResponse
        """
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AzureDataLakeStorageRESTAPI
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)