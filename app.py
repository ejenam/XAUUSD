# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Load the data
# df_2022 = pd.read_excel('trade_XAUUSD_2022.xlsx')
# df_2023 = pd.read_excel('trade_XAUUSD_2023.xlsx')
# df_2024 = pd.read_excel('trade_XAUUSD_2024.xlsx')

# # Convert time to datetime
# for df in [df_2022, df_2023, df_2024]:
#     df['time'] = pd.to_datetime(df['time'])

# # Create dictionary
# data_by_year = {
#     '2022': df_2022,
#     '2023': df_2023,
#     '2024': df_2024
# }

# # Streamlit app
# st.set_page_config(page_title="XAUUSD Balance Tracker", layout="wide")
# st.title("💰 XAUUSD Balance Tracker")

# # --- Sidebar Controls ---
# st.sidebar.header("⚙️ Settings")
# selected_year = st.sidebar.selectbox("Select Year", options=list(data_by_year.keys()), index=1)

# #theme_mode = st.sidebar.radio("Theme", options=["Light", "Dark"], index=1)

# # Choose plotly template based on theme
# #plotly_template = "plotly_dark" if theme_mode == "Dark" else "plotly_white"

# # --- Main chart ---
# df = data_by_year[selected_year]

# fig = px.line(
#     df,
#     x='time',
#     y='balance',
#     title=f'📈 Balance Over Time – {selected_year}',
#     markers=True,
#     labels={'balance': 'Balance (USD)', 'time': 'Time'},
#     template='plotly_dark'
# )
# fig.update_layout(title_x=0.5, hovermode='x unified')

# st.plotly_chart(fig, use_container_width=True)



# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # --- Page Config ---
# st.set_page_config(page_title="XAUUSD Balance Tracker", layout="wide")

# # --- Personal Info ---
# your_name = "Enemchukwu Victor Ejenam"
# your_bio = "Gold trader | Data-driven decision maker | XAUUSD enthusiast"
# profile_img = "me.jpg"  # Ensure this file is in the same directory

# # --- Profile Header ---
# col1, col2 = st.columns([1, 5])
# with col1:
#     st.image(profile_img, width=120)
# with col2:
#     st.markdown(f"## {your_name}")
#     st.markdown(f"**{your_bio}**")

# st.markdown("---")

# # --- Load Data ---
# df_2023 = pd.read_excel('trade_XAUUSD_2023.xlsx')
# df_2024 = pd.read_excel('trade_XAUUSD_2024.xlsx')

# for df in [df_2023, df_2024]:
#     df['time'] = pd.to_datetime(df['time'])

# data_by_year = {
#     '2023': df_2023,
#     '2024': df_2024
# }

# # --- Sidebar Controls ---
# st.sidebar.header("⚙️ Settings")
# selected_year = st.sidebar.selectbox("Select Year", options=list(data_by_year.keys()), index=1)
# theme_mode = st.sidebar.radio("Theme", options=["Light", "Dark"], index=1)
# plotly_template = "plotly_dark" if theme_mode == "Dark" else "plotly_white"

# # --- Plot ---
# df = data_by_year[selected_year]
# fig = px.line(
#     df,
#     x='time',
#     y='balance',
#     title=f'📈 Balance Over Time – {selected_year}',
#     markers=True,
#     labels={'balance': 'Balance (USD)', 'time': 'Time'},
#     template=plotly_template
# )
# fig.update_layout(title_x=0.5, hovermode='x unified')

# st.plotly_chart(fig, use_container_width=True)



import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Config ---
st.set_page_config(page_title="XAUUSD Dashboard", layout="wide")

# --- Personal Info ---
your_name = "Enemchukwu Victor Ejenam"
your_bio = "Gold trader | Data-driven decision maker | XAUUSD enthusiast"
profile_img = "me.jpg"  # Make sure this image is in the same folder

# --- Load Data ---
df_2018 = pd.read_excel('trade_XAUUSD_2018.xlsx')
df_2019 = pd.read_excel('trade_XAUUSD_2019.xlsx')
df_2020 = pd.read_excel('trade_XAUUSD_2020.xlsx')
df_2021 = pd.read_excel('trade_XAUUSD_2021.xlsx')
df_2022 = pd.read_excel('trade_XAUUSD_2022.xlsx')
df_2023 = pd.read_excel('trade_XAUUSD_2023.xlsx')
df_2024 = pd.read_excel('trade_XAUUSD_2024.xlsx')

for df in [df_2018, df_2019, df_2020, df_2021, df_2022, df_2023, df_2024]:
    df['time'] = pd.to_datetime(df['time'])

data_by_year = {
    '2018': df_2018,
    '2019': df_2019,
    '2020': df_2020,
    '2021': df_2021,
    '2022': df_2022,
    '2023': df_2023,
    '2024': df_2024
}

# --- Sidebar Navigation ---
st.sidebar.title("📁 Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Bio", "About"])


# --- DASHBOARD PAGE ---
# if page == "Dashboard":
#     st.title("💰 XAUUSD Balance Tracker")

#     # Sidebar settings
#     st.sidebar.markdown("---")
#     selected_year = st.sidebar.selectbox("Select Year", options=list(data_by_year.keys()), index=1)
#     theme_mode = st.sidebar.radio("Theme", options=["Light", "Dark"], index=1)
#     plotly_template = "plotly_dark" if theme_mode == "Dark" else "plotly_white"

