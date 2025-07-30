import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide",page_title="Startup Dashboard")

df=pd.read_csv('startup_cleaned.csv')
df['Date']=pd.to_datetime(df['Date'],errors='coerce')
df['Year'] = df['Date'].dt.year
df['Month']=df['Date'].dt.month
top5_by_amount = df.groupby('Vertical')['Amount'].sum().nlargest(5)
top5_by_count = df['Vertical'].value_counts().nlargest(5)

def load_overall_analysis():
    st.title("Overall Analysis")

    #total invested amount

    total_fund=round(df['Amount'].sum())

    #maximum fund infused in the startup

    max_funding=round(df.groupby('Startup')['Amount'].max().sort_values(ascending=False).values[0])

    avg_funding=round(df.groupby('Startup')['Amount'].sum().mean())

    count_startups=df.groupby('Startup')['Amount'].count().sum()

    col1,col2,col3,col4=st.columns(4)

    with col1:
        st.metric('Total Fund',str(total_fund)+'Cr')

    with col2:
        st.metric('Maximum Fund', str(max_funding) + 'Cr')

    with col3:
        st.metric('Average Fund', str(avg_funding) + 'Cr')

    with col4:
        st.metric('Funded Startups', count_startups)

    st.header('MOM Graph')
    selected_option=st.selectbox('Select Type',['Total','Count'])
    if selected_option=='Total':
        temp_df = df.groupby(['Year', 'Month'])['Amount'].sum().reset_index()

    else:
        temp_df = df.groupby(['Year', 'Month'])['Amount'].count().reset_index()
    temp_df['X-axis'] = temp_df['Month'].astype('str') + '-' + temp_df['Year'].astype('str')

    fig5, ax5 = plt.subplots()
    ax5.plot(temp_df['X-axis'],temp_df['Amount'])

    st.pyplot(fig5)

    col1,col2=st.columns(2)

    hello= st.selectbox('Choice', ['Amount', 'Count'])
    if hello=='Amount':
        with col1:
            st.subheader('Sector Analysis By Amount')
            fig6, ax6 = plt.subplots()
            ax6.pie(top5_by_amount,labels=top5_by_amount.index,autopct='%1.1f%%')

            st.pyplot(fig6)


    else:
        with col2:
            st.subheader('Sector Analysis By Count')
            fig7, ax7 = plt.subplots()
            ax7.pie(top5_by_count,labels=top5_by_count.index,autopct='%1.1f%%')

            st.pyplot(fig7)

    st.subheader("Funding Types Overview")

    # Pie chart by count (number of deals per funding type)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**By Number of Deals**")
        round_count = df['Round'].value_counts().nlargest(7)
        fig8, ax8 = plt.subplots()
        ax8.pie(round_count, labels=round_count.index, autopct='%1.1f%%')
        st.pyplot(fig8)

    with col2:
        st.markdown("**By Total Investment Amount**")
        round_amount = df.groupby('Round')['Amount'].sum().nlargest(7)
        fig9, ax9 = plt.subplots()
        ax9.pie(round_amount, labels=round_amount.index, autopct='%1.1f%%')
        st.pyplot(fig9)

    st.subheader("City-wise Total Funding")

    # Grouping by City
    city_funding = df.groupby('City')['Amount'].sum().sort_values(ascending=False).head(10)
    fig10, ax10 = plt.subplots()
    ax10.bar(city_funding.index, city_funding.values)

    st.pyplot(fig10)

    # heatmap

    heatmap_data = df.groupby(['Year', 'Month'])['Amount'].sum().unstack().fillna(0)

    st.subheader("Funding Heatmap (Year vs Month)")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(heatmap_data, cmap="YlGnBu", linewidths=0.5, annot=True, fmt=".0f", ax=ax)
    ax.set_title("Total Funding (in INR) by Year and Month")
    st.pyplot(fig)

def load_startup_details(startup):
    st.title(startup)

    st.subheader('Sorry ,But the dataset through which i have created this project not contains details of founders ')









def load_investor_details(investor):
    st.title(investor)
    #load the recent two investments  of the investor
    last2_df=df[df['Investors'].str.contains(investor)].head()[['Date','Startup','Vertical','City','Round','Amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last2_df)

    col1,col2=st.columns(2)
    with col1:
        # biggest investments
        big_series=df[df['Investors'].str.contains(investor)].groupby('Startup')['Amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index,big_series.values)

        st.pyplot(fig)

    with col2:
        vertical_series=df[df['Investors'].str.contains(investor)].groupby('Vertical')['Amount'].sum()

        st.subheader('Sectors Invested In')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series,labels=vertical_series.index,autopct='%1.1f%%')

        st.pyplot(fig1)

    col1,col2=st.columns(2)
    with col1:
        stage_series = df[df['Investors'].str.contains(investor)].groupby('Round')['Amount'].sum()

        st.subheader('Stage Invested In')
        fig2, ax2 = plt.subplots()
        ax2.pie(stage_series,labels=stage_series.index,autopct='%1.1f%%')

        st.pyplot(fig2)

    with col2:
        city_series = df[df['Investors'].str.contains(investor)].groupby('City')['Amount'].sum()

        st.subheader('Cities Invested In')
        fig3, ax3 = plt.subplots()
        ax3.pie(city_series,labels=city_series.index,autopct='%1.1f%%')

        st.pyplot(fig3)

    year_series=df[df['Investors'].str.contains(investor, na=False)].groupby('Year')['Amount'].sum()

    st.subheader('YOY Investment ')
    fig4, ax4 = plt.subplots()
    ax4.plot(year_series.index,year_series.values)

    st.pyplot(fig4)







st.sidebar.title('Startup Funding Analysis')

option=st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])


if option=='Overall Analysis':
    load_overall_analysis()

elif option=='Startup':
    selected_startup=st.sidebar.selectbox('Select Startup',sorted(df['Startup'].unique().tolist()))
    btn1=st.sidebar.button('Find Startup Details')
    if btn1:
        load_startup_details(selected_startup)

else:
    selected_investor=st.sidebar.selectbox('Select Startup',sorted(set(df['Investors'].str.split(',').sum())))
    btn2=st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)



