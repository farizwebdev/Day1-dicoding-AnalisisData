import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import streamlit as st
from babel.numbers import format_currency
sn.set(style='dark')


## st.set_option('deprecation.showPyplotGlobalUse', False)
## marai error di streamlit versi terbaru wkwkk




def create_hour_df(hour_df):
    return hour_df.groupby(['yr', 'season'])['cnt'].agg('mean').reset_index()

    
def create_hour1_df(hour_df):
    hour_df1 = hour_df.groupby(["weathersit"])["cnt"].agg(["sum"]).reset_index()
    return hour_df1



def create_hour2_df(hour_df):
    hour_df2 = hour_df.groupby(["workingday"])["cnt"].agg(["sum"]).reset_index()
    return hour_df2



    




all_df = pd.read_csv("dashboard/hour.csv")


datetime_columns = ["dteday"]
all_df.sort_values(by="dteday", inplace=True)
all_df.reset_index(inplace=True)
 
for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])



min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("dashboard/bike.jpg")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )


main_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                (all_df["dteday"] <= str(end_date))]


hour_df = create_hour_df(main_df)
hour_df1 = create_hour1_df(main_df)
hour_df2 = create_hour2_df(main_df)



st.header('Proyek Analisis Data: Fariz Husain Albar')
st.subheader('Follow ig: @fariz.webdev')



data = pd.read_csv("dashboard/hour.csv")

# Tambahkan judul
st.subheader("1. Jumlah rata-rata persewaan sepeda per jam berdasarkan musim di kedua tahun")

if data['yr'].dtype == 'int64':
    data['yr'] = data['yr'].astype(str)

# Cek tipe data variabel kedua, jika integer, konversi ke string
if data['season'].dtype == 'int64':
    data['season'] = data['season'].astype(str)

# Hitung rata-rata untuk setiap kombinasi kategori
bar_data = data.groupby(['yr','season'])["cnt"].agg("mean").reset_index()

# Tampilkan dataframe
st.write("Data untuk Bar Chart:")
st.write(bar_data)

# Buat Bar Chart menggunakan Seaborn
fig, ax = plt.subplots(figsize=(12, 8))
sn.barplot(x='season', y="cnt", hue='yr', data=bar_data, palette="viridis", ax=ax)
ax.set_xlabel('Musim')
ax.set_ylabel("Jumlah Sewa Sepeda")
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(['Springer', 'Summer', 'Fall', 'Winter'])
ax.set_title("Jumlah pengguna dalam dua tahun berdasarkan musim")
ax.legend(title='Year', loc='best', labels=['2011', '2012'], frameon=False)
st.pyplot(fig)


st.write(
    """
    Penjelasan :

        1: Springer

        2: Summer

        3: Fall

        4: Winter

    Musim puncak adalah musim gugur karena rata-rata persewaan sepeda maksimal pada musim gugur untuk kedua tahun tersebut
    """
    )




# Tambahkan Judul
st.subheader('2. Pada hari apa permintaan sepeda per jam sedang tinggi, baik pada hari kerja maupun hari libur')

# Hitung jumlah hari permintaan yang tinggi
pie_data = data.groupby(["workingday"])["cnt"].agg(["sum"])

# Tampilkan Dataframe
st.write("Data untuk Pie Chart:")
st.write(pie_data)

# Buat Pie Chart menggunakan Seaborn


# Membuat pie chart
fig, ax = plt.subplots()
ax.pie(pie_data['sum'], labels=pie_data.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Pastikan pie chart berbentuk lingkaran

# Menampilkan pie chart menggunakan Streamlit
st.pyplot(fig)


st.write(
    """
    Penjelasan :

        1: Hari Kerja
        0: Hari Libur

    Karena jumlah penyewaan sepeda adalah 2292410 yang tinggi pada hari kerja, 
    jadi manajer bisnis harus berusaha untuk tidak memberikan cuti kepada stafnya pada hari kerja 
    karena permintaan tinggi pada hari-hari tersebut.
    """

    )




st.subheader('3. Bagaimana pengaruh situasi cuaca terhadap jumlah penyewaan sepeda per jam')

# Hitung jumlah hari permintaan yang tinggi
pie_data1 = data.groupby(["weathersit"])["cnt"].agg(["sum"])

# Tampilkan Dataframe
st.write("Data untuk Pie Chart:")
st.write(pie_data1)


# Membuat pie chart
fig, ax = plt.subplots()
ax.pie(pie_data1['sum'], labels=pie_data1.index, autopct='%1.1f%%', startangle=180)
ax.axis('equal')  # Pastikan pie chart berbentuk lingkaran

# Menampilkan pie chart menggunakan Streamlit
st.pyplot(fig)


st.write(
    """
    Penjelasan:

        1: Cerah, Sedikit awan, Berawan sebagian, Berawan sebagian

        2: Kabut + Berawan, Kabut + Awan pecah, Kabut + Sedikit awan, Kabut

        3: Salju Ringan, Hujan Ringan + Badai Petir + Awan berserakan, Hujan Ringan + Awan berserakan

        4: Hujan Lebat + Palet Es + Badai Petir + Kabut, Salju + Kabut

    Pada situasi (Cerah, Sedikit awan, Berawan sebagian, Berawan sebagian) jumlah sepeda sewaan maksimum dan pada situasi (Hujan Lebat + Palet Es + Badai Petir + Kabut, Salju + Kabut) jumlah sepeda sewaan lebih sedikit
    """
    )


 
st.caption('Copyright (c) Fariz Husain Albar 2023')