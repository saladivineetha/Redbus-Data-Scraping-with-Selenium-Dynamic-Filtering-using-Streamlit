import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import pymysql
import time

lists_Andhra=[]
df_AP_bus=pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\redbus.project\df_AP_bus.csv")
for i,r in df_AP_bus.iterrows():
    lists_Andhra.append(r["Route_name"])


lists_Kerala=[]
df_Kerala_bus=pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\redbus.project\df_Kerala_bus.csv")
for i,r in df_Kerala_bus.iterrows():
    lists_Kerala.append(r["Route_name"])


lists_Telangana=[]
df_Telangana_bus=pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\redbus.project\df_Telangana_bus.csv")
for i,r in df_Telangana_bus.iterrows():
    lists_Telangana.append(r["Route_name"])

lists_Rajasthan=[]
df_Rajasthan_bus=pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\redbus.project\df_Rajasthan_bus.csv")
for i,r in df_Rajasthan_bus.iterrows():
    lists_Rajasthan.append(r["Route_name"])


lists_Himachal=[]
df_HP_bus=pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\redbus.project\df_HP_bus.csv")
for i,r in df_HP_bus.iterrows():
    lists_Himachal.append(r["Route_name"])



lists_UP=[]
df_UP_bus=pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\redbus.project\df_UP_bus.csv")
for i,r in df_UP_bus.iterrows():
    lists_UP.append(r["Route_name"])

lists_Assam=[]
df_Assam_bus=pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\redbus.project\df_Assam_bus.csv")
for i,r in df_Assam_bus.iterrows():
    lists_Assam.append(r["Route_name"])


lists_Punjab=[]
df_Punjab_bus=pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\redbus.project\df_Punjab_bus.csv")
for i,r in df_Punjab_bus.iterrows():
    lists_Punjab.append(r["Route_name"])

lists_Kadamba=[]
df_buses_Kadamba=pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\redbus.project\df_buses_Kadamba.csv")
for i,r in df_buses_Kadamba.iterrows():
    lists_Kadamba.append(r["Route_name"])

lists_SB=[]
df_buses_SB=pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\redbus.project\df_buses_SB.csv")
for i,r in df_buses_SB.iterrows():
    lists_SB.append(r["Route_name"])


st.set_page_config(page_title="Redbus",page_icon="",layout="wide")

st.title(":red[RedBus: Apno ko, sapno ko kareeb laye] :bus:")

df=pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\redbus.project\FinalRedBus_df.csv")
st.subheader("Redbus final data")
st.write(df)

selected=option_menu(menu_title="RedBus details🚌 ",
                        options=["Home","States and Routes"],
                        icons=["house","info"],default_index=0)
if selected=="Home":
    st.title(":blue[Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit]")
    st.subheader('''Skills that are used to complete the project:
                        Selenium for web scraping,
                        python
                        SQL
                        Streamlit for dynamic filtering''')
    st.subheader(":blue[Problem Statement:]")
    st.write('''The Redbus Data Scraping and Filtering with Streamlit Application
             aims to revolutionize the transportation industry by providing 
             a comprehensive solution for collecting, analyzing, and visualizing bus travel data. 
             By utilizing Selenium for web scraping, this project automates the extraction of detailed 
             information from Redbus, including bus routes, schedules, prices, and seat availability.
             By streamlining data collection and providing powerful tools for data-driven decision-making,
             this project can significantly improve operational efficiency and strategic planning in the transportation industry''')


