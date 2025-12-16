import streamlit as st
#
# Page config - must be first!
st.set_page_config(page_title="Critical Minerals Tracker", page_icon="🔋", layout="wide")
# ClearPath brand styling
st.markdown("""
<style>
    /* Main header */
    .stApp h1 {
        color: #193D69;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #193D69;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Info boxes (relevance tags) */
    .stAlert {
        background-color: #EFEFEF;
        border-left-color: #9D1C20;
    }
    
    /* Metric styling */
    [data-testid="stMetricValue"] {
        color: #193D69;
    }
</style>
""", unsafe_allow_html=True)
# Fake news data
news_items = [
    {"mineral": "Lithium", "headline": "New lithium deposit found in Nevada", "source": "Reuters", "date": "Dec 16, 2025", "relevance": "Domestic supply"},
    {"mineral": "Cobalt", "headline": "Congo cobalt exports hit record high", "source": "Bloomberg", "date": "Dec 15, 2025", "relevance": "Supply chain"},
    {"mineral": "Rare Earths", "headline": "DOE announces rare earth processing grant", "source": "E&E News", "date": "Dec 15, 2025", "relevance": "DOE policy"},
    {"mineral": "Lithium", "headline": "Tesla signs lithium supply deal", "source": "WSJ", "date": "Dec 14, 2025", "relevance": "Industry"},
    {"mineral": "Nickel", "headline": "Indonesia nickel ban impacts EV market", "source": "Financial Times", "date": "Dec 14, 2025", "relevance": "Trade policy"},
    {"mineral": "Copper", "headline": "Arizona copper mine receives permit approval", "source": "Mining Weekly", "date": "Dec 13, 2025", "relevance": "Permitting"},
    {"mineral": "Graphite", "headline": "US graphite facility breaks ground in Louisiana", "source": "S&P Global", "date": "Dec 12, 2025", "relevance": "Domestic supply"},
]

# SIDEBAR - filters go here
st.sidebar.title("🔋 Filters")
minerals = ["All"] + sorted(list(set([item["mineral"] for item in news_items])))
selected_mineral = st.sidebar.selectbox("Mineral:", minerals)

sources = ["All"] + sorted(list(set([item["source"] for item in news_items])))
selected_source = st.sidebar.selectbox("Source:", sources)

# MAIN AREA
st.title("Critical Minerals News Tracker")
st.write("Daily intelligence for ClearPath policy team")

# Filter the data
filtered = []
for item in news_items:
    mineral_match = (selected_mineral == "All" or item["mineral"] == selected_mineral)
    source_match = (selected_source == "All" or item["source"] == selected_source)
    if mineral_match and source_match:
        filtered.append(item)

# Show count
st.metric("Articles Found", len(filtered))

# Display results
for item in filtered:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader(item["headline"])
        st.caption(f"🏷️ {item['mineral']} | 📰 {item['source']} | 📅 {item['date']}")
    with col2:
        st.info(item["relevance"])
    st.divider()