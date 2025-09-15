# 🎵 Analyze CSV  

A lightweight Python script for quickly exploring CSV datasets.  
This repo demonstrates **basic data analysis with Pandas**, using an included music dataset as an example.  

---

## 📌 Project Overview  
- **Goal** → Provide a simple tool for exploring CSV files (rows, columns, headers, and preview)  
- **Approach** → Load data with Pandas, display dataset structure, and preview rows  
- **Status** → Beginner-friendly demo project, extendable for more advanced analysis  

---

## 📂 Repo Structure  
analyze_csv/  
│── analyze_csv.py       # Main script  
│── requirements.txt     # Dependencies  
│── musicdata.csv        # Example dataset (Spotify recommendations)  
│── README.md            # Project documentation  

- **analyze_csv.py** → Script that loads and analyzes any CSV file.  
- **requirements.txt** → Python packages required to run the script.  
- **musicdata.csv** → Example dataset for testing.  
- **README.md** → This documentation file you’re reading.  

---

## 🚀 Getting Started  
Follow these steps to set up the project locally:  

### 1. 📥 Clone the repository  
Clone this repo from GitHub onto your local machine.  
```bash
git clone https://github.com/kelynst/analyze_csv.git
cd analyze_csv

### 2. 🌱 Create a virtual environment  
Set up an isolated Python environment for dependencies.  
```bash
python3 -m venv .venv

### 3. ⚡ Activate the virtual environment
Enable the environment so Python and pip use the local versions.

**macOS/Linux**
```bash
source .venv/bin/activate

**Windows(PowerShell)**
.venv\Scripts\Activate

### 4. 📦 Install dependencies  
Install the required Python packages listed in `requirements.txt`.  
```bash
pip install -r requirements.txt

### 5. ▶️ Run the script  
Run the Python script and enter the CSV file name when prompted.  

```bash
python analyze_csv.py

### 6. 📝 Example run  
Example using the included `musicdata.csv` file.  

```bash
python analyze_csv.py
Enter CSV file name: musicdata.csv

CSV Analysis
---------------
Rows: 2018
Columns: 19

Column Names:
['track_id', 'artists', 'album_name', 'track_name', ...]

First 5 Rows:
     track_id             artists        album_name      track_name
0  6rqhFgbbKwnb9MLmUQDhG6   Radiohead     OK Computer     No Surprises
1  ...


Future Improvements
	•	Add summary statistics (mean, median, mode)
	•	Handle large files with chunked reading
	•	Export preview results to JSON/CSV
	•	Include simple data visualizations

⸻

Requirements
	•	Python 3.9+
	•	Pandas

⸻

Contributing

Fork the repo and open pull requests with improvements (e.g., summary stats, visualization).

⸻

License

This project is licensed under the MIT License.