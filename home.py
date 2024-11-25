import streamlit as st
import acbc
import pandas as pd

master_sheet = acbc.get_csv_file_as_dataframe("/master.csv")
for i in master_sheet.columns:
    if 'Date'in i:
        master_sheet[i] = pd.to_datetime(master_sheet[i], format='%Y%m%d').dt.strftime('%Y-%m-%d')

# Here the page begins
st.title("AC/BC 🦦")
st.header("Atlantic Canada Biochar Project")
st.write('''### Transformative Climate Action''')
st.write("Made by Brian Espinosa Acosta")

st.markdown('''## **Master Key of Samples**''')
st.dataframe(master_sheet.iloc[:,:4], use_container_width=True)

st.header("Data Management Tips",divider = "green")
st.markdown('''
### Data file naming:  
ProjectName_instrument_date(yyyymmdd)_ResearcherSampleCode_test#/letter.format  
E.g. BP_IR_20240906_BEA001_1.dpt  
:red[**Note**]: BP= Biochar Project, IR=infrared, BEA = Brian Espinosa Acosta  

### Instrument data structure:  
- IR: 2-columns, wavenumber(cm-1) | absorption intensity (a.u)  
- PXRD: 2-columns, 2theta degree | Peak Intensity  
- CHNO: 4-columns, C% | H% | N% | O%  
- ICP-OES: 6-columns, element | ppm | 1sd | wt% | RSD (%) | cor.-coeff  
- EDS: 2-columns, Energy (keV) | Intensity (a.u)  
- PA: ?  
- TGA-MS:  
1. TGA: 2-columns, Temperature (oC) | Mass Loss (mg)  
2. MS: 2-columns, mass-to-charge (m/z) | Relative Abundance (%)  
- pH: single digit"
            ''')