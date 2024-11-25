import streamlit as st
import acbc
import pandas as pd
import plotly.express as px

def plot_line_chart(df, x_col, y_col, title="Line Chart"):
    # Create a line chart with Plotly Express
    fig = px.line(df, x=x_col, y=y_col, title=title)
    # Update layout for better visualization
    fig.update_layout(
        xaxis_title=x_col,
        xaxis=dict(autorange='reversed'),
        yaxis_title=y_col,
        template="plotly_white",
        title_x=0.5
    )
    return fig
def plot_bar_chart(df, x_col, y_col, title="Bar Chart"):
    # Create a bar chart with Plotly Express
    fig = px.bar(df, x=x_col, y=y_col, title=title)
    # Update layout for better visualization
    fig.update_layout(
    #     xaxis_title=x_col,
    #     yaxis_title=y_col,
    #     template="plotly_white",
        title_x=0.5
    )
    return fig

master_sheet = acbc.get_csv_file_as_dataframe("/master.csv")
master_sheet.set_index('No',inplace=True)

for i in master_sheet.columns:
    if 'Date'in i:
        master_sheet[i] = pd.to_datetime(master_sheet[i], format='%Y%m%d').dt.strftime('%Y-%m-%d')

ir = acbc.get_dpt_as_dataframe("/acbc1/20241119_BEA_P0.dpt")

col1 ,col2 = st.columns((1,1))
with col1:
    st.write('''
## **Sample acbc1 data card**
''')
    st.dataframe(master_sheet[['Date Produced','Residence Time(min)','T(C)','C','H','N','O','BET']].loc['acbc1'])

with col2:
    st.write('''## **A plot**''')
    elemental_df = master_sheet[['C','H','N','O']].T.reset_index()
    elemental_df.rename(columns={'index':'element'},inplace=True)
    # st.dataframe(elemental_df)
    st.plotly_chart(plot_bar_chart(elemental_df,elemental_df['element'],elemental_df['acbc1'],title='Elemental Comp.'))

col3 ,col4 = st.columns((1,1))
with col3:
    st.write('''## **Sample acbc1 IR**''')
    st.dataframe(ir, use_container_width=False)

with col4:
    st.write('''## **IR plot**''')
    st.plotly_chart(plot_line_chart(ir,'Wavenumber','Intensity','acbc1 IR'))