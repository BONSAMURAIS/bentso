from entsoe import EntsoePandasClient
import pandas as pd
from . import TOKEN


pd_client = EntsoePandasClient(api_key=TOKEN)
