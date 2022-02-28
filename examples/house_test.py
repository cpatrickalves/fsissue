#from feast.infra.offline_stores.file import SavedDatasetFileStorage
from feast import FeatureStore
import pandas as pd
from datetime import datetime


# repo_path points to the directory where the feature_store.yaml is stored
store = FeatureStore(repo_path=".")

entity_df = pd.DataFrame.from_dict(
    {
        "Id": [893, 414, 523],
        "event_timestamp": datetime(2022, 2, 10, 15, 28, 28),
    })

job = store.get_historical_features(
    entity_df=entity_df,
    features=["houses_features:YrSold", "houses_features:SaleCondition", "houses_features:SalePrice"],
)

print(job.to_df())
