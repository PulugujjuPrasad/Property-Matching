# Property Matching Engine

An AI-powered real estate matching system that connects users to properties based on weighted preferences and hard constraints.

## 🚀 Quick Start

### 1. Prerequisites
You need **Python 3.10+** installed on your machine. Download it from [python.org](https://www.python.org/).

### 2. Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd "Property Matching with User Preferences"

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the Engine
```bash
python main.py
```

## 🛠️ How it Works
The engine uses a two-stage pipeline:
1. **Hard Filtering:** Removes properties that don't meet mandatory criteria (e.g., Budget, Min Bedrooms).
2. **Weighted Scoring:** Uses a vectorized dot-product of User Preference Weights and Normalized Property Features to rank the best matches.

## 📁 Project Structure
- `main.py`: The core matching logic.
- `requirements.txt`: Necessary Python libraries.
- `Documentation/`: Detailed BRD, PRD, and Technical Strategy.
- `Case Study 2 Data (1).xlsx`: The property dataset.
