

class AuditManager:
    """
    Clasa pentru gestionarea auditului.
    """

    def __init__(self, db_manager):
        self.db_manager = db_manager

    def log_action(self, user, action):
        """
        Functie pentru inregistrarea actiunilor utilizatorilor.

        :param user: utilizatorul care a efectuat actiunea
        :param action: descrierea actiunii efectuate
        """
        audit_entry = {
            'user_id': user.id,
            'action': action
        }
        self.db_manager.add_entry('audit', audit_entry)
