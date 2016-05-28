from datetime import datetime

from client.domain.enums import ExecutionReportStatus, ExecutionReportErrorCode, InstructionReportStatus, \
    InstructionReportErrorCode
from client.domain.request.bettingrequest import PlaceInstruction, CancelInstruction, UpdateInstruction


class ExecutionReport:
    def __init__(self, status: ExecutionReportStatus, customer_ref: str = None,
                 error_code: ExecutionReportErrorCode = None, market_id: str = str, instruction_reports: list() = None):
        self._status = status
        self._customer_ref = customer_ref
        self._error_code = error_code
        self._market_id = market_id
        self._instruction_report = instruction_reports


class InstructionReport:
    def __init__(self, status: InstructionReportStatus, error_code: InstructionReportErrorCode):
        self._status = status
        self._error_code = error_code


class PlaceInstructionReport(InstructionReport):
    def __init__(self, status: InstructionReportStatus, instruction: PlaceInstruction,
                 error_code: InstructionReportErrorCode = None, bet_id: str = None, place_date: datetime = None,
                 average_price_matched: float = None, size_matched: float = None):
        super().__init__(status, error_code)
        self._instruction = instruction
        self._bet_id = bet_id
        self._place_date = place_date
        self._average_price_matched = average_price_matched
        self._size_matched = size_matched


class CancelInstructionReport(InstructionReport):
    def __init__(self, status: InstructionReportStatus, size_cancelled: float,
                 error_code: InstructionReportErrorCode = None, instruction: CancelInstruction = None,
                 cancelled_date: datetime = None):
        super().__init__(status, error_code)
        self._size_cancelled = size_cancelled
        self._instruction = instruction
        self._cancelled_date = cancelled_date


class UpdateInstructionReport(InstructionReport):
    def __init__(self, status: InstructionReportStatus, instruction: UpdateInstruction,
                 error_code: InstructionReportErrorCode = None):
        super().__init__(status, error_code)
        self._instruction = instruction


class ReplaceInstructionReport(InstructionReport):
    def __init__(self, status: InstructionReportStatus, error_code: InstructionReportErrorCode = None,
                 cancel_instruction_report: CancelInstructionReport = None,
                 place_instruction_report: PlaceInstructionReport = None):
        super().__init__(status, error_code)
        self._cancel_instruction_report = cancel_instruction_report
        self._place_instruction_report = place_instruction_report
