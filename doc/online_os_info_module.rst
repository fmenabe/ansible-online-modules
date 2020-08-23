.. _online_os_info_module:


online_os_info -- Retrieve operating systems available for a server
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



Synopsis
--------
- Retrieve operating systems available for a server.



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
                    <div class="ansibleOptionAnchor" id="parameter-server_id"></div>
                    <b>server_id</b>
                    <a class="ansibleOptionLink" href="#parameter-server_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Id of a server.</div>
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

    
    - name: "Retrieve available operating systems"
      delegate_to: localhost
      online_os_info:
        api_token: <FIXME>
        server_id: 99999
      register: result
    - debug: var=result.online_os_info




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
                    <div class="ansibleOptionAnchor" id="return-online_os_info"></div>
                    <b>online_os_info</b>
                    <a class="ansibleOptionLink" href="#return-online_os_info" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on sucess</td>
                <td>
                                            <div>Reponse from Online API.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;online_os_info&#x27;: [{&#x27;arch&#x27;: &#x27;64 bits&#x27;, &#x27;end_of_life&#x27;: None, &#x27;id&#x27;: 305, &#x27;name&#x27;: &#x27;centos&#x27;, &#x27;release&#x27;: &#x27;2014-07-06T22:00:00.000Z&#x27;, &#x27;type&#x27;: &#x27;server&#x27;, &#x27;version&#x27;: &#x27;CentOS 7&#x27;}, {&#x27;arch&#x27;: &#x27;64 bits&#x27;, &#x27;end_of_life&#x27;: &#x27;2020-03-11T23:00:00.000Z&#x27;, &#x27;id&#x27;: 335, &#x27;name&#x27;: &#x27;ESXi&#x27;, &#x27;release&#x27;: &#x27;2015-09-09T22:00:00.000Z&#x27;, &#x27;type&#x27;: &#x27;virtualization&#x27;, &#x27;version&#x27;: &#x27;ESXi 6.0.0 U1&#x27;}, &#x27;...&#x27;]}</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

