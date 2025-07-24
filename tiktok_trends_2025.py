import streamlit as st

st.set_page_config(page_title="TikTok Trend Watch", layout="centered")

st.title(" TikTok Fun Fact + Trend Watch")
st.caption("Updated Daily • Curated by Jane Emmanuel")

# --- Section 1: Fun Fact of the Day ---
st.header(" Fun Fact of the Day")
st.success("Connie Francis' 1962 song **'Pretty Little Baby'** is going viral again on TikTok with **600K+ videos daily**, reviving a 63-year-old classic.")

# --- Section 2: Top 5 TikTok Sounds Today ---
st.header(" Top 5 TikTok Sounds Today")

top_sounds = [
    "Show Me Love – WizTheMc & Bees & Honey",
    "There She Goes – CYRIL remix",
    "Blue – Yung Kai",
    "My World – Chuckyy",
    "Shake It to the Max (Fly) – Moliy & Silent Addy remix"
]

# Initialize vote counts in session_state
if "votes" not in st.session_state:
    st.session_state.votes = {sound: 0 for sound in top_sounds}

selected_sound = st.radio(" Vote for your favorite TikTok sound:", top_sounds)

if st.button("Vote"):
    st.session_state.votes[selected_sound] += 1
    st.success(f"✅ You voted for: {selected_sound}")

st.subheader(" Live Voting Results")
for sound, count in st.session_state.votes.items():
    st.write(f"{sound}: **{count}** votes")

# --- Section 3: Global TikTok Trends ---
st.header("🌍 Global Trends to Watch")
st.markdown("""
- **#heatwave** is blowing up with 46K+ new posts today  
- **#summer2025** and **#vocation** trending in lifestyle/travel niches  
- Viral skits still love: *“POV: You forgot your charger in Lagos traffic”*  
- Filter trend: *Neon outline art effect*  
""")

# --- Section 4: Daily Trend Pulse ---
st.header(" Daily Trend Pulse")
col1, col2 = st.columns(2)

with col1:
    st.metric(" Rising", "#heatwave")
with col2:
    st.metric(" Fading", "#NoseContourChallenge")

st.markdown("---")
st.caption("Follow [@jane_emmanuel_](https://www.tiktok.com/@jane_emmanuel_) on TikTok for daily trend updates!")
