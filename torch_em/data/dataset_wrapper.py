from collections import Sized
from typing import Callable

from torch.utils.data import Dataset


class DatasetWrapper(Dataset):
    def __init__(self, dataset: Dataset, wrap_item: Callable):
        assert isinstance(dataset, Dataset) and isinstance(dataset, Sized), "iterable datasets not supported"
        self.dataset = dataset
        self.wrap_item = wrap_item

    def __getitem__(self, item):
        return self.wrap_item(self.dataset[item])

    def __len__(self):
        return len(self.dataset)
