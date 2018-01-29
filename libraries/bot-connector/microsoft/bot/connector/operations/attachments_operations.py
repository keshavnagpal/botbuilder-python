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

from msrest.pipeline import ClientRawResponse

from .. import models


class AttachmentsOperations(object):
    """AttachmentsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def get_attachment_info(
            self, attachment_id, custom_headers=None, raw=False, **operation_config):
        """GetAttachmentInfo.

        Get AttachmentInfo structure describing the attachment views.

        :param attachment_id: attachment id
        :type attachment_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AttachmentInfo or ClientRawResponse if raw=true
        :rtype: ~bot.connector.models.AttachmentInfo or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<bot.connector.models.ErrorResponseException>`
        """
        # Construct URL
        url = '/v3/attachments/{attachmentId}'
        path_format_arguments = {
            'attachmentId': self._serialize.url("attachment_id", attachment_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AttachmentInfo', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def get_attachment(
            self, attachment_id, view_id, custom_headers=None, raw=False, callback=None, **operation_config):
        """GetAttachment.

        Get the named view as binary content.

        :param attachment_id: attachment id
        :type attachment_id: str
        :param view_id: View id from attachmentInfo
        :type view_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: Generator or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<bot.connector.models.ErrorResponseException>`
        """
        # Construct URL
        url = '/v3/attachments/{attachmentId}/views/{viewId}'
        path_format_arguments = {
            'attachmentId': self._serialize.url("attachment_id", attachment_id, 'str'),
            'viewId': self._serialize.url("view_id", view_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=True, **operation_config)

        if response.status_code not in [200, 301, 302]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._client.stream_download(response, callback)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
