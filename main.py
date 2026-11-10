class ReportGenerator:
    """
    The 'expected' base component: a generic report generator.
    It provides a standard structure for reports.
    """
    def __init__(self, title, data):
        self.title = title
        self.data = data

    def _generate_header(self):
        return f"--- {self.title.upper()} REPORT ---\n"

    def _generate_body(self):
        body = "Data Items:\n"
        for item in self.data:
            body += f"- {item}\n"
        return body

    def _generate_footer(self):
        return "-- End of Report --\n"

    def generate_report(self):
        header = self._generate_header()
        body = self._generate_body()
        footer = self._generate_footer()
        return header + body + footer

class FinancialReportGenerator(ReportGenerator):
    """
    'Shaping to your needs': A specialized financial report generator.
    It extends the generic ReportGenerator to handle financial data
    by adding calculations and specific formatting.
    """
    def __init__(self, title, transactions):
        # Call the base class constructor (copying the expected initialization)
        super().__init__(title, transactions)
        self.transactions = transactions # Store for specific financial processing

    def _calculate_total(self):
        # Assume transactions are (description, amount) tuples
        return sum(amount for _, amount in self.transactions)

    def _calculate_average(self):
        if not self.transactions:
            return 0
        return self._calculate_total() / len(self.transactions)

    def _generate_body(self):
        # Override the generic body generation for financial specifics
        body = "Financial Transactions:\n"
        for desc, amount in self.transactions:
            body += f"- {desc}: ${amount:.2f}\n"
        
        total = self._calculate_total()
        average = self._calculate_average()
        body += f"\nTotal Amount: ${total:.2f}\n"
        body += f"Average Transaction: ${average:.2f}\n"
        return body

    def _generate_footer(self):
        # Optionally extend the footer with financial specific info
        base_footer = super()._generate_footer()
        return base_footer.replace("-- End of Report --", "-- End of Financial Report --")


# --- Demonstration ---
if __name__ == "__main__":
    print("--- Generic Report ---")
    generic_data = ["Item A", "Item B", "Item C", "Another Item"]
    generic_report = ReportGenerator("General Overview", generic_data)
    print(generic_report.generate_report())

    print("\n--- Financial Report (Shaped to Needs) ---")
    financial_transactions = [
        ("Salary", 3500.00),
        ("Rent", -1200.00),
        ("Groceries", -150.75),
        ("Bonus", 500.00),
        ("Utilities", -85.20)
    ]
    financial_report = FinancialReportGenerator("Monthly Expenses & Income", financial_transactions)
    print(financial_report.generate_report())