if selected=="States and Routes":
    state= st.selectbox("Lists of States", ["AndhraPradesh", "Kerala", "Telangana", "Rajasthan", 
                                          "Himachal", "UttarPradesh", "Assam", "Punjab","Kadamba", "SouthBengal"])
    
    col1,col2=st.columns(2)
    with col1:
        select_type = st.radio("Choose bus type", ("sleeper", "semi-sleeper", "others"))
    with col2:
        select_fare = st.radio("Choose bus fare range", ("50-500", "500-2500", "2500 and above"))

    Time=st.time_input("select the time")

    if state=="AndhraPradesh":
        AP=st.selectbox("List of routes",lists_Andhra)
        def type_and_fare_AP(bus_type, fare_range):
            connection = pymysql.connect(host="localhost", user="root", password="root", database="REDBUS_DETAILS")
            my_cursor = connection.cursor()

             # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-2500":
                fare_min, fare_max = 500, 2500
            else:
                fare_min, fare_max = 2500, 100000  # assuming a high max value for "2500 and above"

             # Define bus type condition
            if bus_type == "sleeper":
                bus_type= "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type= "Bus_type LIKE '%Semi Sleeper%'"
            else:
                bus_type = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi Sleeper%'"

            
            

    # Formulate the query
            query = f"""
                    SELECT * FROM redbus_complete_details
                    WHERE Price BETWEEN {fare_min} AND {fare_max}
                    AND {bus_type} AND Start_time>='{Time}'
                    AND Route_name="{AP}"
            
                    ORDER BY Price, Start_time DESC
                    """

    # Execute the query
            my_cursor.execute(query)
            data= my_cursor.fetchall()
            connection.close()
        
            df = pd.DataFrame(data, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df
             
        df_result = type_and_fare_AP(select_type, select_fare)
        st.dataframe(df_result)

     
    if state=="Kerala":
        Kerala=st.selectbox("List of routes",lists_Kerala)
        def type_and_fare_Kerala(bus_type, fare_range):
            connection = pymysql.connect(host="localhost", user="root", password="root", database="REDBUS_DETAILS")
            my_cursor = connection.cursor()

             # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-2500":
                fare_min, fare_max = 500, 2500
            else:
                fare_min, fare_max = 2500, 100000  # assuming a high max value for "2500 and above"

             # Define bus type condition
            if bus_type == "sleeper":
                 bus_type= "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                 bus_type= "Bus_type LIKE '%Semi Sleeper%'"
            else:
                 bus_type = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi Sleeper%'"
            
            
           

    # Formulate the query
            query = f"""
                    SELECT * FROM redbus_complete_details
                    WHERE Price BETWEEN {fare_min} AND {fare_max}
                    AND {bus_type} AND Start_time>='{Time}'
                    AND Route_name="{Kerala}" 
                   
                    ORDER BY Price, Start_time DESC
                    """

    # Execute the query
            my_cursor.execute(query)
            data= my_cursor.fetchall()
            connection.close()
        
            df = pd.DataFrame(data, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"])
            return df
        
        df_result = type_and_fare_Kerala(select_type, select_fare)
        st.dataframe(df_result)

    if state=="Telangana":
        Telangana=st.selectbox("List of routes",lists_Telangana)
        def type_and_fare_Telangana(state, bus_type, fare_range):
            connection = pymysql.connect(host="localhost", user="root", password="root", database="REDBUS_DETAILS")
            my_cursor = connection.cursor()

             # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-2500":
                fare_min, fare_max = 500, 2500
            else:
                fare_min, fare_max = 2500, 100000  # assuming a high max value for "2500 and above"

             # Define bus type condition
            if bus_type == "sleeper":
                 bus_type= "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                 bus_type= "Bus_type LIKE '%Semi Sleeper%'"
            else:
                 bus_type = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi Sleeper%'"
                
           

    # Formulate the query
            query = f"""
                    SELECT * FROM redbus_complete_details
                    WHERE Price BETWEEN {fare_min} AND {fare_max}
                    AND {bus_type} AND Start_time>='{Time}'
                    AND Route_name="{Telangana}"
                    
                    ORDER BY Price, Start_time DESC
                    """

    # Execute the query
            my_cursor.execute(query)
            data = my_cursor.fetchall()
            connection.close()
        
            df = pd.DataFrame(data, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"])
            return df
        
        df_result = type_and_fare_Telangana(select_type, select_fare)
        st.dataframe(df_result)

    if state=="Rajasthan":
        Rajasthan=st.selectbox("List of routes",lists_Rajasthan)
        def type_and_fare_Rajasthan( bus_type, fare_range):
            connection = pymysql.connect(host="localhost", user="root", password="root", database="REDBUS_DETAILS")
            my_cursor = connection.cursor()

             # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-2500":
                fare_min, fare_max = 500, 2500
            else:
                fare_min, fare_max = 2500, 100000  # assuming a high max value for "2000 and above"

             # Define bus type condition
            if bus_type == "sleeper":
                 bus_type= "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                 bus_type= "Bus_type LIKE '%Semi Sleeper%'"
            else:
                 bus_type = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi Sleeper%'"

            
            

    # Formulate the query
            query = f"""
                    SELECT * FROM redbus_complete_details
                    WHERE Price BETWEEN {fare_min} AND {fare_max}
                    AND {bus_type} AND Start_time>='{Time}'
                    AND Route_name="{Rajasthan}"
                  
                    ORDER BY Price, Start_time DESC
                    """

    # Execute the query
            my_cursor.execute(query)
            data= my_cursor.fetchall()
            connection.close()
        
            df = pd.DataFrame(data, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"])
            return df
    
        df_result = type_and_fare_Rajasthan(select_type, select_fare)
        st.dataframe(df_result)

    if state=="Himachal":
        Himachal=st.selectbox("List of routes",lists_Himachal)
        def type_and_fare_Himachal(bus_type, fare_range):
            connection = pymysql.connect(host="localhost", user="root", password="root", database="REDBUS_DETAILS")
            my_cursor = connection.cursor()

             # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-2500":
                fare_min, fare_max = 500, 2500
            else:
                fare_min, fare_max = 2500, 100000  # assuming a high max value for "2000 and above"

             # Define bus type condition
            if bus_type == "sleeper":
                 bus_type= "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                 bus_type= "Bus_type LIKE '%Semi Sleeper%'"
            else:
                 bus_type = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi Sleeper%'"

            
            
        

    # Formulate the query
            query = f"""
                SELECT * FROM redbus_complete_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND {bus_type} AND Start_time>='{Time}'
                AND Route_name="{Himachal}"
                
                ORDER BY Price, Start_time DESC
                """


    # Execute the query
            my_cursor.execute(query)
            data= my_cursor.fetchall()
            connection.close()
        
            df = pd.DataFrame(data, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"])
            return df
        
        df_result = type_and_fare_Himachal(select_type, select_fare)
        st.dataframe(df_result)
    
    if state=="UttarPradesh":
        UP=st.selectbox("List of routes",lists_UP)
        def type_and_fare_UP( bus_type, fare_range):
            connection = pymysql.connect(host="localhost", user="root", password="root", database="REDBUS_DETAILS")
            my_cursor = connection.cursor()

             # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-2500":
                fare_min, fare_max = 500, 2500
            else:
                fare_min, fare_max = 2500, 100000  # assuming a high max value for "2000 and above"

             # Define bus type condition
            if bus_type == "sleeper":
                 bus_type= "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                 bus_type= "Bus_type LIKE '%Semi Sleeper%'"
            else:
                 bus_type = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi Sleeper%'"
                
            
            

    # Formulate the query
            query = f"""
                    SELECT * FROM redbus_complete_details
                    WHERE Price BETWEEN {fare_min} AND {fare_max}
                    AND {bus_type} AND Start_time>='{Time}'
                    AND Route_name="{UP}"
                   
                    ORDER BY Price, Start_time DESC
                    """

    # Execute the query
            my_cursor.execute(query)
            data= my_cursor.fetchall()
            connection.close()
        
            df = pd.DataFrame(data, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"])
            return df
       
        df_result = type_and_fare_UP(select_type, select_fare)
        st.dataframe(df_result)

    
    if state=="Assam":
        Assam=st.selectbox("List of routes",lists_Assam)
        def type_and_fare_Assam(bus_type, fare_range):
            connection = pymysql.connect(host="localhost", user="root", password="root", database="REDBUS_DETAILS")
            my_cursor = connection.cursor()

             # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-2500":
                fare_min, fare_max = 500, 2500
            else:
                fare_min, fare_max = 2500, 100000  # assuming a high max value for "2000 and above"

             # Define bus type condition
            if bus_type == "sleeper":
                 bus_type= "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                 bus_type= "Bus_type LIKE '%Semi Sleeper%'"
            else:
                 bus_type = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi Sleeper%'"


    # Formulate the query
            query = f"""
                 SELECT * FROM redbus_complete_details
                 WHERE Price BETWEEN {fare_min} AND {fare_max}
                 AND {bus_type} AND Start_time>='{Time}'
                 AND Route_name="{Assam}"
                 
                 ORDER BY Price, Start_time DESC
                 """

    # Execute the query
            my_cursor.execute(query)
            data= my_cursor.fetchall()
            connection.close()
    
            df = pd.DataFrame(data, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"])
            return df
        
        df_result = type_and_fare_Assam(select_type, select_fare)
        st.dataframe(df_result)

    
    if state=="Punjab":
        Punjab=st.selectbox("List of routes",lists_Punjab)
        def type_and_fare_Punjab( bus_type, fare_range):
            connection = pymysql.connect(host="localhost", user="root", password="root", database="REDBUS_DETAILS")
            my_cursor = connection.cursor()

             # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-2500":
                fare_min, fare_max = 500, 2500
            else:
                fare_min, fare_max = 2500, 100000  # assuming a high max value for "2000 and above"

             # Define bus type condition
            if bus_type == "sleeper":
                 bus_type= "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                 bus_type= "Bus_type LIKE '%Semi Sleeper%'"
            else:
                 bus_type = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi Sleeper%'"

            

    # Formulate the query
            query = f"""
                     SELECT * FROM redbus_complete_details
                     WHERE Price BETWEEN {fare_min} AND {fare_max}
                     AND {bus_type} AND Start_time>='{Time}'
                     AND Route_name="{Punjab}"
                    
                     ORDER BY Price, Start_time DESC
                    """

    # Execute the query
            my_cursor.execute(query)
            data = my_cursor.fetchall()
            connection.close()
        
            df = pd.DataFrame(data, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"])
            return df
        
        df_result = type_and_fare_Punjab(select_type, select_fare)
        st.dataframe(df_result)

    
    if state=="Kadamba":
        Kadamba=st.selectbox("List of routes",lists_Kadamba)
        def type_and_fare_Kadamba( bus_type, fare_range):
            connection = pymysql.connect(host="localhost", user="root", password="root", database="REDBUS_DETAILS")
            my_cursor = connection.cursor()

             # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-2500":
                fare_min, fare_max = 500, 2500
            else:
                fare_min, fare_max = 2500, 100000  # assuming a high max value for "2000 and above"

             # Define bus type condition
            if bus_type == "sleeper":
                 bus_type= "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                 bus_type= "Bus_type LIKE '%Semi Sleeper%'"
            else:
                 bus_type = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi Sleeper%'"
            
            
        

    # Formulate the query
            query = f"""
                    SELECT * FROM redbus_complete_details
                    WHERE Price BETWEEN {fare_min} AND {fare_max}
                    AND {bus_type} AND Start_time>='{Time}'
                    AND Route_name="{Kadamba}"
                    
                    ORDER BY Price, Start_time DESC
                    """
            # Execute the query
            my_cursor.execute(query)
            data= my_cursor.fetchall()
            connection.close()
        
            df = pd.DataFrame(data, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"])
            return df
        
        
        df_result = type_and_fare_Kadamba(select_type, select_fare)
        st.dataframe(df_result)
    
    if state=="SouthBengal":
        SB=st.selectbox("List of routes",lists_SB)
        def type_and_fare_SB( bus_type, fare_range):
            connection = pymysql.connect(host="localhost", user="root", password="root", database="REDBUS_DETAILS")
            my_cursor = connection.cursor()

             # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-2500":
                fare_min, fare_max = 500, 2500
            else:
                fare_min, fare_max = 2500, 100000  # assuming a high max value for "2000 and above"

             # Define bus type condition
            if bus_type == "sleeper":
                 bus_type= "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                 bus_type= "Bus_type LIKE '%Semi Sleeper%'"
            else:
                 bus_type = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi Sleeper%'"

        

    # Formulate the query
            query = f"""
                    SELECT * FROM redbus_complete_details
                    WHERE Price BETWEEN {fare_min} AND {fare_max}
                    AND {bus_type} AND Start_time>='{Time}'
                    AND Route_name="{SB}"
                   
                    ORDER BY Price, Start_time DESC
                    """

    # Execute the query
            my_cursor.execute(query)
            data= my_cursor.fetchall()
            connection.close()

            df = pd.DataFrame(data, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"])
            return df
        
        df_result = type_and_fare_SB(select_type, select_fare)
        st.dataframe(df_result)



    
    
   


        
    
        



    

             
  















