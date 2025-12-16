import streamlit as st
from news_fetcher import fetch_news
#
# Page config - must be first!
st.set_page_config(page_title="Critical Minerals Tracker", page_icon="🔋", layout="wide")
# ClearPath brand styling - light theme
st.markdown("""
<style>
    /* White background */
    .stApp {
        background-color: #FFFFFF;
    }
    
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
    
    /* Subheaders */
    h2, h3 {
        color: #193D69;
    }
    
    /* Links */
    a {
        color: #9D1C20 !important;
    }
</style>
""", unsafe_allow_html=True)
# Fake news data
news_items = fetch_news()

# SIDEBAR - filters go here
st.sidebar.title("🔋 Filters")
minerals = ["All", "Lithium", "Cobalt", "Nickel", "Copper", "Rare Earth", "Graphite"]
selected_mineral = st.sidebar.selectbox("Mineral:", minerals)

sources = ["All"] + sorted(list(set([item["source"] for item in news_items])))
selected_source = st.sidebar.selectbox("Source:", sources)

# MAIN AREA
st.image("https://clearpath.org/wp-content/themes/theme starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter starter/assets/images/logo.svg", width=200)
st.image("https://clearpath.org/wp-content/uploads/sites/44/2023/08/clearpath-logo.png", width=200)
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
        st.caption(f"🔋 {item['mineral']} | 📰 {item['source']} | 📅 {item['date']}")
        st.markdown(f"[Read more]({item['link']})")
    st.divider() 