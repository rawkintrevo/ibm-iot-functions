import logging

from requests import get, post
import pandas as pd

from iotfunctions.base import BaseTransformer
from iotfunctions import ui

logger = logging.getLogger(__name__)

# Specify the URL to your package here.
# This URL must be accessible via pip install

PACKAGE_URL = 'git+git://github.com/rawkintrevo/iot-functions-tutorial@'


class ExternalModel(BaseTransformer):

    def __init__(self, input_items, endpoint, output_items):

        self.input_items = input_items
        self.output_items = output_items
        self.endpoint = endpoint

        super().__init__()


    def execute(self, df):
        df = df.copy()
        assert(df, pd.DataFrame())
        df_dict = df.to_dict()
        r = get(self.endpoint, json= df_dict)

        return pd.DataFrame(r.json())

    @classmethod
    def build_ui(cls):
        #define arguments that behave as function inputs
        inputs = []
        inputs.append(ui.UIMultiItem(
            name = 'input_items',
            datatype=float,
            description = "Data items adjust",
            output_item = 'output_items',
            is_output_datatype_derived = True)
        )
        inputs.append(ui.UISingle(
            name = 'endpoint',
            datatype=str)
        )
        outputs = []
        return (inputs,outputs)