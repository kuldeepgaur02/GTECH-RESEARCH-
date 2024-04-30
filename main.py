from sec_edgar_downloader import Downloader
import os

def download_10k_filings_for_multiple_companies(equity_ids, output_dir, limit=28):

    company_name = "gtech innovation"
    email_address = "gtech@gmail.com"
    dl = Downloader(company_name=company_name, email_address=email_address)
    
    
    for equity_id in equity_ids:
       
        company_subdir = os.path.join(output_dir, equity_id)
        os.makedirs(company_subdir, exist_ok=True)
        
        try:
           
            dl.get("10-K", equity_id, limit=limit)
            
           
            dl.move_files(equity_id, "10-K", company_subdir)
            
           
            print(f"Downloaded {limit} '10-K' filings for {equity_id} in {company_subdir}")
            
        except Exception as e:
            print(f"Error downloading '10-K' filings for {equity_id}: {e}")


equity_ids = ['MCD','PEP','WMT']


output_directory = "./10k_filings"

limit_per_company = 28

download_10k_filings_for_multiple_companies(equity_ids, output_directory, limit_per_company)
