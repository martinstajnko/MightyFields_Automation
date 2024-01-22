from core.init_driver import Initialization
from core.steps import CreateTask 


class TestCreateTask(Initialization):

    def test_create_and_close_task(self):
        
        create_task = CreateTask(self.driver)
        create_task.create_and_close_task()