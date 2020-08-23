.. _online_server_info_module:


online_server_info -- Gather facts about servers
++++++++++++++++++++++++++++++++++++++++++++++++



Synopsis
--------
- Gather facts about servers.



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

    
    - name: Gather information servers
      online_server_info:
        api_token: <FIXME>
      register: result

    - debug: var=result.online_servers




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
                    <div class="ansibleOptionAnchor" id="return-online_servers"></div>
                    <b>online_servers</b>
                    <a class="ansibleOptionLink" href="#return-online_servers" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Servers facts returned by the API.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;online_servers&#x27;: [{&#x27;abuse&#x27;: &#x27;abuse@example.com&#x27;, &#x27;anti_ddos&#x27;: False, &#x27;bmc&#x27;: {&#x27;session_key&#x27;: None}, &#x27;boot_mode&#x27;: &#x27;normal&#x27;, &#x27;contacts&#x27;: {&#x27;owner&#x27;: &#x27;foobar&#x27;, &#x27;tech&#x27;: &#x27;foobar&#x27;}, &#x27;disks&#x27;: [{&#x27;capacity&#x27;: 3815448, &#x27;connector&#x27;: &#x27;A&#x27;, &#x27;id&#x27;: 261223, &#x27;type&#x27;: &#x27;SATA&#x27;}], &#x27;drive_arrays&#x27;: [{&#x27;disks&#x27;: [{&#x27;capacity&#x27;: 3815448, &#x27;connector&#x27;: &#x27;A&#x27;, &#x27;id&#x27;: 261223, &#x27;type&#x27;: &#x27;SATA&#x27;}]}], &#x27;hardware_watch&#x27;: True, &#x27;hostname&#x27;: &#x27;sd-42&#x27;, &#x27;id&#x27;: 42, &#x27;install_status&#x27;: &#x27;installed&#x27;, &#x27;ip&#x27;: [{&#x27;address&#x27;: &#x27;10.0.0.1&#x27;, &#x27;mac&#x27;: &#x27;01:23:45:67:89:ap&#x27;, &#x27;reverse&#x27;: &#x27;10-0-0-1.rev.poneytelecom.eu.&#x27;, &#x27;switch_port_state&#x27;: &#x27;up&#x27;, &#x27;type&#x27;: &#x27;public&#x27;}], &#x27;last_reboot&#x27;: &#x27;2020-06-21T12:28:16.000Z&#x27;, &#x27;location&#x27;: {&#x27;block&#x27;: &#x27;A&#x27;, &#x27;datacenter&#x27;: &#x27;DC3&#x27;, &#x27;position&#x27;: 15, &#x27;rack&#x27;: &#x27;A20&#x27;, &#x27;room&#x27;: &#x27;4 4-5&#x27;}, &#x27;network&#x27;: {&#x27;ip&#x27;: [&#x27;10.0.0.1&#x27;], &#x27;ipfo&#x27;: [], &#x27;private&#x27;: []}, &#x27;offer&#x27;: &#x27;Store-1-S&#x27;, &#x27;os&#x27;: {&#x27;name&#x27;: &#x27;centos&#x27;, &#x27;version&#x27;: &#x27;7&#x27;}, &#x27;power&#x27;: &#x27;ON&#x27;, &#x27;proactive_monitoring&#x27;: False, &#x27;support&#x27;: &#x27;Basic service level&#x27;}, &#x27;...&#x27;]}</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

