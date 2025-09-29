
# TMDB Movie Data Analysis with PySpark

## Project Overview
This project analyzes movie data from The Movie Database (TMDB) API using PySpark. It includes data extraction, cleaning, transformation, and analysis of key performance metrics for movies.

## Features
- 📦 API data extraction from TMDB
- 🧹 Data cleaning and preprocessing pipeline
- 📊 Key performance indicator (KPI) analysis
- 🎞️ Franchise vs standalone movie comparison
- 📈 Data visualization using PySpark and other libraries

## Prerequisites
- Python 3.8+
- Apache Spark with PySpark
- A TMDB API Key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tmdb-movie-analysis.git
   cd tmdb-movie-analysis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your TMDB API key (see **Configuration** below)

---

## Configuration

### Option 1: JSON Configuration File (Recommended)
1. Get a free API key from [TMDB](https://www.themoviedb.org/documentation/api).
2. Create a file at `config/api_config.json` with the following contents:
   ```json
   {
       "api_key": "your_actual_api_key_here"
   }
   ```
3. Ensure `config/api_config.json` is listed in `.gitignore`.

### Option 2: Environment Variables
1. Create a `.env` file:
   ```env
   TMDB_API_KEY=your_actual_api_key_here
   ```
2. Add `.env` to your `.gitignore`.

3. In your code:
   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()
   API_KEY = os.getenv('TMDB_API_KEY')
   ```

### Option 3: Command Line Argument
```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--api-key', required=True)
args = parser.parse_args()

API_KEY = args.api_key
```

---

## Usage

### For Exploration
Run the Jupyter notebook:
```bash
jupyter notebook notebooks/tmdb_analysis.ipynb
```

### For Production
Execute the main PySpark script:
```bash
spark-submit src/main.py
```

---

## Project Structure
```
tmdb-movie-analysis/
│
├── data/             # Raw and processed data
├── notebooks/        # Jupyter notebooks for exploratory analysis
├── src/              # Source code and pipeline scripts
├── visuals/          # Project Visuals
├── .gitignore        # Files to ignore in version control
├── requirements.txt  # Project dependencies
└── README.md         # Project overview and documentation
```
![Visuals](visuals/PySpark-Movie-Data-Analysis-Visuals.png)

---

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

## License
This project is licensed under the MIT License.

---

## .gitignore Highlights

**Sensitive Files**
```
config/api_config.json
.env
```

**Python**
```
__pycache__/
*.py[cod]
*$py.class
```

**Jupyter Notebooks**
```
.ipynb_checkpoints/
```

**Data**
```
data/raw/
data/processed/
```

**Virtual Environments**
```
venv/
env/
```

**Spark**
```
spark-warehouse/
derby.log
```

**System & IDE**
```
.DS_Store
.vscode/
.idea/
```

---

## How to Handle API Keys Securely

### Best Practices
1. **Never commit API keys to source control.**
2. **Use config files or environment variables** (and make sure they are in `.gitignore`).
3. **Use secure channels for team collaboration.**
4. **Use secret management tools for production environments.**

### If You Accidentally Commit a Key
1. **Revoke and regenerate the key immediately.**
2. **Remove it from git history:**
   ```bash
   git filter-branch --force --index-filter    "git rm --cached --ignore-unmatch config/api_config.json"    --prune-empty --tag-name-filter cat -- --all
   ```

