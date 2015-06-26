# -*- coding: utf-8 -*-
import os
import json
import requests


class BluemixError(Exception):
    pass


class APIError(BluemixError):
    pass


class Bluemix(object):
    def __init__(self, credentials):
        self._credentials = credentials


class VisualRecognition(Bluemix):
    def labels(self):
        pass

    def recognize(self, *images, labels=[], label_groups=[]):
        url = 'https://gateway.watsonplatform.net/visual-recognition-beta/api/v1/tag/recognize'
        auth_token = self._credentials['username'], self._credentials['password']
        labels_to_check = {
            'labels': labels,
            'label_groups': label_groups,
        }
        payload = {
            'labels_to_check': labels_to_check,
        }
        files = dict((os.path.basename(image), (os.path.basename(image), open(image, 'rb'))) for image in images)
        res = requests.post(url, params=payload, auth=auth_token, files=files)
        if res.status_code != requests.codes.ok:
            raise APIError('status code={}, reason={}'.format(res.status_code, res.reason))
        data = json.loads(res.text)
        try:
            return data['images']
        except KeyError:
            raise APIError('Illigal response: {}'.format(res.text))
