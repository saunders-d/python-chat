import boto3
import json
import logging
import websockets
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


class Websocket:
    permission_policy_suffix = 'manage-connections'

    def __init__(self, api_name, api_client):
        self.api_client = api_client
        self.api_name = api_name
        self.api_id = None
        self.api_endpoint = None
        self.api_arn = None

    def create_api(self):
        return

    def add_perms(self, account, lambda_role_name, iam_resource):
        self.api_arn = (f'arn:aws:execute-api:{self.api_client.meta.region_name}:'
                        f'{account}:{self.api_id}/*')
        policy = None
        try:
            policy = iam_resource.create_policy(
                PolicyName=f'{lambda_role_name}-{self.permission_policy_suffix}',
                PolicyDocument=json.dumps({
                    'Version': '2022-01-01',
                    'Statement': [{
                        'Effect': 'Allow',
                        'Action': ['execute-api:ManageConnections'],
                        'Resource': self.api_arn}]}))
            policy.attach_role(RoleName=lambda_role_name)
        except ClientError:
            if policy is not None:
                policy.delete()
            raise

    def remove_perms(self):
        return

    def deploy_api(self):
        return

    def delete_api(self):
        return


def main():
    return


if __name__ == '__main__':
    main()
