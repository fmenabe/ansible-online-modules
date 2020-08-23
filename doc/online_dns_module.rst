.. _online_dns_module:


online_dns -- Manage DNS zone of a domain
+++++++++++++++++++++++++++++++++++++++++



Synopsis
--------
- Create/update/delete a DNS record of a zone.
- Online API manage versions for DNS zones. A new version is created each time the zone changes.
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
                    <div class="ansibleOptionAnchor" id="parameter-data"></div>
                    <b>data</b>
                    <a class="ansibleOptionLink" href="#parameter-data" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Value of the record.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-domain_name"></div>
                    <b>domain_name</b>
                    <a class="ansibleOptionLink" href="#parameter-domain_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Domain to update.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the entry.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-priority"></div>
                    <b>priority</b>
                    <a class="ansibleOptionLink" href="#parameter-priority" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Priority of the record.</div>
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
                                            <div>Whether to delete or create the key to Online.net account.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ttl"></div>
                    <b>ttl</b>
                    <a class="ansibleOptionLink" href="#parameter-ttl" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">14400</div>
                                    </td>
                                                                <td>
                                            <div>TTL of the record.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>A</li>
                                                                                                                                                                                                <li>AAAA</li>
                                                                                                                                                                                                <li>CNAME</li>
                                                                                                                                                                                                <li>MX</li>
                                                                                                                                                                                                <li>TXT</li>
                                                                                                                                                                                                <li>SRV</li>
                                                                                                                                                                                                <li>TLSA</li>
                                                                                                                                                                                                <li>NS</li>
                                                                                                                                                                                                <li>PTR</li>
                                                                                                                                                                                                <li>CAA</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of the record.</div>
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

    
    - name: Create A record for 'awesome.example.org'
      delegate_to: localhost
      online_dns:
        api_token: <FIXME>
        domain_name: example.org
        name: awesome
        type: A
        data: <IP>
        ttl: 14400
        state: present

    - name: Create CNAME 'incredible.example.org' to 'awesome.example.org'
      delegate_to: localhost
      online_dns:
        api_token: <FIXME>
        domain_name: example.org
        name: incredible
        type: CNAME
        data: awesome.example.org
        ttl: 60

    # Create a TXT record for 'acme_certificate' challenge
    - name: Create a challenge for the domain
      delegate_to: localhost
      acme_certificate:
        acme_version: 2
        acme_directory: https://acme-v02.api.letsencrypt.org/directory
        account_key_src: "<ACCOUNT_KEY>"
        challenge: dns-01
        src: "<CSR_PATH>"
        dest: "<CERT_PATH>"
      register: challenge

    - name: Create required DNS TXT record for challenge
      delegate_to: localhost
      online_dns:
        api_token: <FIXME>
        state: present
        name: "{{ challenge.challenge_data[<CERT_DOMAIN>]['dns-01'].record  }}"
        type: TXT
        data: "{{ challenge.challenge_data[<CERT_DOMAIN>]['dns-01'].resource_value }}"




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
                    <div class="ansibleOptionAnchor" id="return-records"></div>
                    <b>records</b>
                    <a class="ansibleOptionLink" href="#return-records" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on sucess</td>
                <td>
                                                                        <div>Records of the version.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;name&#x27;: &#x27;store1-s.fmenabe.me.&#x27;, &#x27;data&#x27;: &#x27;62.210.132.60&#x27;, &#x27;type&#x27;: &#x27;A&#x27;, &#x27;ttl&#x27;: 86400, &#x27;priority&#x27;: -1, &#x27;domain_name&#x27;: &#x27;fmenabe.me.&#x27;}, {&#x27;name&#x27;: &#x27;...&#x27;}]</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-version"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#return-version" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">-</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Name of the activated version (the new version in case of update owtherwise the currently active version).</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">MrRobot_WU2fyEd9</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

