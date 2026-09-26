# Cybersecurity Asset Inventory System
# Weekly Mini Project - 01

assets = []

n = int(input("Enter number of assets: "))

for i in range(n):
    print("\nAsset", i + 1)
    asset = {}
    asset["id"] = input("Asset ID: ")
    asset["name"] = input("Asset Name: ")
    asset["type"] = input("Asset Type: ")
    asset["ip"] = input("IP Address: ")
    asset["os"] = input("Operating System: ")
    asset["dept"] = input("Department: ")
    asset["risk"] = input("Risk Level: ")
    asset["status"] = input("Security Status: ")
    assets.append(asset)

print("\n" + "=" * 41)
print(" CYBERSECURITY ASSET INVENTORY")
print("=" * 40)

for asset in assets:
    print("Asset ID    :", asset["id"])
    print("Asset Name  :", asset["name"])
    print("Asset Type  :", asset["type"])
    print("IP Address  :", asset["ip"])
    print("OS          :", asset["os"])
    print("Department  :", asset["dept"])
    print("Risk Level  :", asset["risk"])
    print("Status      :", asset["status"])
    print("-" * 41)

critical = 0
high = 0
medium = 0
vulnerable = 0

for asset in assets:
    if asset["risk"] == "Critical":
        critical += 1
    elif asset["risk"] == "High":
        high += 1
    elif asset["risk"] == "Medium":
        medium += 1
    if asset["status"] == "Vulnerable":
        vulnerable += 1

print("=" * 41)
print("Total Assets        :", len(assets))
print("Critical Assets     :", critical)
print("High Risk Assets    :", high)
print("Medium Risk Assets  :", medium)
print("Vulnerable Assets   :", vulnerable)
print("=" * 41)