#     # Plot
#     df = data_by_year[selected_year]
#     fig = px.line(
#         df,
#         x='time',
#         y='balance',
#         title=f'📈 Balance Over Time – {selected_year}',
#         markers=True,
#         labels={'balance': 'Balance (GBP)', 'time': 'Time'},
#         template=plotly_template
#     )
#     fig.update_layout(title_x=0.5, hovermode='x unified')

#     st.plotly_chart(fig, use_container_width=True)

if page == "Dashboard":
    st.title("💰 XAUUSD Trade Breakdown")

    # Sidebar settings
    st.sidebar.markdown("---")
    selected_year = st.sidebar.selectbox("Select Year", options=list(data_by_year.keys()), index=1)
    theme_mode = st.sidebar.radio("Theme", options=["Light", "Dark"], index=1)
    plotly_template = "plotly_dark" if theme_mode == "Dark" else "plotly_white"

    # Load data
    df = data_by_year[selected_year].copy()
    df['time'] = pd.to_datetime(df['time'])

    # Separate BUY and CLOSE
    buy_df = df[df['action'] == 'BUY'].reset_index(drop=True)
    close_df = df[df['action'] == 'CLOSE'].reset_index(drop=True)

    # Compute profit/loss per trade
    trade_pairs = pd.merge(buy_df, close_df, left_index=True, right_index=True, suffixes=('_buy', '_close'))
    trade_pairs['profit'] = (trade_pairs['price_close'] - trade_pairs['price_buy']) * trade_pairs['size_close']

    # Plot setup
    import plotly.subplots as sp
    import plotly.graph_objects as go

    fig = sp.make_subplots(rows=2, cols=1, shared_xaxes=True, 
                           vertical_spacing=0.1,
                           row_heights=[0.6, 0.4],
                           subplot_titles=("📈 Buy & Close Price", "💼 Balance Over Time"))

    # --- PRICE CHART (Row 1) ---
    fig.add_trace(go.Scatter(
        x=buy_df['time'],
        y=buy_df['price'],
        mode='markers',
        name='Buy Price',
        marker=dict(color='green', size=8, symbol='triangle-up')
    ), row=1, col=1)

    fig.add_trace(go.Scatter(
        x=close_df['time'],
        y=close_df['price'],
        mode='markers',
        name='Close Price',
        marker=dict(color='red', size=8, symbol='x')
    ), row=1, col=1)

    # Annotations for profit/loss per trade
    for i, row in trade_pairs.iterrows():
        profit_str = f"{row['profit']:.2f}"
        color = "limegreen" if row['profit'] >= 0 else "crimson"
        fig.add_annotation(
            x=row['time_close'],
            y=row['price_close'],
            text=f"${profit_str}",
            showarrow=True,
            arrowhead=2,
            font=dict(color=color),
            arrowcolor=color,
            row=1, col=1
        )

    # --- BALANCE CHART (Row 2) ---
    fig.add_trace(go.Scatter(
        x=close_df['time'],
        y=close_df['balance'],
        mode='lines+markers',
        name='Balance',
        line=dict(color='royalblue', width=2)
    ), row=2, col=1)

    # Final layout
    fig.update_layout(
        template=plotly_template,
        hovermode='x unified',
        height=700,
        margin=dict(l=40, r=40, t=60, b=40),
        showlegend=True,
        xaxis2_title="Time",
        yaxis_title="Price (USD)",
        yaxis2_title="Balance (GBP)"
    )

    st.plotly_chart(fig, use_container_width=True)




# --- BIO PAGE ---
# elif page == "Bio":
#     st.title("👤 About Me")

#     col1, col2 = st.columns([1, 3])
#     with col1:
#         st.image(profile_img, width=150)
#     with col2:
#         st.markdown(f"## {your_name}")
#         st.markdown(f"**{your_bio}**")
#         st.markdown("---")
#         st.markdown("📧 *You can reach me via Streamlit comments if deployed.*")

elif page == "Bio":
    st.title("👤 About Me")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("me.jpg", width=150)  # Update path if needed
    with col2:
        st.markdown("## Enemchukwu Victor Ejenam")
        st.markdown("""
        I'm a quantitative trader and machine learning engineer with a passion for data-driven systems and intelligent automation.

        ### 🧠 Background Summary:
        - MSc in Advanced Computer Science with Business from the University of Exeter
        - MSc in Petroleum & Environmental Engineering from Politecnico di Torino
        - Experience across AI, analytics, and energy optimization
        - Built advanced forecasting systems and deployed ML pipelines on Azure
        - AI/ML Engineer at EDATECH and Former Data Scientist at Atkins Réalis

        ### 🚀 Founder – ENV Capital:
        I started **ENV Capital**, a private trading and research firm focused on developing proprietary trading systems for volatile markets — with a particular focus on **XAUUSD** and FX pairs.

        My work blends traditional financial analysis with modern machine learning to create dynamic, adaptive strategies.

        """)
        st.markdown("📫 *For questions, feel free to reach out via LinkedIn.*")


# --- ABOUT PAGE ---
elif page == "About":
    st.title("📘 About the Trading System")
    st.markdown("""
    This project is a custom-built **algorithmic trading system** developed for precision trading on **XAUUSD**.

    ### 🔍 Key Highlights:
    - Combines machine learning and technical analysis
    - Uses multi-timeframe validation and market structure
    - Manages trades dynamically with context-aware risk logic
    - Includes optional hedging and extensive backtesting capabilities

    The system is tailored for data-driven decision making and ongoing refinement, focusing on consistency and edge preservation.
    """)



