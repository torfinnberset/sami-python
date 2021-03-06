#!/usr/bin/env python
"""
WordAPI.py
Copyright 2014 Wordnik, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

from models import *


class DevicetypesApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    

    def getDeviceTypes(self, name, **kwargs):
        """Retrieves Device Types

        Args:
            name, str: Device Type Name (required)

            offset, integer: Offset for pagination. (optional)

            count, integer: Desired count of items in the result set. (optional)

            

        Returns: DeviceTypesEnvelope
        """

        allParams = ['name', 'offset', 'count']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getDeviceTypes" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/devicetypes'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])
        if ('count' in params):
            queryParams['count'] = self.apiClient.toPathValue(params['count'])
        if ('name' in params):
            replacement = str(self.apiClient.toPathValue(params['name']))
            resourcePath = resourcePath.replace('{' + 'name' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DeviceTypesEnvelope')
        return responseObject
        

        

    def getDeviceType(self, deviceTypeId, **kwargs):
        """Retrieves a Device Type

        Args:
            deviceTypeId, str: deviceTypeId (required)

            

        Returns: DeviceTypeEnvelope
        """

        allParams = ['deviceTypeId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getDeviceType" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/devicetypes/{deviceTypeId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('deviceTypeId' in params):
            replacement = str(self.apiClient.toPathValue(params['deviceTypeId']))
            resourcePath = resourcePath.replace('{' + 'deviceTypeId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DeviceTypeEnvelope')
        return responseObject
        

        

    def getLatestManifestProperties(self, deviceTypeId, **kwargs):
        """Get a Device Type's manifest properties for the latest version.

        Args:
            deviceTypeId, str: Device Type ID (required)

            

        Returns: ManifestPropertiesEnvelope
        """

        allParams = ['deviceTypeId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getLatestManifestProperties" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/devicetypes/{deviceTypeId}/manifests/latest/properties'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('deviceTypeId' in params):
            replacement = str(self.apiClient.toPathValue(params['deviceTypeId']))
            resourcePath = resourcePath.replace('{' + 'deviceTypeId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ManifestPropertiesEnvelope')
        return responseObject
        

        

    def getManifestProperties(self, deviceTypeId, version, **kwargs):
        """Get a Device Type's manifest properties for a specific version.

        Args:
            deviceTypeId, str: Device Type ID (required)

            version, integer: Version (required)

            

        Returns: ManifestPropertiesEnvelope
        """

        allParams = ['deviceTypeId', 'version']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getManifestProperties" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/devicetypes/{deviceTypeId}/manifests/{version}/properties'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('deviceTypeId' in params):
            replacement = str(self.apiClient.toPathValue(params['deviceTypeId']))
            resourcePath = resourcePath.replace('{' + 'deviceTypeId' + '}',
                                                replacement)
        if ('version' in params):
            replacement = str(self.apiClient.toPathValue(params['version']))
            resourcePath = resourcePath.replace('{' + 'version' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ManifestPropertiesEnvelope')
        return responseObject
        

        

    def getAvailableManifestVersions(self, deviceTypeId, **kwargs):
        """Get a Device Type's available manifest versions

        Args:
            deviceTypeId, str: Device Type ID (required)

            

        Returns: ManifestVersionsEnvelope
        """

        allParams = ['deviceTypeId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAvailableManifestVersions" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/devicetypes/{deviceTypeId}/availablemanifestversions'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('deviceTypeId' in params):
            replacement = str(self.apiClient.toPathValue(params['deviceTypeId']))
            resourcePath = resourcePath.replace('{' + 'deviceTypeId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ManifestVersionsEnvelope')
        return responseObject
        

        

    




