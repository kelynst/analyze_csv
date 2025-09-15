import pandas as pd

def analyze_csv():
    fname = input("Enter CSV file name (e.g., musicdata.csv): ").strip()

    try:
        # Load the CSV into a DataFrame
        df = pd.read_csv(fname)

        # -- Console Output --
        print("\nCSV Analysis")
        print("---------------")
        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")

        print("\nColumn Names:")
        print(df.columns.tolist())

        print("\nFirst 5 Rows:")
        print(df.head())

        # Summary stats (numeric + text)
        print("\nNumeric Summary (df.describe()):")
        if df.select_dtypes(include="number").shape[1] > 0:
            print(df.describe())
        else:
            print("(No numeric columns found.)")

        print("\nText / Categorical Summary (counts):")
        if df.select_dtypes(include=["object", "category"]).shape[1] > 0:
            print(df.describe(include=["object", "category"]))
        else:
            print("(No text/categorical columns found.)")

        # -- Save Outputs --
        # 1) Basic metrics to a simple 2-column CSV
        summary_rows = [
            {"metric": "rows", "value": df.shape[0]},
            {"metric": "columns", "value": df.shape[1]},
            {"metric": "column_names", "value": ", ".join(df.columns.astype(str))}
        ]
        summary_df = pd.DataFrame(summary_rows)
        summary_df.to_csv("analysis_summary.csv", index=False)

        # 2) Numeric describe() to a CSV (if there are numeric columns)
        if df.select_dtypes(include="number").shape[1] > 0:
            df.describe().to_csv("summary_stats.csv")
        else:
            # Make an empty placeholder with a note
            pd.DataFrame({"note": ["No numeric columns to summarize."]}).to_csv(
                "summary_stats.csv", index=False
            )

        print("\n Saved:")
        print(" - analysis_summary.csv  (basic metrics + column names)")
        print(" - summary_stats.csv     (numeric describe() table or a note)")

    except FileNotFoundError:
        print("File not found. Please check the name and try again.")

    except pd.errors.EmptyDataError:
        print("The file is empty. Please provide a CSV with data.")

    except pd.errors.ParserError:
        print("That file is not a valid CSV. Please check the format.")

    except Exception as e:
        # Catch-all for anything unexpected
        print(f" Something went wrong: {e}")

if __name__ == "__main__":
    analyze_csv()