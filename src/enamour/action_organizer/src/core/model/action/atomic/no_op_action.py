from src.controller import controller_provider
from src.controller.controller import Controller
from src.core.model.action.action_type import ActionType
from src.core.model.action.atomic.generic.atomic_action import AtomicAction
from src.core.model.action.execution_method import ExecutionMethod
from src.core.model.action.selection_type import SelectionType, SelectAlways


class NoOpAction(AtomicAction):
    def __init__(self, selection_type: SelectionType = SelectAlways()):
        super(NoOpAction, self).__init__(
            action_type=ActionType.NO_OP, selection_type=selection_type, execution_method=ExecutionMethod.MULTIPLE
        )

    def get_controller(self) -> Controller:
        return controller_provider.no_op_controller
