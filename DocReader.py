from google.colab import auth
auth.authenticate_user()

import gspread, re, pandas as pd
from google.colab.data_table import DataTable
from google.auth import default
creds, _ = default()

gc = gspread.authorize(creds)

data = []

for link in links:
  worksheet = gc.open_by_url(link['url'])

  worksheet_list = worksheet.worksheets()
  worksheet_names = [ws.title for ws in worksheet_list]


  for ws in worksheet_names:
    current_worksheet = worksheet.worksheet(ws)
    criteria_re = re.compile(text_to_search, re.IGNORECASE)
    result = current_worksheet.findall(criteria_re)

    for cell in result:
      data.append({"Fonte": ws + " - " + link['name'], "Infos": cell.value})

df = pd.DataFrame(data)
df.head(500)