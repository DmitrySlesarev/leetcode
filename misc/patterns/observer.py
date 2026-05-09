from typing import List, Any, Optional


class Observer:
    def __init__(self, name: str = " "):
        self._state: Optional[Any] = None
        self._name = name

    def update(self, state: Any) -> None:
        self._state = state

    def __str__(self) -> str:
        return f"{self._name}: The state is {self._state}"


class Subject:
    def __init__(self):
        self._members: List[Observer] = list()
        self._state: Optional[Any] = None

    def add_observer(self, member: Observer) -> None:
        if member not in self._members:
            self._members.append(member)

    def remove_observer(self, member: Observer) -> None:
        if member in self._members:
            self._members.remove(member)

    def notify(self) -> None:
        for member in self._members:
            member._state = self._state

    def set_state(self, state: Any) -> None:
        self._state = state
        self.notify()


if __name__ == "__main__":
    member2 = Observer("Member 1")
    member3 = Observer("Member 2")

    observer = Subject()
    observer.add_observer(member2)
    observer.add_observer(member3)

    observer.set_state("Alarm")

    print(member2)
    print(member3)