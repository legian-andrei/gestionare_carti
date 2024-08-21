

class AuditLog:
    def __init__(self, id, action, time):
        self.user_id = id
        self.action = action
        self.time = time


    def __str__(self):
        max_length = 38
        border_line = f"{'-' * (max_length + 4)}"
        lines = [
            f"\t\t\t\t{border_line}",
            f"User ID: {self.user_id}",
            f"Action: {self.action}",
            f"Time: {self.time}",
            border_line
        ]
        return '\n\t\t\t\t'.join(lines)