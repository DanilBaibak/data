import _torcharrow as velox
from torcharrow.column_factory import Device
from torcharrow.dtypes import DType
from torcharrow.icolumn import IColumn
from torcharrow.scope import Scope


class ColumnFromVelox:
    _data: velox.BaseColumn
    _finialized: bool

    @staticmethod
    def from_velox(
        scope: Scope, device: Device, dtype: DType, data: velox.BaseColumn, finialized: bool
    ) -> IColumn:
        col = scope.Column(dtype=dtype, to=device)
        col._data = data
        col._finialized = finialized
        return col