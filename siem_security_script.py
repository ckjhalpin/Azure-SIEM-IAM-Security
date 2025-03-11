import json
import logging
from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.subscription import SubscriptionClient

# ✅ Authenticate with Azure
credential = DefaultAzureCredential()

# ✅ Get subscription ID dynamically
subscription_client = SubscriptionClient(credential)
subscription_id = next(subscription_client.subscriptions.list()).subscription_id

# ✅ Initialize Azure Authorization Client
auth_client = AuthorizationManagementClient(credential, subscription_id)

# ✅ Map role GUIDs to human-readable names
role_mapping = {
    "8e3af657-a8ff-443c-a75c-2fe8c4bcb635": "Owner",
    "b24988ac-6180-42a0-ab88-20f7382dd24c": "Contributor"
    # Add more role IDs if needed
}

def get_role_name(role_definition_id):
    """Fetch the actual role name from the role GUID."""
    role_guid = role_definition_id.split("/")[-1]
    return role_mapping.get(role_guid, f"Unknown Role ({role_guid})")

def check_iam_roles():
    print("🔍 Scanning IAM roles...")

    role_assignments = auth_client.role_assignments.list_for_scope(scope=f"/subscriptions/{subscription_id}")
    found_roles = False

    for role in role_assignments:
        role_name = get_role_name(role.role_definition_id)  # Convert GUID to role name
        principal_name = getattr(role, "principal_name", role.principal_id)

        print(f"📢 Found role: {role_name} assigned to {principal_name}")

        if role_name in ["Owner", "Contributor"]:
            alert_message = f"⚠️ HIGH RISK: {principal_name} has {role_name} role!"
            print(alert_message)
            logging.warning(alert_message)
            found_roles = True

    if not found_roles:
        print("✅ No high-risk IAM roles found.")

# ✅ Run the function
check_iam_roles()
