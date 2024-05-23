import random
import time
import streamlit as st

# List of players and their possible positions
players = {
    "Chris": ["GK", "RCM", "LCM", "CAM", "RW", "LW", "ST", "WISSEL1", "WISSEL2", "WISSEL3"],
    "Tim": ["GK", "RB", "RCB", "LCB", "LB", "RCM", "LCM", "CAM", "WISSEL1", "WISSEL2", "WISSEL3"],
    "Luuk": ["GK", "RB", "RCB", "LCB", "LB", "ST", "WISSEL1", "WISSEL2", "WISSEL3"],
    "Terp": ["GK", "RB", "RCB", "LCB", "LB", "RW", "LW", "WISSEL1", "WISSEL2", "WISSEL3"],
    "Walter": ["GK", "RCM", "LCM", "CAM", "RW", "LW", "ST", "WISSEL1", "WISSEL2", "WISSEL3"],
    "JP": ["GK", "RB", "RCB", "LCB", "LB", "RCM", "LCM", "CAM", "WISSEL1", "WISSEL2", "WISSEL3"],
    "Pieter": ["GK", "CAM", "RW", "LW", "ST", "WISSEL1", "WISSEL2", "WISSEL3"],
    "Reinout": ["GK", "RCM", "LCM", "CAM", "RW", "LW", "ST", "WISSEL1", "WISSEL2", "WISSEL3"],
    "Maxime": ["GK", "RCM", "LCM", "CAM", "RW", "LW", "ST", "WISSEL1", "WISSEL2", "WISSEL3"],
    "Luitjes": ["GK", "RCM", "LCM", "CAM", "RW", "LW", "ST", "WISSEL1", "WISSEL2", "WISSEL3"],
    "Ids": ["GK", "RB", "RCB", "LCB", "LB", "RW", "LW", "ST", "WISSEL1", "WISSEL2", "WISSEL3"],
    "Sander": ["GK", "RB", "RCB", "LCB", "LB", "RCM", "LCM", "CAM", "WISSEL1", "WISSEL2", "WISSEL3"],
    "Job": ["GK", "RB", "RCB", "LCB", "LB", "WISSEL1", "WISSEL2", "WISSEL3"],
    "Mark": ["GK", "RB", "RCB", "LCB", "LB", "WISSEL1", "WISSEL2", "WISSEL3"]
}

# List of positions in order
positions = ["RB", "RCB", "LCB", "LB", "RCM", "LCM", "CAM", "RW", "LW", "ST", "GK", "WISSEL1", "WISSEL2", "WISSEL3"]

# Keep track of assigned players
assigned_players = {}

def display_assignment(placeholder, position, player, final=0):
    border_color = 'green' if final == 1 else 'black'
    border_thickness = '10px' if final == 1 else '2px'
    
    placeholder.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
        <div style="border: {border_thickness} solid {border_color}; padding: 20px; width: 200px; height: 200px; display: flex; justify-content: center; align-items: center;">
            <div style="text-align: center; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;">
                <div>
                    <h1 style="font-size: 24px;">{position}</h1>
                    <p style="font-size: 24px;">{player}</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Function to assign players to positions
def assign_players():
    placeholder = st.empty()  # Create a placeholder
    for position in positions:   
        possible_players = [player for player, pos in players.items() if position in pos and player not in assigned_players]
        possible_players2 = [player for player in players if player not in assigned_players]
        if possible_players:
            selected_player = random.choice(possible_players)
            assigned_players[selected_player] = position
            players[selected_player] = []
            
            if "WISSEL" not in position: 
                display_assignment(placeholder, position, selected_player, 1)
                for i in range(120):
                    random_player = random.choice(possible_players2)
                    display_assignment(placeholder, position, random_player, 0)
                    time.sleep(0.0001*(0.5*i)**2)
                display_assignment(placeholder, position, selected_player, 1)
                time.sleep(3)
            display_assignment(placeholder, position, selected_player, 1)
            time.sleep(0.5)
    
    # Once all assignments are done, display the final lineup on the football field
    display_final_lineup(placeholder)

def display_final_lineup(placeholder):
    # Map positions to coordinates on the football field
    position_coordinates = {
        "GK": (90, 50),
        "RB": (70, 80),
        "RCB": (70, 60),
        "LCB": (70, 40),
        "LB": (70, 20),
        "RCM": (50, 70),
        "LCM": (50, 30),
        "CAM": (40, 50),
        "RW": (30, 80),
        "ST": (20, 50),
        "LW": (30, 20),
        "WISSEL1": (110, 5),
        "WISSEL2": (110, 20),
        "WISSEL3": (110, 35)
    }

    # Final lineup assignment
    final_output = """
    <div style="position: relative; width: 100%; height: 500px; background-color: green; border: 2px solid white;">
    """

    box_width = "100px"
    box_height = "40px"

    for player, position in assigned_players.items():
        top, left = position_coordinates[position]
        final_output += f"""
        <div style='position: absolute; top: {top}%; left: {left}%; transform: translate(-50%, -50%); color: white; text-align: center;'>
            <div style='border: 2px solid white; padding: 5px; width: {box_width}; height: {box_height}; background-color: rgba(0, 0, 0, 0.7); display: flex; align-items: center; justify-content: center;'>
                <div>
                    <p style='margin: 0; font-size: 14px;'>{position}</p>
                    <p style='margin: 0; font-size: 14px;'>{player}</p>
                </div>
            </div>
        </div>
        """

    final_output += "</div>"

    # Display the football field with the final lineup
    placeholder.markdown(
        f"""
        <div style="position: relative; width: 100%; height: 600px; background-color: green; border: 2px solid white;">
            {final_output}
        </div>
        """, unsafe_allow_html=True)

# Run the assignment
assign_players()
