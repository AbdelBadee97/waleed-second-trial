# Data Explorer with Streamlit

This repository contains a Streamlit app for interactive data exploration and visualization.

## Files

- `streamlit_app.py` — Main Streamlit application.
- `data/your_data.csv` — Place your CSV dataset here.
- `requirements.txt` — Python dependencies.
- `README.md` — This file.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running Locally

```bash
streamlit run streamlit_app.py
```

## Deployment

- **Streamlit Community Cloud**: Connect this GitHub repo and set `streamlit_app.py` as the entry point.
- **Other Platforms**: Heroku, Azure, etc., following their deployment guides.
