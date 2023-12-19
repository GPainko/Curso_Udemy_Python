class TodoList:
    def __init__(self):
        self._tasks = []
        self._redo_stack = []

    def add_task(self, task):
        self._tasks.append(task)
        self._redo_stack.clear()

    def remove_task(self, task):
        if task in self._tasks:
            self._tasks.remove(task)
            self._redo_stack.clear()

    def show_tasks(self):
        for task in self._tasks:
            print(task)

    def undo(self):
        if self._tasks:
            task = self._tasks.pop()
            self._redo_stack.append(task)

    def redo(self):
        if self._redo_stack:
            task = self._redo_stack.pop()
            self._tasks.append(task)

# Uso do sistema de lista de tarefas com desfazer e refazer
if __name__ == "__main__":
    todolist = TodoList()
    print("Bem-vindo ao gerenciador de tarefas!")

    while True:
        print("\nOpções:")
        print("1 - Adicionar tarefa")
        print("2 - Remover tarefa")
        print("3 - Visualizar tarefas")
        print("4 - Desfazer")
        print("5 - Refazer")
        print("6 - Sair")
        
        choice = input("Escolha uma opção: ")

        if choice == "1":
            task = input("Digite a tarefa que deseja adicionar: ")
            todolist.add_task(task)
        elif choice == "2":
            task = input("Digite a tarefa que deseja remover: ")
            todolist.remove_task(task)
        elif choice == "3":
            todolist.show_tasks()
        elif choice == "4":
            todolist.undo()
            print("Ação desfeita.")
        elif choice == "5":
            todolist.redo()
            print("Ação refeita.")
        elif choice == "6":
            print("Saindo do gerenciador de tarefas...")
            break
        else:
            print("Opção inválida. Tente novamente.")