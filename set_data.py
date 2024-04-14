from webscrap_test import *

page_link = f"https://wuzzuf.net/search/jobs/?a=hpb&q=Machine%20learning&start=0"

def scrap_all(start_link, num_pages):
    df_lst = []
    for i in range(num_pages):
        page_link = start_link[:-1] + str(i)
        df = scrap(page_link)
        df_lst.append(df)
    return df_lst

def meger_dfs(df_lst):
    return pd.concat(df_lst, ignore_index=True)

def to_csv_file(data_fram, csv_file_name):
    data_fram.to_csv(csv_file_name, index=False)


if __name__ == "__main__":
    # scrap machine learning search
    ml_search = f"https://wuzzuf.net/search/jobs/?a=hpb&q=machine%20learning&start=0"
    df_lst = scrap_all(ml_search, 13)
    to_csv_file(meger_dfs(df_lst), "Machine learning search.csv")

    # scrap data analysis search
    data_analysis_search = f"https://wuzzuf.net/search/jobs/?a=navbg&q=data%20analysis&start=0"
    df_lst = scrap_all(data_analysis_search, 134)
    to_csv_file(meger_dfs(df_lst), "Data Analysis search.csv")

    # # scrap data science search
    data_science_search = f"https://wuzzuf.net/search/jobs/?a=navbg%7Cspbg&q=data%20science&start=0"
    df_lst = scrap_all(data_science_search, 123)
    to_csv_file(meger_dfs(df_lst), "Data Science search.csv")

    # # scrap business intelligence search
    business_intelligence_search = f"https://wuzzuf.net/search/jobs/?a=navbg&q=business%20intelligence&start=0"
    df_lst = scrap_all(business_intelligence_search, 35)
    to_csv_file(meger_dfs(df_lst), "Business Intelligence search.csv")
