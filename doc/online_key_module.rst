.. _online_key_module:


online_key -- Create, update or delete Online.net account SSH key
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



Synopsis
--------
- Create/update/delete a SSH key of an account.
- See `Online API documentation <https://console.online.net/en/api/>`_ for more details.



Requirements
------------
The below requirements are needed on the host that executes this module.

- `python-requests <https://requests.readthedocs.io/en/latest/>`_


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-api_timeout"></div>
                    <b>api_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-api_timeout" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">30</div>
                                    </td>
                                                                <td>
                                            <div>Timeout of HTTP requests.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-api_token"></div>
                    <b>api_token</b>
                    <a class="ansibleOptionLink" href="#parameter-api_token" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                 / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Token to access Online API.</div>
                                            <div>Fallback to <code>ONLINE_API_TOKEN</code> environment variable if not set.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-api_url"></div>
                    <b>api_url</b>
                    <a class="ansibleOptionLink" href="#parameter-api_url" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"https://api.online.net/api/v1"</div>
                                    </td>
                                                                <td>
                                            <div>Base URL to access Online API.</div>
                                            <div>Fallback to <code>ONLINE_API_URL</code> environment variable if not set.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Description of the SSH public key.</div>
                                            <div>Required if <em>state=present</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Content of the SSH public key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to create/update/delete the key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
                    <b>validate_certs</b>
                    <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">"yes"</div>
                                    </td>
                                                                <td>
                                            <div>Whether to check SSL certificates.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>




Examples
--------

.. code-block:: yaml+jinja

    
    - name: "Ensure SSH public key of the controller user exists"
      delegate_to: localhost
      online_key:
        api_token: <FIXME>
        # generate <USER>@<HOSTNAME>
        description: "{{ lookup('pipe', 'whoami') }}@{{ lookup('pipe', 'hostname') }}"
        key: "{{ lookup('file', '~/.ssh/id_rsa.pub'|expanduser) }}"
        state: present

    - name: Update description
      delegate_to: localhost
      online_key:
        api_token: <FIXME>
        description: "my awesome key"
        key: "{{ lookup('file', '~/.ssh/id_rsa.pub'|expanduser) }}"
        state: present

    - name: Remove key
      delegate_to: localhost
      online_key:
        api_token: <FIXME>
        key: "{{ lookup('file', '~/.ssh/id_rsa.pub'|expanduser) }}"
        state: absent




Return Values
-------------
Common return values are documented `here
<https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`__, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-key_id"></div>
                    <b>key_id</b>
                    <a class="ansibleOptionLink" href="#return-key_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">-</span>
                                          </div>
                                    </td>
                <td>when exists</td>
                <td>
                                            <div>UUID of the key into Online account.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">1c7f74bb-fc23-4b82-9369-fbe1df425d1d</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

