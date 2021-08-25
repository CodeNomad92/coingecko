import streamlit as st
import pandas
from pandas import json_normalize
from pycoingecko import CoinGeckoAPI
from streamlit.proto.DataFrame_pb2 import Table
cg = CoinGeckoAPI()

st.title("This is crypto price app")
CHOICES = {'Bitcoin': "Bitcoin", 'Ethereum': "Ethereum", 'Litecoin': "Litecoin"}

st.sidebar.selectbox("select crypto",options=list(CHOICES.keys()))
d=cg.get_price(ids=['bitcoin'],vs_currencies ='INR',include_market_cap=True, include_24hr_vol=True, include_24hr_change=True, include_last_updated_at=True)
e=cg.get_price(ids=['litecoin'], vs_currencies='usd', include_market_cap=True, include_24hr_vol=True, include_24hr_change=True, include_last_updated_at=True)
f=cg.get_price(ids=['ethereum'], vs_currencies='usd', include_market_cap=True, include_24hr_vol=True, include_24hr_change=True, include_last_updated_at=True)

st.write("""
Bitcoin
""")
st.write(json_normalize(d))
st.write("""
Litecoin
""")
st.write(json_normalize(e))
st.write("""
Ethereum
""")
st.write(json_normalize(f))
