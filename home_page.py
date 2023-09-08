  # Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import os

LOGGER = get_logger(__name__)
main_directory = os.getcwd()
# target_directory = "archive"
# work_directory = os.path.join(main_directory, target_directory)

fin_data = os.path.join(main_directory, "fin_data_x.csv")
type_of_transactions = ['Select Transaction type','Payment', 'Cash-In', 'Cash-Out', 'Merchant']
customer_balance = 1000000

def run():
    st.set_page_config(
        page_title="SECURE SENSE HOME",
        page_icon="🔒",
    )

    # st.header("JETSTREAM KNOWLEDGE BASE")

    st.write("# Welcome to SecureSense! 🔒")

    st.session_state['customer_balance'] = 1000000

    setup_payment_portal()

    setup_data(fin_data)

    # st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        
        **👈 Select a page from the sidebar** to do something useful.
    """
    )

    st.markdown('**_SecureSense_**. ❤')

def setup_data(file_name: str):

    df = pd.read_csv(file_name)

    st.markdown("## SYNTHETIC DATA")
    # modify = st.checkbox("Add filters")

    st.data_editor(df, num_rows='dynamic')


    st.download_button(
        "Download current selection as .html",
        df.to_html().encode("utf-8"),
        "transactions.html",
        "text/html",
        key="download-html",
    )

    st.download_button(
        "Download current selection as .csv",
        df.to_csv().encode("utf-8"),
        "transactions.csv",
        "text/csv",
        key="download-csv",
    )

def setup_payment_portal():
    st.session_state.test_disabled = False 

    with st.sidebar:
        transaction_amount = st.number_input(label="Transaction amount", key='transaction_amount', min_value=0, max_value=1000, value=300, step=50, help="", disabled=st.session_state.test_disabled)
        transaction_rate = st.slider(label="rate", min_value=0.0, max_value=1.0, step=0.1, value=0.7, key='tranaction_rate', help="", disabled=st.session_state.test_disabled)
        transaction_type = st.selectbox(label='Type of Transaction', options=type_of_transactions)
        st.button(label="Make Transaction", on_click=handler_payment_process, disabled=st.session_state.test_disabled)      
    
def handler_payment_process():
    """Fetches model responses"""
    st.session_state.test_disabled = False 

    model_config_template = {
        'transaction_amount': st.session_state.transaction_amount,
        'transaction_rate': st.session_state.transaction_rate,
        'transaction_type': st.session_state.transaction_type,
    }

if __name__ == "__main__":
    run()