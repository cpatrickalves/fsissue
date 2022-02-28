# This is an example feature definition file

from feast import Entity, FeatureView, FileSource, ValueType, FeatureStore
from datetime import datetime
from google.protobuf.duration_pb2 import Duration


# defines the feature source location
house_data_batch = FileSource(
    path="data/raw/houses.parquet",
    event_timestamp_column="created",
)

# Define an entity.
# You can think of entity as a primary key used to fetch features.
# The Entity object describes which column contains the entity identifier
house = Entity(name="Id", value_type=ValueType.INT64, description="house identifier",)

# combines the available column names (and types) with the entity identifier and the data location.
houses_feature_view = FeatureView(
    name="houses_features",
    entities=["Id"],
    # The TTL describes the maximal time difference between the actual event timestamp and the timestamp we want to get.
    # TTL time is relative to each timestamp within the entity dataframe.
    # TTL is not relative to the current point in time (when you run the query).
    ttl=Duration(seconds=86400 * 100),
    online=True,  # If you have only historical data, you may set the online parameter to False.
    batch_source=house_data_batch,
    tags={},
)

print("Feature View:", houses_feature_view)