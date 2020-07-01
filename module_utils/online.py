# coding: utf-8

# Copyright: (c) 2020, François Ménabé <francois.menabe@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import sys
import json
import requests
from ansible.module_utils.basic import AnsibleModule, env_fallback

class OnlineModule(AnsibleModule):
    # URL to Online.net API
    API_URL = 'https://api.online.net/api/v1'

    # Environment variables to fallback to.
    _ONLINE_URL_FALLBACK = ['ONLINE_API_URL']
    _ONLINE_TOKEN_FALLBACK = ['ONLINE_API_TOKEN']

    # Default argument_spec for Online modules.
    ARGUMENT_SPEC = dict(
        api_url=dict(
            fallback=(env_fallback, _ONLINE_URL_FALLBACK),
            default=API_URL,
            aliases=['base_url']
        ),
        api_token=dict(
            required=True,
            fallback=(env_fallback, _ONLINE_TOKEN_FALLBACK),
            no_log=True,
            aliases=['oauth_token']
        ),
        api_timeout=dict(type='int', default=30, aliases=['timeout']),
        validate_certs=dict(type='bool', default=True),
    )

    def __init__(self, *args, **kwargs):
        '''
        Initialize Ansible module and prepare headers for making API calls.
        '''
        super(OnlineModule, self).__init__(*args, **kwargs)

        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': 'Bearer {:s}'.format(self.params['api_token']),
            'User-Agent': self.user_agent,
            'Content-type': 'application/json'
        })

        # dummy call for ensuring there is no communication or identification problems
        self.get(self.url('user'))

    @property
    def user_agent(self):
        '''
        Generate a User-Agent for HTTP requests based on Ansible and Python versions.
        '''
        return ("ansible {:s} Python {:s}"
                .format(self.ansible_version, sys.version.split(' ')[0]))

    def url(self, *endpoints):
        '''
        Generate calling URL from base API URL and ``endpoints``. Slashed at start
        and end of endpoints are stripped to ensure the URL is valid.
        '''
        return '/'.join([self.params['api_url'], *(str(e).strip('/') for e in endpoints)])

    def call(self, method, url, params=None, data=None, headers=None):
        '''
        Wrap HTTP calls with `requests` module.

        Errors are managed based on HTTP codes and how Online API operate. A
        dictionary containing the JSON response is always returned (or an empty
        dictionnary for endpoints not returning content).
        '''
        resp = getattr(self.session, method.lower())(
            url,
            params=params,
            data=json.dumps(data),
            headers=headers,
            timeout=self.params['api_timeout'],
            verify=self.params['validate_certs']
        )

        if resp.status_code == 204:
            return {}
        if 400 <= resp.status_code <= 499:
            self.warn(str(resp.text))
            self.fail_json(
                msg="({:s} {:s}) Client Error {:d}: {:s}"
                    .format(method.upper(), url, resp.status_code, resp.json()['error']))
        if 500 <= resp.status_code <= 599:
            self.fail_json(
                msg="({:s} {:s}) Server Error {:d}"
                    .format(method.upper(), url, resp.status_code))

        content = resp.json()
        # Sometimes response contains status and error message.
        if isinstance(content, dict) and not content.get('success', True):
            self.fail_json(msg=content.get('message', 'unknown error'))
        return content

    def get(self, url, params=None, headers=None):
        '''Wrap HTTP *GET*.'''
        return self.call('GET', url, params=params, headers=headers)

    def post(self, url, data=None, headers=None):
        '''Wrap HTTP *POST*.'''
        return self.call('POST', url, data=data, headers=headers)

    def delete(self, url, headers=None):
        '''Wrap HTTP *DELETE*.'''
        return self.call('DELETE', url, headers=headers)

    def put(self, url, data=None, headers=None):
        '''Wrap HTTP *PUT*.'''
        return self.call('PUT', url, data=data, headers=headers)

    def patch(self, url, data=None, headers=None):
        '''Wrap HTTP *PATCH*.'''
        return self.call('PATCH', url, data=data, headers=headers)

    def follow_link(self, link):
        return self.get(self.url(link.replace('/api/v1', '')))
