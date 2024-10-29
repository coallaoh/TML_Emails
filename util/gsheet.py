from gsheet_manager import GSheetManager
import tqdm


class GSheetToWrite(GSheetManager):
    @GSheetManager.batch_sync_with_remote
    def write_data_list(self, data_list):
        headers = sorted(list(data_list[0].keys()))
        for header_idx, header_name in enumerate(headers):
            self._set_buffer_cells(python_row_idx=0,
                                   python_col_idx=header_idx,
                                   value=header_name)

        for row_idx, d in tqdm.tqdm(enumerate(data_list)):
            for header_idx, header_name in enumerate(headers):
                self._set_buffer_cells(python_row_idx=row_idx + 1,
                                       python_col_idx=header_idx,
                                       value=d[header_name])


class GSheetWithHeader(GSheetManager):
    @property
    def headers(self):
        return self.local_sheet_values[0]

    def get_data_list(self):
        self.sync_from_remote()
        data_list = []
        for row in self.local_sheet_values[1:]:
            data_list.append(dict(zip(self.headers, row)))
        return data_list

    @GSheetManager.batch_sync_with_remote
    def write_rows(self, rows, headers=None, start_row_idx=0):
        if headers is None:
            headers = self.headers
            offset = 0
        else:
            for header_idx, header_name in enumerate(headers):
                self._set_buffer_cells(python_row_idx=start_row_idx,
                                       python_col_idx=header_idx,
                                       value=header_name)
            offset = 1

        for row_idx, d in enumerate(rows):
            for header_idx, header_name in enumerate(headers):
                self._set_buffer_cells(python_row_idx=row_idx + start_row_idx + offset,
                                       python_col_idx=header_idx,
                                       value=d[header_name])
        row_cursor = len(rows) + start_row_idx + 1
        return row_cursor
