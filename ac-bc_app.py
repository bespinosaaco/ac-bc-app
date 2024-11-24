import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET
import pandas as pd
import io
import streamlit as st

# Configuration
NEXTCLOUD_URL = "https://nextcloud.computecanada.ca/remote.php/dav/files/be4/ac-bc"
USERNAME = "be4"
PASSWORD = ""

# Function to list files in the specific folder
def list_nextcloud_folder_files():
    url = f"{NEXTCLOUD_URL}/"
    response = requests.request("PROPFIND", url, auth=HTTPBasicAuth(USERNAME, PASSWORD))

    if response.status_code == 207:
        # Parse XML response to get file and folder names
        root = ET.fromstring(response.text)
        namespace = {'d': 'DAV:'}

        print("Files and folders in the specific folder:")
        for response in root.findall("d:response", namespace):
            href = response.find("d:href", namespace).text
            if href.endswith('/'):
                folder_name = href.split('/')[-2]
                if folder_name != "specific-folder":
                    print(f"[Folder] {folder_name}")
            else:
                file_name = href.split('/')[-1]
                print(f"[File] {file_name}")
    else:
        print(f"Failed to list files. Status code: {response.status_code}")

# Function to download and return CSV as pandas DataFrame
def get_csv_file_as_dataframe(file_path):
    url = f"{NEXTCLOUD_URL}{file_path}"
    response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD))

    if response.status_code == 200:
        csv_content = response.content.decode('utf-8')
        df = pd.read_csv(io.StringIO(csv_content))
        return df
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        return None

# # Main script
# if __name__ == "__main__":
#     list_nextcloud_folder_files()
#
#     file_path = "/master.csv"
#     if file_path.endswith(".csv"):
#         df = get_csv_file_as_dataframe(file_path)
#         if df is not None:
#             print("\nDataFrame successfully retrieved:\n")
#             print(df)
#     else:
#         print("The specified file is not a CSV file.")

if __name__ == "__main__":
    file_path = "/master.csv"
    master_sheet = get_csv_file_as_dataframe(file_path)
    # Title and header
    st.title("AC/BC 🦦")
    st.header("Atlantic Canada Biochar Project")
    st.write("Made by Brian Espinosa Acosta")
    st.dataframe(master_sheet, use_container_width=True)

