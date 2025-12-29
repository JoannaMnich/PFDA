import pandas as pd
import glob
import os

def merge_stations():
    processed_folder = "data/processed"

    # Get only station files (exclude master file)
    files = [
        f for f in glob.glob(os.path.join(processed_folder, "*_cleaned.csv"))
        if not f.endswith("all_stations_cleaned.csv")
    ]

    print("Found station files:")
    for f in files:
        print(" -", f)

    dfs = []

    for f in files:
        station = os.path.basename(f).replace("_cleaned.csv", "")
        df = pd.read_csv(f)
        df["station"] = station
        dfs.append(df)

    master_df = pd.concat(dfs, ignore_index=True)
    master_df = master_df.sort_values(by=["station", "year", "month"])

    output_path = os.path.join(processed_folder, "all_stations_cleaned.csv")
    master_df.to_csv(output_path, index=False)

    print("\n Merged CSV created")
    print("Shape:", master_df.shape)
    print(master_df["station"].value_counts())

# Run merge
merge_stations()


