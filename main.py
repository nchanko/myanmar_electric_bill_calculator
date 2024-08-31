import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from calculate_cost import calculate_househhold_cost, calculate_industrial_cost, format_number, calculate_percentage_change
import json

def main():
    st.set_page_config(layout="wide")
    
    # Load translation dictionary from JSON file
    with open("translations.json", "r", encoding="utf-8") as file:
        translations = json.load(file)

    # Language selection
    language = st.sidebar.selectbox("Choose Language", options=["Burmese", "English"])
    t = translations[language]

    col1, col2 = st.columns([1, 5])

    with col2:
        # Display title
        st.markdown(f"<h1 style='color: #000080;'>{t['title']}</h1>", unsafe_allow_html=True)

    with col1:
        # Display QR code
        st.image("qrcode.png", width=100)

    col1, col2 = st.columns([1, 4])
    
    with col1:
        # Dropdown to select Household or Industrial
        use_type = st.selectbox(t["select_usage_type"], options=["Household", "Industrial"])
    with col2:
        # Input for units used
        units = st.number_input(t["units_input"], min_value=0, step=1)

    # Initialize variables
    period_keys = ["period_1", "period_2", "period_3"]
    costs_and_breakdowns = []
    costs = []

    if units > 0:
        if use_type == "Household":
            costs_and_breakdowns = [calculate_househhold_cost(units, period_key) for period_key in period_keys]
        else:  # Industrial
            costs_and_breakdowns = [calculate_industrial_cost(units, period_key) for period_key in period_keys]

        costs = [item[0] for item in costs_and_breakdowns]

        # Create two columns: one for the scorecard and cost breakdown, another for the chart
        col1, col2 = st.columns([1, 3])

        with col1:
            # Display scorecard for period_3 only
            period_label = t[period_keys[2]]  # Only display Period 3 in the scorecard
            st.metric(period_label, f"{format_number(costs[2])} MMK")

            # Cost breakdown explanation
            if costs_and_breakdowns:
                st.markdown(f"<h4 style='text-align: center; color: #000080;'>{t['cost_breakdown_title']}</h4>", unsafe_allow_html=True)
                for period_key, (cost, breakdown) in zip(period_keys, costs_and_breakdowns):
                    period_label = t[period_key]
                    with st.expander(f"{period_label}"):
                        for line in breakdown:
                            st.write(line)

        with col2:
            if costs:
                # Comparison chart including all periods
                fig = go.Figure(data=[
                    go.Bar(name=t[period_key], x=[t[period_key]], y=[cost]) for period_key, cost in zip(period_keys, costs)
                ])
                fig.update_layout(
                    title=t["comparison_chart_title"],
                    xaxis_title=t["period_xaxis_title"],  # Add a title to the x-axis
                    yaxis_title=t["cost_yaxis_title"],
                    yaxis=dict(tickformat=",.0f"),
                    template="simple_white",
                    title_x=0.1,
                    title_font=dict(size=24, color='#000080'),
                    width=800,  # Set the width of the chart
                    height=350  # Set the height of the chart
                )
                st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.markdown(
        "<p style='color: #7F00FF; text-align: center;'>💡 Concept by NLM,  🛠️ Built by NCKK</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
