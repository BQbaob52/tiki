import httpx
import pandas as pd

def fetch_tiki_data(category_id, num_pages=20):
    base_url = 'https://tiki.vn/api/personalish/v1/blocks/listings'
    headers = {'Host': 'tiki.vn'}

    all_records = []
    for page in range(1, num_pages + 1):
        params = {'category': category_id, 'page': page}
        response = make_api_request(base_url, params, headers)
        dict_response = response.json()
        records = dict_response.get('data', [])
        all_records.extend(records)

    df = pd.DataFrame(all_records)
    return df

# Example usage:
category_id = 8594  # Replace with the desired category ID
result_df = fetch_tiki_data(category_id, num_pages=20)
result_df  # Print the first 3 rows of the combined DataFrame