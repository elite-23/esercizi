import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import numpy as np

class DataSourceConfig:
    """Configurazione sorgenti dati e destinazione output"""
    db_uri: str = "postgresql+psycopg://postgres:postgres@postgresql:5432/transactions_db"
    csv_path: str = "../../dati/retail/"


class DataPipeline:
    def __init__(self, config: DataSourceConfig):
        self.config = config
        self.data = None
        
    def load_from_csv(self,name:str) -> pd.DataFrame:
        """Carica dati da un file CSV"""
        return pd.read_csv(self.config.csv_path+name)        

    def load_from_remote(self) -> pd.DataFrame:
        """Carica dati da un file remoto identificato da un URL aggiungendo intestazioni"""
        headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
                  "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
                  "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
                  "peak-rpm","city-mpg","highway-mpg","price"]
        return pd.read_csv(self.config.remote_url, names = headers)
    
    def save_on_csv(self, df: pd.DataFrame) -> None:
        """Salva dati in un file CSV"""
        df.to_csv(self.config.csv_path)    
    
    def store_on_database(self, df: pd.DataFrame) -> None:
        """Scrive dati in un database PostgreSQL"""      
        table_name = "auto_info"
        engine = create_engine(self.config.db_uri)
        try:
            with engine.begin() as conn:  # begin() per gestione automatica di commit/rollback
                df.to_sql(table_name, con=conn, if_exists='replace', index=False)
        except SQLAlchemyError as e:
            print(f"Error di scrittura in database: {e}")
        finally:
            engine.dispose()  # Chiusura pulita e rilascio risorse
        
    def load_from_database(self) -> pd.DataFrame:
        """Carica dati da un database PostgreSQL"""
        query_def = "SELECT * FROM public.auto_info"        
        engine = create_engine(self.config.db_uri)
        try:
            with engine.connect() as conn:
                df = pd.read_sql_query(text(query_def), con=conn)[['make', 'price']].head()
        except SQLAlchemyError as e:
            print(f"Errore di lettura da database: {e}")
            df = pd.DataFrame() 
        finally:
            engine.dispose()  # Chiusura pulita e rilascio risorse
        return df

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Operazioni varie di pulizia dati"""

        df.replace({'StockCode': {"POST": "?", "C2": "?", "D": "?", "M": "?"}},inplace=True)

        df[df["Country"].str.contains(",")].replace(value="?",inplace=True)

        df.replace("?",np.nan, inplace=True)

        df.dropna(subset=["StockCode"], axis=0, inplace=True)
        df.reset_index(drop=True, inplace=True)

        df["Country"].replace(np.nan, df["Country"].value_counts().idxmax(), inplcae=True)
        
        df["Country"].replace("Unspecified",np.nan, inplace=True)
        df.dropna(subset=["Country"], axis=0, inplace=True)
        df.reset_index(drop=True, inplace=True)

        df[df["Quantity"]<0].replace(value=np.nan, inplace=True)
        df.dropna(subset=["Quantity"], axis=0, inplace=True)
        df.reset_index(drop=True, inplace=True)
        return df 
    
    def run_pipeline(self) -> pd.DataFrame:
        """Esegue la pipeline completa"""

        customer_df = self.load_from_csv("customer.csv")
        customer_df.rename(columns={"Col1": "CustomerID", "Col2": "Country"})

        product_df = self.load_from_csv("product.csv")
        product_df.rename(columns={"Col1": "StockCode", "Col2": "Description"})

        transaction_df = self.load_from_csv("transaction.csv")
        
        merged_df = pd.merge(customer_df, transaction_df, on="CustomerID")

        self.store_on_database(merged_df)
        db_df = self.load_from_database()

        df_final=pd.merge(product_df, db_df, on="StockCode")

        # Pulizia dati
        cleaned_df = self.clean_data(df_final)


        print("Pulizia dati completata")
        self.data = cleaned_df
        return cleaned_df


if __name__ == "__main__":
    config = DataSourceConfig() # Usa default DataSourceConfig
    pipeline = DataPipeline(config) # Esegui la pipeline
    final_df = pipeline.run_pipeline()
    print("Pipeline completata con successo!")
    print(final_df.head())