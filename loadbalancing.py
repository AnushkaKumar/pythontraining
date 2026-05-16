from collections import defaultdict
from copy import deepcopy


class AssignmentSystem:
    def __init__(self, agents: list):
        self.agents = agents
        self.agent_limits_map = defaultdict(int)
        self.index = 0
        for agent in self.agents:
            self.agent_limits_map[agent] = 2

    def set_limit(self, agent_name, limit):
        self.agent_limits_map[agent_name] += limit

    def assign(self, conversation_id):
        n = len(self.agent_limits_map)
        index = 0
        for _ in range(n):
            agent = self.agents[index % n]
            index += 1
            if self.agent_limits_map[agent] > 0:
                self.agent_limits_map[agent] -= 1
                return agent

    def preview_assignments(self, count):
        temp_assignment_map = deepcopy(self.agent_limits_map)
        res = []
        n = len(temp_assignment_map)
        temp_index = 0

        for _ in range(count):
            for _ in range(n):
                agent = self.agents[temp_index % n]
                temp_index += 1
                if temp_assignment_map[agent] > 0:
                    temp_assignment_map[agent] -= 1
                    res.append(agent)
                    break
        return res


if __name__ == "__main__":
    system = AssignmentSystem(["Alice", "Bob", "Charlie"])
    system.set_limit("Bob", 4)
    system.set_limit("Charlie", 3)
    print(system.preview_assignments(4))  # Output: ["Alice", "Bob", "Charlie", "Alice"]
    system.assign(101)  # Assigns to Alice
    system.assign(102)  # Assigns to Bob
    system.assign(103)  # Assigns to Charlie
    system.assign(104)  # Assigns to Alice

    print(system.preview_assignments(5))  # ['Bob', 'Charlie', 'Bob', 'Charlie', 'Bob']

"""
agent_limits_map={
	
	"Alice":2
	"Bob":2
	"Charlie":2
}


(make a copy of this map) iterate over the new map, decrease the count by 1, until map count reaches 0
assignments = ["Alice","Bob","Charlie", "Alice","Bob","Charlie"]

=> update limits of Bob and Charlie
agent_limits_map={
	
	"Alice":2
	"Bob": 4
	"Charlie":3
}
assignments = ["Alice","Bob","Charlie", "Alice","Bob","Charlie", "Bob","Charlie","Bob"]

=> preview 4 assignments
first four values of assignments

["Alice","Bob","Charlie", "Alice"]

=> assign to 4 to first four from assignments

["Alice","Bob","Charlie", "Alice"] and also update the count of individuals in original map
agent_limits_map={
	
	"Alice":0
	"Bob": 3
	"Charlie":2
}
create new assingments = ["Bob","Charlie", "Bob","Charlie","Bob"]

=> preview assignments(5)
remaining assignments  = ["Bob","Charlie", "Bob","Charlie","Bob"]

"""
