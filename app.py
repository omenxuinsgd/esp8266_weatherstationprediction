import streamlit as st
# import model_kel6 as md
from supabase import create_client
import plotly.express as px
import matplotlib.pyplot as plt
import os
import kel6_model as md

API_URL = 'https://yawjhokrhegewvzqzcdh.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inlhd2pob2tyaGVnZXd2enF6Y2RoIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY2ODk1MjA3MSwiZXhwIjoxOTg0NTI4MDcxfQ.o8-s-1FzfseqI6fGWUmULdWv6clZRJa8g3Y986nCyUY'

supabase = create_client(API_URL, API_KEY)

supabaseList = supabase.table('mlxkel6_uas').select('*').execute().data
supabaseList2 = supabase.table('mlxkel6_uas').select('*').limit(1).order('id', desc=True).execute().data

st.write("#### Peramalan Cuaca Berbasis NodeMCU ESP8266 Menggunakan Algoritma Gaussian Naive Bayes")
st.image("IMG_2110.jpg")

st.sidebar.write("### Peramalan Cuaca Berbasis NodeMCU ESP8266 Menggunakan Algoritma Gaussian Naive Bayes")

st.sidebar.write("#### Introduction")
check_box = st.sidebar.checkbox(label="Display Creators")

namakel = ["Nur Rokhman", "Eka Imamul Muhlisin", "Lilien Ramadhan", "Alif Hilmi", "Hilman Taufiq Akbar"]
if check_box:
    st.write("###### Created By: Nur Rokhman | Eka Imamul Muhlisin | Lilien Ramadhan | Alif Hilmi | Hilman Taufiq Akbar")
    st.sidebar.write(namakel)

st.write("#### Prediksi Cuaca: Stasiun Cuaca")
st.table(supabaseList2)

# Prediksi
import json
import numpy as np
cek = np.array(supabaseList2)
prediksi = md.model.predict([[cek[0]['prestipasi'], cek[0]['suhu'], cek[0]['kelembapan'], cek[0]['kecepatan_angin'], cek[0]['arah_angin']]])
if prediksi[-1] == 1:
  st.markdown("#### Prediksi Cuaca: " + md.weather_dict[prediksi[-1]])
elif prediksi[-1] == 2:
  st.markdown("#### Prediksi Cuaca: " + md.weather_dict[prediksi[-1]])
elif prediksi[-1] == 3:
  st.markdown("#### Prediksi Cuaca: " + md.weather_dict[prediksi[-1]])
elif prediksi[-1] == 4:
  st.markdown("#### Prediksi Cuaca: " + md.weather_dict[prediksi[-1]])
elif prediksi[-1] == 5:
  st.markdown("#### Prediksi Cuaca: " + md.weather_dict[prediksi[-1]])
elif prediksi[-1] == 6:
  st.markdown("#### Prediksi Cuaca: " + md.weather_dict[prediksi[-1]])
elif prediksi[-1] == 7:
  st.markdown("#### Prediksi Cuaca: " + md.weather_dict[prediksi[-1]])
elif prediksi[-1] == 8:
  st.markdown("#### Prediksi Cuaca: " + md.weather_dict[prediksi[-1]])
elif prediksi[-1] == 9:
  st.markdown("#### Prediksi Cuaca: " + md.weather_dict[prediksi[-1]])
elif prediksi[-1] == 10:
  st.markdown("#### Prediksi Cuaca: " + md.weather_dict[prediksi[-1]])
elif prediksi[-1] == 11:
  st.markdown("#### Prediksi Cuaca: " + md.weather_dict[prediksi[-1]])
elif prediksi[-1] == 12:
  st.markdown("#### Prediksi Cuaca: " + md.weather_dict[prediksi[-1]])
elif prediksi[-1] == 13:
  st.markdown("#### Prediksi Cuaca: " + md.weather_dict[prediksi[-1]])
elif prediksi[-1] == 14:
  st.markdown("#### Prediksi Cuaca: " + md.weather_dict[prediksi[-1]])
elif prediksi[-1] == 15:
  st.markdown("#### Prediksi Cuaca: " + md.weather_dict[prediksi[-1]])

import streamlit as st

import streamlit as st

def refresh():
    st.write("Halaman sekarang akan direfresh...")
    st.markdown("""
        <script>
            window.location.reload();
        </script>
    """, unsafe_allow_html=True)

