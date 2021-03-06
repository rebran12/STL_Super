# Import library yang dibutuhkan
import numpy as np
import seaborn as sns
import pandas as pd
import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
import datetime as dt
import calendar
import time
matplotlib.use('Agg')
from PIL import Image

st.set_option('deprecation.showPyplotGlobalUse', False) #Disable error bila error terjadi pada chart

#Design sidebar pada dashboard
st.sidebar.title("Supermarket Sales Data Analisis")
st.sidebar.markdown("Dashboard Analisis pada data supermarket sales yang mempunyai 3 branch dalam waktu 3 bulan")


def main():

    df = pd.read_csv("supermarket_sales_p.csv") #read data dari supermarket sales yang telah di proceed

    menu = ['Explore your dataset','Visualisasi Dataset','Hypothesis Test'] #Menu Sidebar
    choice=st.sidebar.selectbox("Menu",menu)
    if choice=='Explore your dataset':
        st.image("analysis1.jpg",use_column_width=True)
        st.info("Dashboard ini dibuat sebagai halaman data explore, dimana data dapat ditampilkan sesuai dengan yg di inginkan, dapat juga melihat dataset summary, dan juga apakah terdapat data yang missing values.")
        st.header("Explore your dataset")
        #df=pd.read_csv(data) test23


        if st.checkbox("Show Dataset"): #checkbox untuk menampilkan dataset
            number=st.number_input("Number of Rows to view",5,15)
            st.dataframe(df.head(number))
            st.success("Data loaded successfully") 


            data_dim= st.radio("Shape of the dataset:", ("Number of Rows","Number of Columns")) #radio button widget
            if st.button("Show Dimension"):
                if data_dim== 'Number of Rows':
                    st.write(df.shape[0])
                elif data_dim== 'Number of Columns':
                    st.write(df.shape[1])
                else:
                    st.write(df.shape)

            Info =['Dataset Information','Display Multiple Columns','Display the dataset summary','Check for missing values in the dataset']
            options=st.selectbox("Pilihan - pilihan terhadap dataset",Info)


            if options==('Dataset Information'): #cemacem dataset
                st.markdown("**Date Time**: Time of purchase.")
                st.markdown("**Branch**: Branches of the Supermarke)t.")
                st.markdown("**City**: Supermarkets location.")
                st.markdown("**Customer Type**: Members are member card holders and normal without member cards.")
                st.markdown("**Gender**: Gender type of customer.")
                st.markdown("**Product line**: General item categorization groups.")
                st.markdown("**Payment**: Payment method used by customer for purchase.")
                st.markdown("**Branch Location**: Location of Branch.")
                st.markdown("**UnitPrice**: Price of each product in U.S. Dollars.")
                st.markdown("**Quantity**: Number of products purchased by customer.")
                st.markdown("**Tax**: 5% tax fee on total amount.")
                st.markdown("**Total Sales**: Total price including tax.")
                st.markdown("**COGS**: Cost of goods sold.")
                st.markdown("**Gross margin percentage**: Gross margin percentage.")
                st.markdown("**Gross income**: Gross income.")
                st.markdown("**Rating**:Customer stratification rating for shopping experience(On a scale of 1 to 10).")


            if options=='Display Multiple Columns': #bila ingin menampilkan kolom tertentu
                 selected_columns=st.multiselect('Select Preferred Columns:',df.columns)
                 df1=df[selected_columns]
                 st.dataframe(df1)

            if options=='Check for missing values in the dataset': 
                 st.write(df.isnull().sum(axis=0)) #cekk null values
                 if st.button("Drop Null Values"):
                     df=df.dropna() #drop null values
                     st.success("Null values droped successfully")


            if options=='Display the dataset summary':
                 st.write(df.describe().T)
                 

    elif choice=='Visualisasi Dataset':
        st.image("visuals.jpeg",use_column_width=True)
        st.info("Dashboard ini dibuat sebagai halaman Visualisasi Data, dimana data dapat divisualisasikan sesuai dengan meassure, fact / labels, serta bar chart yg di inginkan")
        st.header("Visualisasikan dataset yang anda inginkan")
        #df=pd.read_csv(data)
            #st.dataframe(df.head(50))
        df['date_time']=pd.to_datetime(df['date_time'])

        df['Month']=pd.DatetimeIndex(df['date_time']).month
        #hadeuh
        df['MonthName'] = df['Month'].apply(lambda x: calendar.month_abbr[x])
        df['date_time'] = pd.to_datetime(df['date_time'])
        df['Hour'] = (df['date_time']).dt.hour


        if st.button("Show Dataset again"):
            st.dataframe(df.head(50)) #menampilkan kembali 50 dataset apabila diperlukan

        col1,col2,col3=st.columns(3)

        st.subheader("Bar Chart / Horizontal Bar Chart / Scatter Bar / Plot Bar")
        with col1:
            measure_selection = st.selectbox('Choose a Measure:', ['quantity','unit_price','total','cogs','gross_income'], key='1')
        with col2:
            fact_selection = st.selectbox('Choose a Fact:', ['product_line','city','payment','gender','customer_type','branch','MonthName','Hour'], key='1')
            ax=df.groupby([fact_selection])[measure_selection].aggregate('sum').reset_index().sort_values(measure_selection,ascending=True)
            dx=df.groupby([fact_selection])[measure_selection].aggregate('sum').reset_index().sort_values(fact_selection,ascending=True)
            #cust_data=ax xxx gatau mau diapain tar aj
        with col3:
            type_of_plot=st.selectbox("Select Type of Plot",["Bar Chart","Horizontal Bar", "Scatter Bar", "Plot Bar"])

        if type_of_plot=='Bar Chart':
            st.success("Menampilkan Custom Plot {} untuk pengukuran {} terhadap {}".format(type_of_plot,measure_selection,fact_selection))
            plt.xticks(rotation=45)
                #plt.subplots(figsize=(15, 7))
            plt.autoscale()
            plt.tight_layout(rect=(0, 0.25, 1, 1))
            plt.bar(ax[fact_selection], ax[measure_selection], align='center')
            plt.ylabel(fact_selection)
            st.pyplot()
    

        elif type_of_plot=='Horizontal Bar':
            st.success("Menampilkan Custom Plot {} untuk pengukuran {} terhadap {}".format(type_of_plot,measure_selection,fact_selection))
            plt.barh(ax[fact_selection], ax[measure_selection], align='center')
            #plt.barh(ax[measure_selection], ax[fact_selection])
            st.pyplot()
        
        
        elif type_of_plot=='Scatter Bar':
            st.success("Menampilkan Custom Plot {} untuk pengukuran {} terhadap {}".format(type_of_plot,measure_selection,fact_selection))
            plt.autoscale()
            plt.xticks(rotation=45)
            plt.xlabel(measure_selection)
            plt.tight_layout(rect=(0, 0.25, 1, 1))
            plt.scatter(ax[fact_selection], ax[measure_selection],color='green')
            plt.ylabel(fact_selection)
            plt.grid(True)
            st.pyplot()
            
            
        elif type_of_plot=='Plot Bar':
            st.success("Menampilkan Custom Plot {} untuk pengukuran {} terhadap {}".format(type_of_plot,measure_selection,fact_selection))
            plt.autoscale()
            plt.xticks(rotation=45)
            plt.xlabel(measure_selection)
            plt.tight_layout(rect=(0, 0.25, 1, 1))
            plt.plot(ax[fact_selection], ax[measure_selection],color='red')
            plt.ylabel(fact_selection)
            plt.grid(True)
            st.pyplot()        

        st.subheader("Donut Chart")
        #col5 = st.columns(1)
        #st.button('Donut Chart')
        st.success("Menampilkan Donut Chart untuk pengukuran {} terhadap {}".format(measure_selection,fact_selection))
        labels = dx[fact_selection].unique()
        #labels = ax[measure_selection].unique()
        #values =df.groupby([measure_selection])[fact_selection].sum()
        values =df.groupby([fact_selection])[measure_selection].sum()
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])
        #fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])
        st.plotly_chart(fig)
        
        
        
        # st.subheader("FF Chart")
        # st.success("Menampilkan Custom Plot {} untuk pengukuran {} terhadap {}".format(type_of_plot,measure_selection,fact_selection))
        # x1 = np.random.randn(200) - 2
        # x2 = np.random.randn(200)
        # x3 = np.random.randn(200) + 2
        # labels = [x1, x2, x3]
        # values =df.groupby([fact_selection])[measure_selection].sum()
        # fig = ff.create_distplot(
        #  labels, values, bin_size=[.1, .25, .5])
        # st.plotly_chart(fig, use_container_width=True)
        
        # st.subheader("Bubble Chart")
        # st.success("Menampilkan Custom Plot {} untuk pengukuran {} terhadap {}".format(type_of_plot,measure_selection,fact_selection))
        # labels = dx[fact_selection].unique()
        # values =df.groupby([fact_selection])[measure_selection].sum()
        # fig = go.Figure(go.Bar(labels, values, orientation='h'))
        # st.plotly_chart(fig)
        

    elif choice=='Hypothesis Test':
        st.image("Anova.png",use_column_width=True)
        st.info("Dashboard ini dibuat sebagai halaman Hipothesis testing Anova")
        
        st.header("Hipotesis Testing Pemasukan kotor toko")
        st.image('Rata-Rata Gross Income per-toko.png',use_column_width=True)
        Hipothesis = '''
Dapat dilihat pada tabel di atas, rata-rata pemasukan kotor dari 3 toko hampir
serupa. Tetapi sebelum membuat sebuah kesimpulan, akan lebih baik bila
memastikan terlebih dahulu, apakah perbedaan statistiknya signifikan / tidak
dan tidak terjadi secara kebetulan. Maka dari itu akan dilakukan pengujian
untuk membuat sebuah kesimpulan.'''
        st.code(Hipothesis, language='python')
        st.markdown('Box Plot Distribusi dari gross income terhadap 3 toko :')
        st.image("Distribusi.png",use_column_width=True)
        
        st.header("Metode Pengujian")
        st.markdown('Pengujian statistik yang dipilih untuk analisis ini adalah ANOVA (Analysis of Variance)')
        st.markdown('Karena tujuan dari analisis ini adalah untuk membandingkan pendapatan kotor setiap cabang toko (A,B,C).')
        st.markdown('ANOVA dipilih karena memiliki beberapa kategori :')
        
        
        anova = '''
1. Variabel kategori (Diskrit / Label)
2. Variabel kontinu (Matematis / Numerik)'''
        st.code(anova, language='python')
        
        st.subheader('''Test ANOVA
?? = 0.05 (Standart Hypothesis Test Signifikan) bila probabilitas hasil test lebih dari 0.05
maka H0 Diterima
- H0: Tidak ada perbedaan yang signifikan antara rata-rata gross income diantara 3 toko.
- H1: Ada perbedaan yang signifikan antara rata-rata gross income dari minimal 2 toko.''')
       
        
        st.subheader('''Menggunakan Permutasi Test
1. Observed means:
- A - Yangon: 14.9
- B - Mandalay: 15.2
- C - Naypyitaw: 16.1
2. Gross income variance: 0.365
3. Permutation test variance: 0.014''')
        st.image("permutasi.png",use_column_width=True)
        st.markdown('''Permutasi test dilakukan sebanyak 3000 kali dan menghasilkan
                    probabilitas sebesar **0.403**. Dimana Hasil tersebut lebih
                    besar daripada level signifikan yang telah di tentukan''')
        
        st.subheader('''Menggunakan F-Statistik
Setelah melakukan ANOVA test, didapatlah f-statistik dan juga **p-value** sebagai berikut
- F-Statistik = 0.4423
- P-Value     = 0.2006

P-Value lebih besar daripada level signifikan yang telah di tentukan''')
        
        
        st.header("Kesimpulan")
        Kesimpulan = '''
Dari kedua test di atas, **probabilitas** dan nilai **p-value** lebih besar 
daripada level signifikan yang telah ditentukan. Mengacu pada data tersebut 
maka dapat dikatakan bahwa terdapat kemungkinan yang sangat tinggi variansi 
dari gross income tiap toko terjadi secara kebetulan. 
Maka dari itu N0 / null hypotesis gagal untuk di tolak

Lalu Akhirnya dapat disimpulkan bahwa tidak ada perbedaan yang signifikan antara
rata-rata pendapatan kotor diantara 3 toko tersebut'''
        st.code(Kesimpulan, language='python')
        #df=pd.read_csv(data)
     
if __name__ == '__main__':
    main()
