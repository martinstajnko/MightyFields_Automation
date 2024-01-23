from core.init_driver import Initialization
from core.steps import CreateTask 
from core.dataclass import User


class TestCreateTask(Initialization):

    def test_create_and_close_task_in_test(self):
        
        category = 'test'
        user = User()
        create_task = CreateTask(self.driver, category, user)
        create_task.create_and_close_task()