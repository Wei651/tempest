#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_serialization import jsonutils as json

from tempest.common import service_client


class RolesClient(service_client.ServiceClient):
    api_version = "v2.0"

    def create_role(self, **kwargs):
        """Create a role.

        Available params: see http://developer.openstack.org/
                              api-ref-identity-v2-ext.html#createRole
        """
        post_body = json.dumps({'role': kwargs})
        resp, body = self.post('OS-KSADM/roles', post_body)
        self.expected_success(200, resp.status)
        body = json.loads(body)
        return service_client.ResponseBody(resp, body)

    def show_role(self, role_id):
        """Get a role by its id."""
        resp, body = self.get('OS-KSADM/roles/%s' % role_id)
        self.expected_success(200, resp.status)
        body = json.loads(body)
        return service_client.ResponseBody(resp, body)

    def delete_role(self, role_id):
        """Delete a role."""
        resp, body = self.delete('OS-KSADM/roles/%s' % str(role_id))
        self.expected_success(204, resp.status)
        return resp, body

    def list_user_roles(self, tenant_id, user_id):
        """Returns a list of roles assigned to a user for a tenant."""
        url = '/tenants/%s/users/%s/roles' % (tenant_id, user_id)
        resp, body = self.get(url)
        self.expected_success(200, resp.status)
        body = json.loads(body)
        return service_client.ResponseBody(resp, body)

    def assign_user_role(self, tenant_id, user_id, role_id):
        """Add roles to a user on a tenant."""
        resp, body = self.put('/tenants/%s/users/%s/roles/OS-KSADM/%s' %
                              (tenant_id, user_id, role_id), "")
        self.expected_success(200, resp.status)
        body = json.loads(body)
        return service_client.ResponseBody(resp, body)

    def delete_user_role(self, tenant_id, user_id, role_id):
        """Removes a role assignment for a user on a tenant."""
        resp, body = self.delete('/tenants/%s/users/%s/roles/OS-KSADM/%s' %
                                 (tenant_id, user_id, role_id))
        self.expected_success(204, resp.status)
        return service_client.ResponseBody(resp, body)

    def list_roles(self):
        """Returns roles."""
        resp, body = self.get('OS-KSADM/roles')
        self.expected_success(200, resp.status)
        body = json.loads(body)
        return service_client.ResponseBody(resp, body)
