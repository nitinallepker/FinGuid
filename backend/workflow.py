class FinancialWorkflow:

    def __init__(self):
        self.stage = 1
        self.data = {}
        self.history = []

    def next_step(self, user_input):

        if self.stage == 1:

            self.data["goal"] = user_input
            self.stage = 2

            return (
                "Great.\n\n"
                "Approximately how much money will you need "
                "to achieve this goal?"
            )

        elif self.stage == 2:

            self.data["target_amount"] = user_input
            self.stage = 3

            return (
                "When do you plan to achieve this goal?\n\n"
                "Examples:\n"
                "- 3 years\n"
                "- 5 years\n"
                "- 10 years"
            )

        elif self.stage == 3:

            self.data["timeline"] = user_input
            self.stage = 4

            return (
                "Tell me about your current financial position.\n\n"
                "You can include:\n"
                "- Monthly Income\n"
                "- Savings\n"
                "- Current Investments(if any)\n"
                "- Loans / EMIs\n"
                "- Any other relevant financial information"
            )

        elif self.stage == 4:

            self.data["financial_position"] = user_input
            self.stage = 5

            return "PROFILE_COMPLETE"

        return None