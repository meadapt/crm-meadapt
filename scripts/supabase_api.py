import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

def call_supabase():
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")

    # Debug information
    print(f"Attempting to connect to Supabase URL: {url}")

    if not url or not key:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in .env file")

    try:
        supabase: Client = create_client(url, key)
        response = supabase.table("crm_loja").select("*").execute()
        return response
    except Exception as e:
        print(f"Error connecting to Supabase: {str(e)}")
        raise

if __name__== '__main__':
    try:
        response = call_supabase()
        print("Response:", response)
    except Exception as e:
        print(f"Failed to execute Supabase query: {str(e)}")
