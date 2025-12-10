from supabase import create_client
import os

SUPABASE_URL = os.getenv("https://stbevycnigjecrbhjixu.supabase.co")
SUPABASE_KEY = os.getenv("sb_secret__sN7IxqPMWNgjAUHUkFEIw_fPAmIZBl")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
