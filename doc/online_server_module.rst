.. _online_server_module:


online_server -- Deploy/update/reboot/terminate a server
++++++++++++++++++++++++++++++++++++++++++++++++++++++++



Synopsis
--------
- Update informations, launch installation, reboot or terminate a server.
- Terminating a server seems to end subscription for it according to the documentation. It has not been tested yet!



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
                    <div class="ansibleOptionAnchor" id="parameter-hostname"></div>
                    <b>hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-hostname" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Hostname of the server.</div>
                                            <div>This is configured in the Online console but it does not set the hostname of the server.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-install"></div>
                    <b>install</b>
                    <a class="ansibleOptionLink" href="#parameter-install" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to launch an installation.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-os"></div>
                    <b>os</b>
                    <a class="ansibleOptionLink" href="#parameter-os" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Operating system to use for the installation.</div>
                                            <div>Use <span class='module'>online_os_info</span> or make a GET call to <em>/server/operatingSystems/{server_id}</em> for retrieving available operating systems.</div>
                                            <div>Name, not id, of the operating system must be used.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-panel_password"></div>
                    <b>panel_password</b>
                    <a class="ansibleOptionLink" href="#parameter-panel_password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Password for panel.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-partitioning"></div>
                    <b>partitioning</b>
                    <a class="ansibleOptionLink" href="#parameter-partitioning" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>How to partition disks.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-root_password"></div>
                    <b>root_password</b>
                    <a class="ansibleOptionLink" href="#parameter-root_password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Password for the <em>root</em> account.</div>
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
                                            <div>Id of the server.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ssh_keys"></div>
                    <b>ssh_keys</b>
                    <a class="ansibleOptionLink" href="#parameter-ssh_keys" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of SSH key ids.</div>
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
                                                                                                                                                                                                <li>stopped</li>
                                                                                                                                                                                                <li>rebooted</li>
                                                                                                                                                                                                <li>terminated</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Final state of the server.</div>
                                            <div>Use <em>install=yes</em> to (re)install a server.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-user_login"></div>
                    <b>user_login</b>
                    <a class="ansibleOptionLink" href="#parameter-user_login" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Username of the local user.</div>
                                            <div>Installation required to set a local user.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-user_password"></div>
                    <b>user_password</b>
                    <a class="ansibleOptionLink" href="#parameter-user_password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Password of the local user.</div>
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

    
    - name: Retrieve server informations
      online_server:
        api_token: <FIXME>
        server_id: 99999
        state: present
      register: result
    - debug: var=result.server_info

    # Install a server
    - name: Ensure SSH public key of the controller user exists
      online_key:
        api_token: <FIXME>
        # generate <USER>@<HOSTNAME>
        description: "{{ lookup('pipe', 'whoami') }}@{{ lookup('pipe', 'hostname') }}"
        key: "{{ lookup('file', '~/.ssh/id_rsa.pub'|expanduser) }}"
        state: present
      register: ssh_key

    - name: "(Re)Install a server"
      online_server:
        api_token: <FIXME>
        server_id: 99999
        state: present
        install: yes
        hostname: awesome
        os: Centos 7
        user_login: myuser
        user_password: CHANGEME
        root_password: CHANGEME
        panel_password: CHANGEME
        ssh_keys:
        - {{ ssh_key.key_id }}
        partitioning:
          A:
            type: [P, P, P]
            fstype: [xfs, swap, xfs]
            mount: [/boot, '', /]
            size: [300, 1024, 952542]
      register: result
    - debug: var=result.online_os_info

    # Reboot server
    - name: Reboot server
      online_server:
        api_token: <FIXME>
        server_id: 99999
        state: rebooted

    # Shutdown server
    - name: Shutdown server
      online_server:
        api_token: <FIXME>
        server_id: 99999
        state: stopped




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
                    <div class="ansibleOptionAnchor" id="return-server_info"></div>
                    <b>server_info</b>
                    <a class="ansibleOptionLink" href="#return-server_info" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on sucess</td>
                <td>
                                            <div>Server informations return by /server/{server_id} API call.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;online_server_info&#x27;: {&#x27;abuse&#x27;: &#x27;abuse@example.com&#x27;, &#x27;anti_ddos&#x27;: False, &#x27;bmc&#x27;: {&#x27;session_key&#x27;: None}, &#x27;boot_mode&#x27;: &#x27;normal&#x27;, &#x27;contacts&#x27;: {&#x27;owner&#x27;: &#x27;foobar&#x27;, &#x27;tech&#x27;: &#x27;foobar&#x27;}, &#x27;disks&#x27;: [{&#x27;capacity&#x27;: 3815448, &#x27;connector&#x27;: &#x27;A&#x27;, &#x27;id&#x27;: 261223, &#x27;type&#x27;: &#x27;SATA&#x27;}], &#x27;drive_arrays&#x27;: [{&#x27;disks&#x27;: [{&#x27;capacity&#x27;: 3815448, &#x27;connector&#x27;: &#x27;A&#x27;, &#x27;id&#x27;: 261223, &#x27;type&#x27;: &#x27;SATA&#x27;}]}], &#x27;hardware_watch&#x27;: True, &#x27;hostname&#x27;: &#x27;sd-42&#x27;, &#x27;id&#x27;: 42, &#x27;install_status&#x27;: &#x27;installed&#x27;, &#x27;ip&#x27;: [{&#x27;address&#x27;: &#x27;10.0.0.1&#x27;, &#x27;mac&#x27;: &#x27;01:23:45:67:89:ap&#x27;, &#x27;reverse&#x27;: &#x27;10-0-0-1.rev.poneytelecom.eu.&#x27;, &#x27;switch_port_state&#x27;: &#x27;up&#x27;, &#x27;type&#x27;: &#x27;public&#x27;}], &#x27;last_reboot&#x27;: &#x27;2020-05-20T12:00:00.000Z&#x27;, &#x27;location&#x27;: {&#x27;block&#x27;: &#x27;A&#x27;, &#x27;datacenter&#x27;: &#x27;DC3&#x27;, &#x27;position&#x27;: 15, &#x27;rack&#x27;: &#x27;A18&#x27;, &#x27;room&#x27;: &#x27;4 5-4&#x27;}, &#x27;network&#x27;: {&#x27;ip&#x27;: [&#x27;10.0.0.1&#x27;], &#x27;ipfo&#x27;: [], &#x27;private&#x27;: []}, &#x27;offer&#x27;: &#x27;Store-1-S&#x27;, &#x27;os&#x27;: {&#x27;name&#x27;: &#x27;centos&#x27;, &#x27;version&#x27;: &#x27;7&#x27;}, &#x27;power&#x27;: &#x27;ON&#x27;, &#x27;proactive_monitoring&#x27;: False, &#x27;support&#x27;: &#x27;Basic service level&#x27;}}</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