btn = st.button("Refresh halaman")
if btn:
    refresh()
    


#st.write(supabaseList2)
#st.write(type(supabaseList2))
#import json
#import numpy as np
#cek = np.array(supabaseList2)
#st.write(cek)
#st.write(cek[0])
#list = list(cek[0].items())
#nparray = np.array(list)
#print(nparray)
#st.markdown(nparray)

check_box2 = st.sidebar.checkbox(label="Display Explaining Project")
if check_box2:
    st.write("##### Aplikasi Stasiun Cuaca")
    st.write("Aplikasi peramalan cuaca adalah aplikasi yang memberikan ramalan cuaca kepada penggunanya. Aplikasi ini menampilkan informasi tentang suhu, kelembaban, kecepatan angin, dan kondisi cuaca saat ini. Aplikasi peramalan cuaca bisa diakses melalui perangkat seluler atau komputer, dan mengambil data dari stasiun cuaca (ESP8266) untuk memperoleh informasi yang akurat tentang kondisi cuaca saat ini. Stasiun cuaca adalah suatu tempat yang terdapat peralatan yang digunakan untuk mengukur kondisi cuaca. Peralatan tersebut bisa berupa anemometer untuk mengukur kecepatan angin, DHT11 untuk mengukur kelembaban dan suhu udara, serta barometer untuk mengukur tekanan udara. Data yang dihasilkan oleh stasiun cuaca kemudian diolah dan dikirimkan kepada aplikasi peramalan cuaca untuk dipublikasikan ke masyarakat.")
    st.write('''
Gaussian Naive Bayes adalah salah satu jenis algoritma klasifikasi yang sering digunakan dalam machine learning. Algoritma ini mengasumsikan bahwa setiap fitur (atribut) dari data yang digunakan untuk melakukan klasifikasi adalah merupakan variabel Gaussian (atau Normal). Dengan kata lain, algoritma ini mengasumsikan bahwa distribusi dari setiap fitur adalah sebuah distribusi Normal.

Untuk memprediksi cuaca, algoritma Gaussian Naive Bayes dapat digunakan dengan mengumpulkan data cuaca seperti suhu, kelembaban, tekanan udara, dan sebagainya. Setiap fitur ini kemudian dianggap sebagai variabel Gaussian, dan algoritma akan mempelajari pola-pola yang terkait dengan kondisi cuaca yang berbeda.

Untuk melakukan klasifikasi, algoritma Gaussian Naive Bayes akan menggunakan rumus probabilitas yang menghitung kemungkinan suatu kondisi cuaca terjadi berdasarkan nilai-nilai fitur yang diberikan. Misalnya, jika nilai suhu tinggi dan kelembaban rendah, algoritma dapat memprediksi bahwa cuaca tersebut adalah cerah. Sebaliknya, jika nilai suhu rendah dan kelembaban tinggi, algoritma dapat memprediksi bahwa cuaca tersebut adalah hujan.

Sebagai tambahan, algoritma Gaussian Naive Bayes juga mengasumsikan bahwa semua fitur adalah independen satu sama lain. Ini berarti bahwa kemungkinan suatu kondisi cuaca terjadi tidak terpengaruh oleh nilai dari fitur lain.

Dalam kasus prediksi cuaca, asumsi independensi fitur ini mungkin tidak sepenuhnya benar, karena fitur-fitur seperti suhu dan kelembaban biasanya saling terkait. Namun, meskipun demikian, algoritma Gaussian Naive Bayes masih dapat memberikan hasil yang cukup akurat dalam memprediksi cuaca, terutama jika data yang digunakan cukup banyak dan representatif.
''')

st.sidebar.write("#### Visualization Data")
select = st.sidebar.selectbox("Visualizatiobn Type", ["Histogram", "Tabel"], key='1')
if not st.sidebar.checkbox("Hide", True, key='l'):
    st.markdown("### Sensor Data")
    if(select == "Histogram"):
        fig = px.histogram(supabaseList, x="created_at", y="suhu",
                           color='suhu', height=300, width=700)
        st.plotly_chart(fig)
        fig2 = px.histogram(supabaseList, x="created_at", y="kelembapan",
                           color='kelembapan', height=300, width=700)
        st.plotly_chart(fig2)
    else:
        st.table(supabaseList)

    st.markdown("x--------------------------------------------------------------------------------------------------------------------------------------------")
