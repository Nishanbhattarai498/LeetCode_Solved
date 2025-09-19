class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.cols = 26
        self.cells = {}  # store only non-zero cells as {(row, col): value}

    def _parse_cell(self, cell: str):
        """Convert 'A1' -> (row_idx, col_idx)."""
        col = ord(cell[0]) - ord('A')      # column A-Z → 0-25
        row = int(cell[1:]) - 1            # row is 1-indexed
        return (row, col)

    def setCell(self, cell: str, value: int) -> None:
        r, c = self._parse_cell(cell)
        self.cells[(r, c)] = value

    def resetCell(self, cell: str) -> None:
        r, c = self._parse_cell(cell)
        if (r, c) in self.cells:
            del self.cells[(r, c)]

    def getValue(self, formula: str) -> int:
        expr = formula[1:]  # remove '='
        parts = expr.split('+')
        total = 0
        for part in parts:
            if part.isdigit():
                total += int(part)
            else:
                r, c = self._parse_cell(part)
                total += self.cells.get((r, c), 0)
        return total
