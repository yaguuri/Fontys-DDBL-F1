### SETTING UP ###
import streamlit as st


### LOAD DATA ###

#Initialize connection
conn = st.connection("mysql", type="sql")

#perform query
#ttl=600: to ensure the query result is cached for no longer than 10 minutes
player_df = conn.query("SELECT * FROM player;", ttl=600)

#print result
st.table(player_df)

#load data as dataframe
#lap_df = conn.query(f"SELECT * FROM lap WHERE lap.sessionUID = (SELECT sessionUID FROM player LIMIT {limit_idx});", ttl=600)
#motion_df = conn.query(f"SELECT * FROM motion WHERE motion.sessionUID = (SELECT sessionUID FROM player LIMIT {limit_idx});", ttl=600)
#session_df = conn.query(f"SELECT * FROM session WHERE session.sessionUID = (SELECT sessionUID FROM player LIMIT {limit_idx});", ttl=600)
#telemetry_df = conn.query(f"SELECT * FROM telemetry WHERE telemetry.sessionUID = (SELECT sessionUID FROM player LIMIT {limit_idx});", ttl=600)
