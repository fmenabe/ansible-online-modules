# coding: utf-8

# Copyright: (c) 2020, François Ménabé <francois.menabe@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

class ModuleDocFragment(object):
    DOCUMENTATION = r''''
author:
  - François Ménabé (@fmenabe)
requirements:
  - requests
version_added: 2.9
options:
  api_url:
    description:
      - Base URL to access Online API. Fallback to I(ONLINE_API_URL)
        environment varialbe if not set.
    default: https://api.online.net/api/v1
  api_token:
    description:
      - Token to access Online API. Fallback to I(ONLINE_API_TOKEN)
        environment varialbe if not set.
    required: yes
  api_timeout:
    description:
      - Timeout of HTTP requests.
    default: 30
  validate_certs:
    description:
      - Whether to check SSL certificates.
    default: True
'''
