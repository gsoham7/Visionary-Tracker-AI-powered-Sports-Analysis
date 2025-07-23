import streamlit as st
import base64

# Function to add a video
def add_video(video_file):
    with open(video_file, "rb") as video_file:
        encoded_video = base64.b64encode(video_file.read()).decode()
    return f"""
    <div style="display: flex; justify-content: center;">
        <video autoplay muted loop width="600" style="border-radius: 10px;">
            <source src="data:video/mp4;base64,{encoded_video}" type="video/mp4">
        </video>
    </div>
    """

# Function to add a Google Drive button
def add_drive_button(link, text):
    st.markdown(

        f"""
        <div style="display: flex; justify-content: center; margin-top: 10px;">
            <a href="{link}" target="_blank" style="text-decoration: none;">
                <button style="padding: 10px 20px; font-size: 16px; border: none; border-radius: 5px; background-color: #007BFF; color: white; cursor: pointer;">{text}</button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# Main function to run the Streamlit app
def main():
    # Set page title and icon
    st.set_page_config(page_title="Visionary Tracker", page_icon="🏆", layout="wide")

    # Styling for the whole app
    st.markdown("""
        <style>
            body {
                font-family: sans-serif; /* Modern font */
            }
            h1 {
                color: #333; /* Darker title */
                text-align: center;
            }
            h3 {
                color: #666; /* Slightly lighter subtitle */
                text-align: center;
            }
            .sidebar .sidebar-content {
                background-color: #f0f0f0; /* Light gray sidebar */
                padding: 20px; /* Add some padding */
                border-radius: 10px; /* Rounded corners for sidebar */
            }
            .sidebar-title {
                font-size: 1.2em;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .stRadio { /* Style radio buttons */
                margin-bottom: 10px;
            }
            .stButton { /* Style buttons */
                margin-top: 10px;
            }

        </style>
    """, unsafe_allow_html=True)



    # Add title and subtitle at the top of the page
    st.markdown("""
        <h1>Visionary Tracker</h1>
        <h3>Track Your Favorite Sports</h3>
    """, unsafe_allow_html=True)

    # Sidebar with categories (Styling applied above)
    st.sidebar.markdown("<div class='sidebar-title'>Categories</div>", unsafe_allow_html=True) #Styled title
    category = st.sidebar.radio("Choose a category:", ("Indoor Sports", "Outdoor Sports"))

    # Define video and link mappings for each sport
    sport_video_links = {
        "Pool Table": ("pool_table.mp4", "https://drive.google.com/drive/folders/1Y6YVLUz-4ZWctQsnW2h2YZnq6NMCcDIs?usp=sharing"),
        "Badminton": ("badminton.mp4", "https://drive.google.com/drive/folders/1FBjyIxGp-u5iod5GcauOuwddPZyrNSxN?usp=sharing"),
        "Football": ("football.mp4", "https://drive.google.com/drive/folders/1k1a8nPy_hSZCHiowUOgXMWd42OPbzKzs"),
        "Tennis": ("tennis.mp4", "https://drive.google.com/drive/folders/1E4V3YmmdCTbWA-JroIHy9VrMxXCDxBeF?usp=sharing"),
        "Basketball": ("basketball.mp4", "https://drive.google.com/drive/folders/1xayiJ93rpVl6p5xGjEmVFpDFjNTqTbR5?usp=sharing"),
    }

    # Display sports based on the selected category
    if category == "Indoor Sports":
        sport = st.sidebar.radio("Choose a sport:", ("Pool Table", "Badminton"))
    else:
        sport = st.sidebar.radio("Choose a sport:", ("Football", "Tennis", "Basketball"))

    # Get the video file and drive link for the selected sport
    video_file, drive_link = sport_video_links[sport]

    # Key Change: Use st.empty() to create a placeholder
    video_placeholder = st.empty()

    # Display the video and button using the placeholder
    video_html = add_video(video_file)
    video_placeholder.markdown(video_html, unsafe_allow_html=True)

    add_drive_button(drive_link, f"{sport} Resources")

# Run the app
if __name__ == "__main__":
    main()