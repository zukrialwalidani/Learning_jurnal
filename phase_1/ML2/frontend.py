from numpy import size
import streamlit as st
import pickle
with open("pipeline.pkl", "rb") as pipe:
    pipeline = pickle.load(pipe)

st.title("Aplikasi Pendeteksi Resign Karyawan")
Education = st.number_input('Pendidikan')
st.write('Pendidikan Bachelors(0), Masters(1), PhD(2)')
JoiningYear = st.number_input('Tahun Bergabung')
st.write('2012(0), 2013(1), 2014(2), 2015(3), 2016(4), 2017(5), 2018(6)')
City = st.number_input('Asal Kota')
st.write('Bangalore(0), Pune(1), New Delhi(2)')
PaymentTier = st.number_input('Tingkat Upah')
st.write('Tingkat 1(0), Tingkat 2(1), Tingkat(3)')
Age = st.number_input('Umur')
st.write('Umur dimulai dari 24 tahun(0) hingga 41(19)')
Gender= st.number_input('Jenis Kelamin')
st.write('Wanita(0), Pria(1)')
EverBenched = st.number_input('Hiatus(berhenti sejenak)')
st.write('Tidak Berhenti(0), Berhenti(1)')
ExperienceInCurrentDomain = st.number_input('Pengalaman Pekerjaan sebelumnya')
st.write('indeks 0-7')
new_data = [Education, JoiningYear, City, PaymentTier, Age, Gender, EverBenched, ExperienceInCurrentDomain ]
res = pipeline.predict([new_data])
classes = [' Karyawan Stay','Karyawan Leave']
st.write(f"Hasil Prediksi :{classes[res[0]]}")