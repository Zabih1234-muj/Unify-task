import json
from datetime import datetime

# IMPLEMENT: function to convert ISO timestamps to milliseconds
def iso_to_millis(iso_string):
    # Parse the ISO timestamp into a datetime object
    dt = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%SZ")
    # Convert datetime to UNIX epoch time in ms
    return int(dt.timestamp() * 1000)

# IMPLEMENT: function to unify records
def unify_records(records):
    unified = []
    for rec in records:
        # Handle ISO string timestamps
        if isinstance(rec["timestamp"], str):
            ts = iso_to_millis(rec["timestamp"])
        # Already in milliseconds
        else:
            ts = rec["timestamp"]

        # Build target format
        unified.append({
            "timestamp": ts,
            "value": rec["value"]
        })
    return unified

if __name__ == "__main__":
    # Load both datasets
    with open("data-1.json") as f1, open("data-2.json") as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    # Merge + unify
    result = unify_records(data1 + data2)

    # Save output
    with open("output.json", "w") as fout:
        json.dump(result, fout, indent=2)

    print("✅ Transformation complete! Check output.json")
