import streamlit as st
import pandas as pd
import altair as alt

@st.cache
def baca_csv():
    DATA_PATH = 'the_progress.csv'
    data = pd.read_csv(DATA_PATH)
    return data

def main():
    st.title('Cabaran Cergas Sihat 2021')
    st.text('Together We Are Strong - Bersama kurus sempena Raya!!')

    selections = ['Syarat', 'Statistik']
    pilihan = st.sidebar
    pilihan.title('Menu')
    memilih = pilihan.selectbox('Pilih menu', selections)
    if memilih == 'Statistik':
        st.subheader('Statistik Semasa')
        df = baca_csv()
        st.write(df)

        st.subheader('Graf Semasa')
        # df_g = baca_csv()
        series = pd.DataFrame({
            'nama': ['Kamil', 'Kamil', 'WDaiya', 'WDaiya', 'Hisyam', 'Hisyam', 'AlFirdaus', 'AlFirdaus', 'Adz', 'Adz', 'Auni', 'Auni', 'Achik', 'Achik'],
            'masa': ['Minggu 0', 'Minggu 1', 'Minggu 0', 'Minggu 1', 'Minggu 0', 'Minggu 1', 'Minggu 0', 'Minggu 1', 'Minggu 0', 'Minggu 1', 'Minggu 0', 'Minggu 1', 'Minggu 0', 'Minggu 1'],
            'timbangan': [75.4,74.1,73.7,73.1,91,91.5,85,85,0,0.0,66.6,66.5,89.8,90.1]
        })
        basic_chart = alt.Chart(series).mark_line().encode(
            x='masa',
            y='timbangan',
            color='nama'
        ).properties(width=500,height=700)
        st.altair_chart(basic_chart)
        # st.line_chart(df_g)
    elif memilih == 'Syarat':
        st.subheader('Syarat-syarat pertandingan')
        st.write('1. Pertandingan terbuka kepada keluarga nukleus Arwah Wan Samsudin Bin Wan Ahmed')
        st.write('2. Timbangan peserta akan dilakukan setiap minggu')
        st.write('3. Pemenang akhir akan ditentukan di timbangan akhir')
        st.write('4. Peserta dengan jumlah susutan paling banyak akan diisytiharkan sebagai pemenang')
        st.write('5. Pemenang akan menerima hadiah wang tunai yang akan dimaklumkan kemudian')
        st.write('6. Peserta-peserta yang tidak bernasib baik dapat menambah keyakinan diri dengan imej badan positif') 

if __name__ == "__main__":
    main()