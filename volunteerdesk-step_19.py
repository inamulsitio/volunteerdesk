# === Stage 19: Add undo support for the last simple mutation ===
# Project: VolunteerDesk
# Undo support for the last simple mutation

class UndoStack:
    def __init__(self):
        self.history = []

    def push(self, action):
        self.history.append(action)

    def undo(self):
        if self.history:
            return self.history.pop()
        return None

# Example usage:
undo_stack = UndoStack()
undo_stack.push("Mutation 1")
undo_stack.push("Mutation 2")
last_action = undo_stack.undo()
print(f"Undid: {last_action}")
