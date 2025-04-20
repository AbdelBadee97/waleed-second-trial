import streamlit as st
import pandas as pd

# 1. Load your data (drop or adjust skiprows/header if you have metadata rows)
@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

df = load_data("data/your_data.csv")

st.set_page_config(
    page_title="Data Explorer",
    layout="wide",
)

st.title("🔍 Interactive Data Explorer")

# 2. Sidebar filters
st.sidebar.header("Filters")
df_filtered = df.copy()

for col in df.columns:
    col_data = df[col]
    # numeric filter
    if pd.api.types.is_numeric_dtype(col_data):
        min_val = float(col_data.min())
        max_val = float(col_data.max())
        step = (max_val - min_val) / 100 if max_val != min_val else 1.0
        low, high = st.sidebar.slider(
            label=f"{col} range",
            min_value=min_val,
            max_value=max_val,
            value=(min_val, max_val),
            step=step,
        )
        df_filtered = df_filtered[df_filtered[col].between(low, high)]
    # datetime filter
    elif pd.api.types.is_datetime64_any_dtype(col_data):
        start, end = st.sidebar.date_input(
            label=f"{col} date range",
            value=(col_data.min(), col_data.max()),
        )
        df_filtered = df_filtered[df_filtered[col].between(pd.to_datetime(start), pd.to_datetime(end))]
    # categorical / text filter
    else:
        opts = list(col_data.dropna().unique())
        default = opts[:]  # all selected by default
        selection = st.sidebar.multiselect(
            label=f"Select {col}",
            options=opts,
            default=default,
        )
        df_filtered = df_filtered[df_filtered[col].isin(selection)]

# 3. Show filtered data
st.subheader(f"Filtered Data — {len(df_filtered):,} rows")
st.dataframe(df_filtered, use_container_width=True)

# 4. Example visualizations (customize as needed)
st.markdown("### 📊 Example Charts")
if "year" in df_filtered.columns and "pm25_concentration" in df_filtered.columns:
    chart_df = df_filtered.groupby("year")["pm25_concentration"].mean().reset_index()
    st.line_chart(chart_df.set_index("year"), height=300)

if "country_name" in df_filtered.columns and "no2_concentration" in df_filtered.columns:
    bar_df = (
        df_filtered.groupby("country_name")["no2_concentration"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    st.bar_chart(bar_df.set_index("country_name"), height=300)
