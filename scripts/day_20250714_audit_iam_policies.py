import boto3

def list_user_policies():
    iam = boto3.client('iam')

    users = iam.list_users()['Users']
    print(f"Found {len(users)} IAM users.\n")

    for user in users:
        username = user['UserName']
        print(f"👤 User: {username}")

        # Managed Policies
        attached_policies = iam.list_attached_user_policies(UserName=username)['AttachedPolicies']
        if attached_policies:
            print("  🔒 Attached Managed Policies:")
            for policy in attached_policies:
                print(f"    - {policy['PolicyName']}")
        else:
            print("  🔒 Attached Managed Policies: None")

        # Inline Policies
        inline_policies = iam.list_user_policies(UserName=username)['PolicyNames']
        if inline_policies:
            print("  📝 Inline Policies:")
            for policy_name in inline_policies:
                print(f"    - {policy_name}")
        else:
            print("  📝 Inline Policies: None")

        print()

if __name__ == "__main__":
    list_user_policies()
