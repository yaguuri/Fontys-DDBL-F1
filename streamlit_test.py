import streamlit as st

#Initialize connection
conn = st.connection("mysql", type="sql")

#perform query
#ttl=600: to ensure the query result is cached for no longer than 10 minutes
player_df = conn.query("SELECT * FROM player;", ttl=600)

#choose one player
limit_idx = "9,1"  #just change this when you want other player
chosen_player = conn.query(f"SELECT CAST(sessionUID AS UNSIGNED INTEGER), firstName, lastName FROM player LIMIT {limit_idx};", ttl=600)

#print result
st.table(player_df)
st.table(chosen_player)

#load data as dataframe
lap_df = conn.query(f"SELECT * FROM lap WHERE lap.sessionUID = (SELECT sessionUID FROM player LIMIT {limit_idx});", ttl=600)
motion_df = conn.query(f"SELECT * FROM motion WHERE motion.sessionUID = (SELECT sessionUID FROM player LIMIT {limit_idx});", ttl=600)
session_df = conn.query(f"SELECT * FROM session WHERE session.sessionUID = (SELECT sessionUID FROM player LIMIT {limit_idx});", ttl=600)
telemetry_df = conn.query(f"SELECT * FROM telemetry WHERE telemetry.sessionUID = (SELECT sessionUID FROM player LIMIT {limit_idx});", ttl=600)

#save data as csv file
csv1 = lap_df.to_csv(index=False)
csv2 = motion_df.to_csv(index=False)
csv3 = session_df.to_csv(index=False)
csv4 = telemetry_df.to_csv(index=False)

#change the file_name before you execute!!!
st.download_button(
    label="Download data: lap",
    data=csv1,
    file_name="lap.csv",
    mime="text/csv"
)
st.download_button(
    label="Download data: motion",
    data=csv2,
    file_name="motion.csv",
    mime="text/csv"
)
st.download_button(
    label="Download data: session",
    data=csv3,
    file_name="session.csv",
    mime="text/csv"
)
st.download_button(
    label="Download data: telemetry",
    data=csv4,
    file_name="telemetry.csv",
    mime="text/csv"
)