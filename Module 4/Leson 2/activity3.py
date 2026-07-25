counry_codes = {
    "Bangladesh":"BD",
    "India":"IN",
    "Pakistan":"PK",
    "Bhutan": "BT"
}
print(counry_codes.get("Bangladesh", "Country not found"))
print(counry_codes.get("Nepal", "Country not found"))