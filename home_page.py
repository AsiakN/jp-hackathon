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
import secrets
import string
from llm import OpenAIFraudDetection

llm = OpenAIFraudDetection()

LOGGER = get_logger(__name__)
main_directory = os.getcwd()


fin_data = os.path.join(main_directory, "fin_data_x.csv")
df = pd.read_csv(fin_data)

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

    setup_data()

    # st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        
        **👈 Select a page from the sidebar** to do something useful.
    """
    )

    st.markdown('**_SecureSense_**. ❤')

def setup_data():
    if 'data' not in st.session_state:
        st.session_state['data'] = df

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
        if transaction_type and transaction_amount and transaction_rate:
            model_config_template = {
        'transaction_amount': transaction_amount,
        'rate':   transaction_rate,
        'transaction_type':  str.upper(transaction_type),
        'customer_code' :   gen_unique('C'), 
        'recipient': gen_unique('C')
        }
        st.button(label="Make Transaction", on_click=handler_payment_process, disabled=st.session_state.test_disabled, args=[model_config_template])      
    
def handler_payment_process(transaction_details:dict):
    """Fetches model responses"""
    st.session_state.test_disabled = False 
    print(transaction_details)

    new_df = pd.DataFrame.from_dict({
        'step': [1],
        'type': [transaction_details['transaction_type']],
        'amount': [transaction_details['transaction_amount']],
        'nameOrig': [transaction_details['customer_code']],
        'oldBalanceOrig': [customer_balance] ,
        'newBalanceOrig': [584743.8585],
        'oldBalanceDest': [574833],
        'newBalanceDest': [57493743],
        'nameDest': [transaction_details['recipient']],
        'isFraud': [0],
        'isFlaggedFraud': [0]
    }) 

    llm.make_api_call(transaction_details=transaction_details)
    

    # combined_df = pd.concat([new_df, df], ignore_index=True)
    # new_combined_df = combined_df.style.apply(highlight_new_row, axis=1)

    # st.data_editor(combined_df)

    # Make api prediction

def highlight_new_row(row):
    if row.name == 0:
        return ['background-color: yellow'] * len(row)
    return [''] 

def gen_unique(prefix: str, length: int = 5) -> str:
    """
    Generate some cool unique identifiers
    @param length: length for three parts of string, the longer the better
    @param prefix: A text to prefix recommended to make things highly unique
    @return: str
    """
    # get a good charset
    chars = string.digits + string.ascii_uppercase + string.octdigits

    word = prefix
    word += '-' + ''.join([secrets.choice(chars) for _ in range(length - 1)])  # first secure random in charset
    word += ''.join([secrets.choice(chars) for _ in range(length - 1)])  # second secure random in charset
    word += ''.join([secrets.choice(chars) for _ in range(length - 1)])  # third secure random in charset
    return word

if __name__ == "__main__":
    run()