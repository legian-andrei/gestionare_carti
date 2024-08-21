from audit_log import *


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

    def get_logs_for_user(self, user):
        """
        Functie pentru obtinerea actiunilor efectuate de un utilizator.
        :param user: obiect de tip User pentru care se doresc actiunile
        :return: list(AuditLog) sau None daca nu exista actiuni
        """
        audit_query = "SELECT action, time FROM audit WHERE user_id = %s"
        actions = self.db_manager.execute_query(query=audit_query, params=(user.id,), fetch_all=True)
        return [AuditLog(user.id, action[0], action[1]) for action in actions] if actions else None
