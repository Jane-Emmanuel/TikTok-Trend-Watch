import streamlit as st

st.set_page_config(page_title="TikTok Trend Watch", layout="centered")

st.title("🎵 TikTok Fun Fact + Trend Watch")
st.caption("Updated Weekly • Curated by Jane Emmanuel")

# --- Section 1: Fun Fact ---
st.header("✨ Fun Fact of the Week")
st.success("The TikTok sound **'If We Ever Broke Up' by Mae Stephens** has been used in over **3.4 million** videos globally as of this week!")

# --- Section 2: Top 5 TikTok Sounds ---
st.header("🔥 Top 5 TikTok Sounds Right Now")

top_sounds = [
    "Espresso - Sabrina Carpenter",
    "Not Like Us - Kendrick Lamar",
    "You Look Happier (sped up)",
    "Tshwala Bam (Remix) – Titom & Yuppe",
    "Staring at the Ceiling – Girl in Red"
]

# Initialize vote counts in session_state
if "votes" not in st.session_state:
    st.session_state.votes = {sound: 0 for sound in top_sounds}

selected_sound = st.radio("🎧 Vote for your favorite TikTok sound:", top_sounds)

if st.button("Vote"):
    st.session_state.votes[selected_sound] += 1
    st.success(f"✅ You voted for: {selected_sound}")

st.subheader("📊 Live Voting Results")
for sound, count in st.session_state.votes.items():
    st.write(f"{sound}: **{count}** votes")

# --- Section 3: Global TikTok Trends ---
st.header("🌍 Global Trends to Watch")
st.markdown("""
- **#OrangePeelMakeup** trend is going viral in beauty TikTok  
- Afro-dance trend using **Tshwala Bam** is trending worldwide  
- Skit trend: *“POV: You’re the friend with no AirDrop”*  
- Filter trend: *Neon outline art effect*  
""")

# --- Section 4: Weekly Trend Watch ---
st.header("📈 Weekly Trend Watch")
col1, col2 = st.columns(2)

with col1:
    st.metric("📈 Rising", "#WalmartHaul")
with col2:
    st.metric("📉 Fading", "#NoseContourChallenge")

st.markdown("---")
st.caption("Follow [@jane_emmanuel_](https://www.tiktok.com/) on TikTok for more updates!")
